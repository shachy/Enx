from distutils.core import setup

setup(
  name = 'Ord',         # How you named your package folder (MyLib)
  packages = ['Ord'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package to help me and maybe other people use more efficient lists',   # Give a short description about your library
  author = 'shachy',                   # Type in your name
  author_email = 'shachar262@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/shachy/Vec',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/shachy/Ord/archive/0.1.zip',    # I explain this later on
  keywords = ['list', 'vector', 'order'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'random',

      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
