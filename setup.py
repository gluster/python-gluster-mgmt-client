
from setuptools import setup, find_packages

setup(
    name='glusterapi-python',
    version='0.1',
    description='Python client library for GlusterD2',
    license='GPLv3+',
    author='Gluster Developers',
    author_email='gluster-devel@gluster.org',
    url='https://github.com/gluster/glusterapi-python',
    packages=find_packages(exclude=['test', 'bin']),
)
