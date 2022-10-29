from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = [
'cvxopt==1.2.5',
'image==1.5.32',
'ipython==7.18.1',
'ipythonblocks==1.9.0',
'ipywidgets==7.5.1',
'jupyter==1.0.0',
'keras==2.4.3',
'matplotlib==3.3.2',
'networkx==2.5',
'numpy==1.18.5',
'opencv-python==4.4.0.44',
'pandas==1.1.3',
'pillow==7.2.0',
'pytest-cov==2.10.1',
'qpsolvers==1.4',
'scipy==1.5.2',
'sortedcontainers==2.2.2',
]

setup(
    name="alda",
    version="0.2.0",
    author="Tao Xiang",
    author_email="tao.xiang@tum.de",
    description="A package of algorithms.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/leoxiang66/Algorithms-and-Data-Structures",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
  "Programming Language :: Python :: 3.7",
  "License :: OSI Approved :: MIT License",
    ],
)