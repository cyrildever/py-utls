import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-utls",
    version="0.3.0",
    author="Cyril Dever",
    author_mail="cdever@pep-s.com",
    description="Utilities for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyrildever/py-utls",
    project_urls={
        "Bug Tracker": "https://github.com/cyrildever/py-utls/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "python",
        "utils",
        "chunks",
        "flatten",
        "hexadecimal",
        "euclidean division",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
