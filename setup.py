from setuptools import setup

setup(
    name='shelpy',
    version='0.0.1',
    packages=['shelpy'],
    entry_points={
        'console_scripts': [
            'shelpy-hi = shelpy.shelpy:hello_world',
            'range = shelpy.shelpy:_range',
            'map = shelpy.shelpy:_map',
            'filter = shelpy.shelpy:_filter',
        ]
    }
)
