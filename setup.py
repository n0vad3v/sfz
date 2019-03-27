import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sfz",
    version="0.0.2",
    author="Nova Kwok",
    author_email="n0vad3v@riseup.net",
    description="A simple Package to deal with Mainland ID Card Number.（一个用来处理大陆身份证号码的小包）。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/n0vad3v/sfz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
