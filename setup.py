import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pagent-dmiracle", # Replace with your own username
    version="0.0.1",
    author="Dylan Miracle",
    author_email="dylan.miracle@gmail.com",
    description="A probabalistic agent",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmiracle/pagent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)