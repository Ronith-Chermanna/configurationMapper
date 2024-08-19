from setuptools import setup, find_packages

setup(
    name="config_mapper",
    version="0.1",
    author="Chermanna MT",
    author_email="ronithchermanna@gmail.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
       "PyYAML",
        "pytest"
    ],
)


