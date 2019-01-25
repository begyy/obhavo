import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Obhavo",
    version="0.4",
    author="Sadullayev Bekhzod",
    author_email="begymrx@gmail.com",
    description="ObhavoUz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/begyy/obhavo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
