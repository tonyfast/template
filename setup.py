# coding: utf-8
import setuptools

setuptools.setup(
    name="{{name}}",
    version="0.0.1",
    author="{{author.name}}",
    author_email="{{author.email}}",
    description="{{about}}",
    license="BSD-3-Clause",
    url="http://github.com/{{author.user}}/{{name}}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Utilities",
        "Framework :: IPython",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Documentation",
    ],
    install_requires=[],
    tests_require=[],)
