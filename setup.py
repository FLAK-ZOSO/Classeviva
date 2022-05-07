import setuptools
setuptools.setup(
    name='classevivaAPI',
    packages=['classeviva'],
    package_dir={'': 'src'},
    version='0.2.0.dev3',
    requires=["selenium"],
    description='Classeviva Python API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='FLAK-ZOSO',
    author_email='mattia.marchese.2006@gmail.com',
    url='https://github.com/Lioydiano/Classeviva',
    download_url='https://github.com/Lioydiano/Classeviva/archive/refs/tags/v0.2.0-dev.3.tar.gz',
    keywords=['classeviva', 'school', 'api'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: Italian",
        "Natural Language :: English",
        "Typing :: Typed"
    ],
    python_requires=">=3.10"
)