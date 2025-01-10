from setuptools import setup, find_packages

setup(
    name="OpenSpy",
    version="0.1.0",
    author="Clyde",
    author_email="clyde@dreamsurvival.fun",
    description="OpenSpy - Un outil OSINT multifonctionnel en Python",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clydedc/OpenSpy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "requests",
        "beautifulsoup4",
        "stem"
    ],
    entry_points={
        'console_scripts': [
            'openspy=openspy:main',
        ],
    },
    keywords="OSINT, reconnaissance, dark web, google search, phone lookup",
    project_urls={
        "Bug Tracker": "https://github.com/clydedc/OpenSpy/issues",
        "Source Code": "https://github.com/clydedc/OpenSpy",
    },
)
