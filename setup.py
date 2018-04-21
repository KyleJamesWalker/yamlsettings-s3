from setuptools import setup

readme = open('README.rst').read()

requirements = {
    "package": [
        'six',
        'boto3',
        'yamlsettings>=1.0.1',
    ],
    "setup": [
        "pytest-runner",
    ],
    "test": [
        "pytest",
        "pytest-mock",
        "pytest-pudb",
    ],
}

requirements.update(all=sorted(set().union(*requirements.values())))

setup(
    name='yamlsettings-s3',
    version='1.0.0',
    author='Kyle Walker',
    author_email='KyleJamesWalker@gmail.com',
    description='YamlSettings S3 Extension',
    long_description=readme,
    py_modules=['yamlsettings_s3'],
    extras_require=requirements,
    install_requires=requirements['package'],
    setup_requires=requirements['setup'],
    tests_require=requirements['test'],
    entry_points={
        'yamlsettings10': [
            'ext = yamlsettings_s3:S3Extension',
        ],
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
