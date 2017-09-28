from setuptools import setup

setup(name='ani_scraper',
      version='0.0.1',
      packages=['ani_scraper'],
      install_requires=['beautifulsoup4>=4.6', 'requests>=2.18'],
      entry_points={
          'console_scripts': ['ani_scraper = ani_scraper.__main__:main']
      }
     )
