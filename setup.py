from setuptools import setup, find_packages

setup(
    name='pyLog',
    version='0.1.0',
    author='Mainframe Matrix',
    author_email='mainframematrix01@gmail.com',
    description='A Simple Python Logging Framework.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mainframematrix/Python-Logger',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
