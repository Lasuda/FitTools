from setuptools import setup, find_packages

setup(
    name="fittools",
    version="0.1.0",
    packages=find_packages(),
    description="A simple math utilities package",
    long_description=open("README.md").read() if open("README.md", errors="ignore") else "",
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="cuitf@ihep.ac.cn",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)