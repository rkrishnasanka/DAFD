# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='DAFD',
    version='0.1.0',
    python_requires='==3.8',
    author='Radhakrishna Sanka',
    author_email='rkrishnasanka@gmail.com',
    packages=['dafd'],
    package_dir={"": "."},
    package_data={
        "dafd": [
            "*.txt", "helper_scripts/*.png",
            "helper_scripts/experimental_data/*.csv",
            "models/forward_models/saved/*.h5",
            "models/forward_models/saved/*.json",
            "models/forward_models/saved/*.md",
            "models/regime_models/saved/*.h5",
            "models/regime_models/saved/*.json",
            "models/regime_models/saved/*.md"
        ]
    },
    install_requires=[
        'keras==2.*,>=2.4.3', 'matplotlib==3.*,>=3.3.1', 'pandas==1.*,>=1.1.2',
        'scikit-learn==0.*,>=0.23.2', 'tensorflow==2.*,>=2.3.0',
        'tqdm==4.*,>=4.48.2'
    ],
)