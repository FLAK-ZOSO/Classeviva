import setuptools
setuptools.setup(
    name='classevivaAPI',
    packages=['classevivaAPI'],
    package_dir={'': 'src'},
    version='0.0.7',
    description='Classeviva Python API',
    author='FLAK-ZOSO',
    author_email='mattia.marchese.2006@gmail.com',
    url='https://github.com/Lioydiano/Classeviva',
    download_url='https://github.com/Lioydiano/Classeviva/archive/refs/tags/v0.0.7.tar.gz',
    keywords=['classeviva', 'school', 'api'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.10",
    packages=setuptools.find_packages(where="src")
)