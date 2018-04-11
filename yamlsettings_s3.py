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
        client = boto3.client('s3')

        data = client.get_object(
            Bucket=hostname,
            Key=path.lstrip('/'),
        )['Body'].read()

        return load_method(data)
