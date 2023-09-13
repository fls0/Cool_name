import setuptools
from setuptools import setup

setup(
    name='Personal_assistant',
    version='0.0.1',
    description='Group-12 team project',
    authors='PythonWizards',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'dateparser==1.0.0',
        'prompt_toolkit==3.0.21',
        'folium==0.12.1',
        'requests==2.26.0',
        'pygame==2.0.1',
        'colorama==0.4.4',
        'dill>=0.3.7'
        ],
    entry_points={'console_scripts': ['personal-assistant = Personal_assistant.main:menu']}
)
