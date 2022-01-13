import sys, os
from setuptools import setup

dependencies = ['Pillow', 'numpy']

if os.path.exists('/sys/bus/platform/drivers/gpiomem-bcm2835'):
    dependencies += ['RPi.GPIO', 'spidev']
else:
    dependencies += ['Jetson.GPIO']

setup(
    name='waveshare-epd',
    description='Waveshare e-Paper Display',
    author='Waveshare',
    package_dir={'': 'lib'},
    packages=['waveshare_epd'],
    download_url = 'https://github.com/LeoinChina/waveshare_epd/archive/refs/tags/v1.0.0.tar.gz',
    install_requires=dependencies,
)

