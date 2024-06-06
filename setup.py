from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
    requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name='space_agent',
    version="0.0.1",
    description="to-infinity-and-beyond utility module",
    license="MIT",
    author="A-Team",
    author_email="contact@lewagon.org",
    install_requires=requirements,
    packages=find_packages(),
    test_suite="tests",
    include_package_data=True,
    zip_safe=False
)
