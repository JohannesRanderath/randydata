from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="randydata",
    version="0.2",
    description="Tools for SQL or Excel of observational data handling.",
    long_description=readme(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming language :: Python :: 3.8",
        "Topic :: Data :: Excel :: SQL :: OOP"
    ],
    keywords="excel sql data handling",
    url="https://github.com/JohannesRanderath/randydata",
    author="Johannes Randerath",
    author_email="randydata@randerath.eu",
    license="MIT",
    packages=["randydata"],
    install_requires=["pandas", "mysql", "sqlalchemy", "IPython"],
    include_package_data=True
)
