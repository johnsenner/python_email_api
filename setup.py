from setuptools import setup, find_packages

setup(
    name='email_service',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'email_service=email_service.__main__:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
