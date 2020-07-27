from setuptools import setup

setup(
    name='url_short',
    packages=['url_short'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-sqlalchemy',
    ],
)