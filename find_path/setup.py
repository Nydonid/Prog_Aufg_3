from setuptools import setup

# notwendig, damit Programm aus Terminal ladbar ist.
setup(
    name='find_path',
    version='1.0',
    py_modules=['main', 'Graph', 'Edge', 'Node', 'myParser'],
    packages=['find_path'],
    entry_points={
        'console_scripts': [
            'find_path = main:main',
        ],
    },
)

