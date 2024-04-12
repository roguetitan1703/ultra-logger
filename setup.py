from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()
    
    
setup(
    name='ultra_logger',
    version='0.1.1',
    packages=find_packages(),
    author="Om Sing Chandel",
    author_email="omchandel1703@gmail.com",
    description="This Python package provides a robust and customizable logger that simplifies the process of recording messages and events in your applications. It leverages the power of the `colorlog` library to enhance readability and debugging capabilities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'certifi==2024.2.2',
        'charset-normalizer==3.3.2',
        'colorama==0.4.6',
        'colorlog==6.8.2',
        'docutils==0.21.1',
        'idna==3.7',
        'importlib_metadata==7.1.0',
        'jaraco.classes==3.4.0',
        'jaraco.context==5.3.0',
        'jaraco.functools==4.0.0',
        'keyring==25.1.0',
        'markdown-it-py==3.0.0',
        'mdurl==0.1.2',
        'more-itertools==10.2.0',
        'nh3==0.2.17',
        'pkginfo==1.10.0',
        'Pygments==2.17.2',
        'pywin32-ctypes==0.2.2',
        'readme_renderer==43.0',
        'requests==2.31.0',
        'requests-toolbelt==1.0.0',
        'rfc3986==2.0.0',
        'rich==13.7.1',
        'setuptools==69.2.0',
        'tqdm==4.66.2',
        'twine==5.0.0',
        'urllib3==2.2.1',
        'wheel==0.43.0',
        'zipp==3.18.1'
    ],
)
