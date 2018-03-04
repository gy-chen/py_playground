from setuptools import setup, find_packages

setup(
    name='py_playground',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'flask',
        'matplotlib',
        'numpy',
        'faker',
        'websockets',
        'opencv-python',
        'pynput',
        'pyaudio',
        'google-cloud-speech',
        'google-cloud-vision',
        'tornado',
        'pykka',
        'python-socketio'
    ],
    scripts=['src/py_playground/flask/bin/play_socketio'],
    entry_points={
        'console_scripts': {
            'scope_demo=py_playground.flask.scope_demo:run',
            'simple_wsgi=py_playground.web.simple_wsgi:start_simple_wsgi'
        }
    }
)
