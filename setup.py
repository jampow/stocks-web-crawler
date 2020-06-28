from setuptools import setup

setup(name='stocks',
      version='0.1',
      description='stocks web crawler',
      url='http://github.com/jampow/stocks-web-crawler',
      author='Gianpaulo M. Soares',
      author_email='jam_pow@hotmail.com',
      license='MIT',
      packages=['brdt3ri'],
      install_requires=[
          'requests',
          'BeautifulSoup',
          'tabulate',
          'colored'
      ],
      zip_safe=False)
