# from __future__ import unicode_literals
from io import StringIO

import boto3
import yamlsettings
import pytest


@pytest.fixture
def s3(mocker):
    """Patch Boto3 S3 Calls"""
    s3_patch = mocker.patch('boto3.client')
    s3_patch.return_value.get_object.return_value = {
        'Body': StringIO(u"foo: bar"),
    }

    return s3_patch


def test_basic_request(s3):
    """Test Basic Request"""
    config = yamlsettings.load("s3://bucket/key.yaml")
    assert config.foo == 'bar'
    s3.assert_called_once_with('s3')
    s3.return_value.get_object.assert_called_once_with(
        Bucket='bucket',
        Key='key.yaml',
    )


def test_pass_client(s3):
    """Verify client not created when passed"""
    client = boto3.client('mocked')
    config = yamlsettings.load("s3://bucket/long/key.yaml", client=client)
    assert config.foo == 'bar'
    s3.assert_called_once_with('mocked')
    s3.return_value.get_object.assert_called_once_with(
        Bucket='bucket',
        Key='long/key.yaml',
    )


def test_version_used(s3):
    """Verify version is used"""
    config = yamlsettings.load("s3://bucket/key.yaml", VersionId='mocked')
    assert config.foo == 'bar'
    s3.return_value.get_object.assert_called_once_with(
        Bucket='bucket',
        Key='key.yaml',
        VersionId='mocked',
    )


def test_client_params(s3):
    """Test params passed to client"""
    config = yamlsettings.load("s3://bucket/key.yaml", region_name='us-east-1')
    assert config.foo == 'bar'
    s3.assert_called_once_with('s3', region_name='us-east-1')
    s3.return_value.get_object.assert_called_once_with(
        Bucket='bucket',
        Key='key.yaml',
    )


def test_client_params_via_url_params(s3):
    """Test params passed to client via url"""
    config = yamlsettings.load("s3://bucket/key.yaml?region_name=us-east-1")
    assert config.foo == 'bar'
    s3.assert_called_once_with('s3', region_name='us-east-1')
    s3.return_value.get_object.assert_called_once_with(
        Bucket='bucket',
        Key='key.yaml',
    )
