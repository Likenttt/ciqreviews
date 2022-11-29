from setuptools import setup, find_packages

VERSION = '0.1.6'
DESCRIPTION = 'This package is used to analyse the downloads,reviews,ratings of some Garmin Connect IQ App'
LONG_DESCRIPTION = 'Using Beautifulsoup4 to find the download and reviews statistics of some app'

# 配置
setup(
    name="ciqreviews",
    version=VERSION,
    author="li2niu",
    author_email="<chuanyi.work@gmail.com>",
    url='https://github.com/Likenttt/ciqreviews',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['connectiq', 'garmin', 'ciq'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
