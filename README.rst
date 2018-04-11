yamlsettings-s3
---------------------

YamlSettings Extension for http files

.. image:: https://travis-ci.org/KyleJamesWalker/yamlsettings-s3.svg?branch=master
    :target: https://travis-ci.org/KyleJamesWalker/yamlsettings-s3

.. image:: https://codecov.io/gh/KyleJamesWalker/yamlsettings-s3/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/KyleJamesWalker/yamlsettings-s3

Usage
=====

.. code-block:: python

 import yamlsetttings

 config = yamlsettings.load('s3://bucket/path/to/key/config.yaml')
