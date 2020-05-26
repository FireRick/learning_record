from setuptools import setup, find_packages


setup(
    name='learning_record',
    version='0.0.1',
    description='Learning Record',
    packages=find_packages('learning_record'),
    package_dir={'': 'learning_record'},
    include_package_data=True,
    install_requires=[
        'Django~=2.2',
        'mysqlclient==1.4.6',
    ],
    scripts=[
        'learning_record/manage.py',
        'learning_record/learning_record/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'record_manage = manage:main',
        ]
    },
)