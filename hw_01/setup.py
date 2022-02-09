from setuptools import setup

setup(
    name="fibastprint",
    version="0.1.0",
    packages=['fibastprint'],
    description="fibastprint",
    url="https://github.com/turovkv/python-hw/tree/main/hw_01",
    author="turovkv",
    author_email="turovkv@yandex.ru",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=[
        "networkx~=2.6.3",
        "matplotlib~=3.5.1",
        "pydot~=1.4.2",
    ],
)
