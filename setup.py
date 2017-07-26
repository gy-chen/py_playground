from setuptools import setup, find_packages

setup(
    name='py_playground',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=['flask'],
    entry_points={
        'console_scripts': {
            'scope_demo=py_playground.flask.scope_demo:run'
        }
    }
)