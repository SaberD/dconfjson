import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Topic :: Gnome :: Linux :: Ubuntu :: Config :: Json',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
    'Topic :: Utilities']

setuptools.setup(
    name="dconfjson",
    version="0.1.0",
    python_requires='>=3.*',
    author="saberd",
    author_email="mail@saberd.com",
    description="Convert gnome settings between binary conf files and json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saberd/dconfjson",
    packages=setuptools.find_packages(),
    py_modules=['dconfjson'],
    install_requires=[
    ],
    classifiers=classifiers,
    entry_points={
        'console_scripts': [
            'dconfjson=dconfjson.main:main', # need to add export import functions to/from json
        ],
    },
)