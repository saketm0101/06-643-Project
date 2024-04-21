"""Setup for the package."""
from setuptools import setup

setup(
    name="distillation",
    version="0.0.1",
    description="package utilities",
    maintainer="Saket Mundra",
    maintainer_email="saketram@andrew.cmu.edu",
    license="MIT",
    packages=["distillation"],
    entry_points={"console_scripts": ["oa = package.main:main"]},
    long_description="""\

package utilities
==============
Handy functions for a project.""",
)
