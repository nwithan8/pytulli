import setuptools

from tautulli import (
    __title__,
    __version__,
    __license__,
    __description__,
    __author__,
    __author_email__,
    __github_username__,
    __github_repo__,
    __keywords__
)

with open("README.md", "r") as fh:
    long_description = fh.read()


def python_versions():
    """Return a list of supported Python versions."""
    with open("tautulli/PYTHON_VERSIONS") as f:
        versions = f.read().splitlines()
    version_strings = ['Programming Language :: Python :: 3']
    for version in versions:
        version_strings.append(f"Programming Language :: Python :: {version}")
    return version_strings


def python3_range():
    """Return a string of the supported Python version range."""
    with open("tautulli/PYTHON_VERSIONS") as f:
        versions = f.read().splitlines()
    return f">={versions[0]}, <4"


REQUIREMENTS = [
    "objectrest==2.0.*",
    "pydantic==1.10.*",
    "pytz==2022.1.*",
    "python-dotenv==0.20.*",
    "packaging==21.3.*",
    "typing-extensions"
]

DEV_REQUIREMENTS = [
    "black",
    "flake8",
    "isort",
    "pytest-cov==3.*",
    "pytest-vcr==1.*",
    "pytest==7.*",
    "types-requests",
    "types-urllib3",
    "vcrpy==4.*",
]

classifiers = [
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Development Status :: 4 - Beta',
    # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',  # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Topic :: Multimedia :: Video',
    'Topic :: Multimedia',
    'Topic :: Internet :: WWW/HTTP',
    'Operating System :: OS Independent'
]
classifiers.extend(python_versions())

setuptools.setup(
    name=__title__,
    packages=setuptools.find_packages(exclude=["tests"]),
    include_package_data=True,
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__author_email__,
    url=f'https://github.com/{__github_username__}/{__github_repo__}',
    download_url=f'https://github.com/{__github_username__}/{__github_repo__}/archive/refs/tags/{__version__}.tar.gz',
    keywords=__keywords__,
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    test_suite="test",
    classifiers=classifiers,
    python_requires=python3_range(),
)
