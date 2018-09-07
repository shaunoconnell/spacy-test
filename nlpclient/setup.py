from distutils.core import setup


setup(
    name='nlpclient',
    version='0.0.1',
    author='Shaun O',
    author_email='shaun@codescratch.com',
    # packages=['towelstuff', 'towelstuff.test'],
    # scripts=['bin/stowe-towels.py', 'bin/wash-towels.py'],
    url='http://nowhere/pypi/nlpapi/',
    license='N/A',
    description='Useful towel-related stuff.',
    long_description=open('README.md').read(),
    install_requires=[
        "nlpapi",
    ],
)
