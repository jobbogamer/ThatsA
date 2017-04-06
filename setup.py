from setuptools import setup

# Load dependencies from requirements.txt
with open('requirements.txt') as f:
    requirements = f.readlines()

# Remove comments from requirements.txt
requirements = [line.strip() for line in requirements if not line.startswith('#')]

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=requirements,
     )
