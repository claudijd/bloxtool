from setuptools import setup, find_packages

setup(name='bloxtool',
      version='0.21',
      description='Tool for interfacing with InfoBlox',
      url='https://github.com/rtucker-mozilla/bloxtool',
      author='Rob Tucker',
      author_email='rtucker@mozilla.com',
      license='Mozilla Public License',
      packages = [
          'bloxtool',
      ],
      install_requires = [
            "requests",
            "docopt",
      ],
      scripts=["bin/bloxtool"],
      zip_safe=False)