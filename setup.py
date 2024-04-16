from setuptools import find_packages, setup

# def parse_requirements_file(filename):
#     """ Load requirements from a pip requirements file """
#     with open(filename, 'r') as file:
#         lines = [line.strip() for line in file if line.strip() and not line.startswith('#')]
#     return lines

setup(
    name="yolov7",
    version="1.0",
    # install_requires=parse_requirements_file('requirements.txt'),
    install_requires=[],
)