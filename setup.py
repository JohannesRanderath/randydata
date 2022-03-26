from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="randydata",
    version="0.3",
    description="Tools for SQL or Excel of observational data handling.",
    long_description=readme(),
    keywords="excel sql data handling",
    url="https://github.com/JohannesRanderath/randydata",
    author="Johannes Randerath",
    author_email="randydata@randerath.eu",
    license="MIT",
    packages=["randydata"],
    install_requires=["pandas>=1.4.1", "mysql>=0.0.3", "sqlalchemy>=1.4.32", "IPython>=8.1.1"],
    include_package_data=True
)
