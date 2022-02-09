from setuptools import setup, find_packages

setup(
    name="fib-ast-print",
    version="0.1.0",
    packages=find_packages(),
    description="fib-ast-print",
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
        "networkx",
        "matplotlib",
        "pydot",
    ],
)
