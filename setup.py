import setuptools
from tautulli._info import __title__, __description__, __version__, __author__, __author_email__, __license__, \
    __keywords__, __github_username__, __github_repo__, __copyright__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", 'r') as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name=__title__,
    packages=setuptools.find_packages(),
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__author_email__,
    url=f'https://github.com/{__github_username__}/{__github_repo__}',
    download_url=f'https://github.com/{__github_username__}/{__github_repo__}/archive/{__version__}.tar.gz',
    keywords=__keywords__,
    install_requires=requirements,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia',
        'Topic :: Internet :: WWW/HTTP',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7'
)
