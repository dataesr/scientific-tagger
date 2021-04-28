from setuptools import find_packages, setup
from project import __version__

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
    name='scientific-tagger',
    version=__version__,
    description='Tagger for scholarly publications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dataesr/scientific_tagger',
    license='MIT',
    author='Eric Jeangirard, Anne L\'Hôte',
    keywords=['research', 'tagging', 'publication', 'domain'],
    python_requires='>=3.6',
    packages=find_packages(),
    install_requires=[
        'fasttext==0.9.2',
        'Flask==1.1.1',
        'Flask-Bootstrap==3.3.7.1',
        'Flask-Testing==0.7.1',
        'Flask-WTF==0.14.2',
        'gunicorn==20.0.4',
        'pandas==0.25.3',
        'python-keystoneclient==4.0.0',
        'python-swiftclient==3.9.0',
        'redis==3.3.11',
        'regex==2017.4.5',
        'requests==2.20.0',
        'rq==1.1.0',
        'sklearn==0.0',
        'tokenizers==0.10.1',
        'Unidecode==1.0.22',
        'xlrd==1.1.0',
        'XlsxWriter==1.0.4'
    ],
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    zip_safe=True
)
