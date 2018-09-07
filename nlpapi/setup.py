
import setuptools

setuptools.setup(
    name='nlpapi',
    version='0.0.1',
    author='Shaun O',
    author_email='shaun@codescratch.com',
    packages=['nlpapi', 'nlpapi.spacy'],
    url='http://nowhere/pypi/nlpapi/',
    license='N/A',
    description='Generated thrift code for an NLP wrapper.',
    long_description=open('README.md').read(),
    install_requires=[
        "thrift == 0.11.0",
    ],
)
