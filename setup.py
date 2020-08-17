import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='pymarkdown-video',
    version='1.0.0',
    description='Render video tags in python markdown for images that are video',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Olivier Robardet',
    author_email='orobardet@gmail.com',
    keywords="markdown image video",
    license='MIT',
    url='https://github.com/orobardet/pymarkdown-video',
    py_modules=['pymarkdown-video'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['markdown>=3.0'],
    python_requires='>=3',
)