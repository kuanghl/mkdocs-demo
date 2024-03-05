import setuptools

with open("READMEmd", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kuanghl",
    version="0.0.1",
    author="kuanghl",
    author_email="kuanghl98@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)