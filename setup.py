import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="dragonglass",
    version="0.0.1",
    author="Ryan Willett",
    author_email="ryan.willett@gmail.com",
    description="Software package for Python to work with Obsidian notetaking software",
    long_description=long_description,
    url="https://github.com/rtwillett/DragonGlass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "wheel",
        "jupyter",
        "os",
        "glob",
        "re"
    ]
)