# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='quidam',
    version="1.11",
    packages=find_packages(),
    author="megadose",
    install_requires=["requests","fake_useragent","evolut","argparse"],
    description="Permet de recupérer des informations grace a la fonction mot de passe oubliée de certains sites",
    long_description="",
    include_package_data=True,
    url='http://github.com/megadose/Quidam',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
