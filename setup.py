import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sfz-novakwok",
    version="0.0.2",
    author="Nova Kwok",
    author_email="n0vad3v@riseup.net",
    description="A simple Package to deal with Mainland ID Card Number.（一個用來處理大陸身份證號碼的小包）。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n0vad3v/sfz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
