import boto3

from yamlsettings.extensions.base import YamlSettingsExtension


class S3Extension(YamlSettingsExtension):
    """Open S3 Keys"""
    protocols = ['s3']

    @classmethod
    def load_target(cls, scheme, path, fragment, username,
                    password, hostname, port, query,
                    load_method, **kwargs):
        """Load Target from S3"""
        params = {}
        params.update(query)
        params.update(kwargs)

        client = params.pop('client', None)
        version_id = params.pop('VersionId', None)
        get_kwargs = {}

        if version_id:
            get_kwargs['VersionId'] = version_id

        if client is None:
            client = boto3.client('s3', **params)

        data = client.get_object(
            Bucket=hostname,
            Key=path.lstrip('/'),
            **get_kwargs
        )['Body'].read()

        return load_method(data)
