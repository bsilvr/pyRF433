
from distutils.core import setup, find_packages

setup(
    name='RF433',
    packages=find_packages(),
    version='0.1.2',
    description='RF433 library to send signals for various protocols using \
                    an arduino',
    author='Bruno Silva',
    author_email='brunomiguelsilva@ua.pt',
    url='https://github.com/bsilvr/pyRF433',
    download_url='https://github.com/bsilvr/pyRF433/tarball/0.1.2',
    keywords=['rf433', 'arduino'],
    classifiers=[],
)

install_requires = [
   'pyserial==3.1.1'
]
