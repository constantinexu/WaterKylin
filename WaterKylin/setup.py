# setup.py is not finished
from setuptools import setup, find_packages

setup(
    name='waterkylin',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'networkx>=2.4'
    ],
    author='Shipeng',
    author_email='924225024@qq.com',
    description='A library for analyzing the periphery of complex networks',
    long_description=open('README.md').read(),
 
    url='https://github.com/constantinexu/waterkylin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='complex network',
    license='MIT',
    test_suite='tests',
    project_urls={
        'Documentation': 'https://github.com/constantinexu/waterkylin',
        'Source': 'https://github.com/constantinexu/waterkylin',
        'Tracker': 'https://github.com/constantinexu/waterkylin/issues',
    },
)
