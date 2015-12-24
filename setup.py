from setuptools import setup, find_packages

setup(
    name = 'pbbridgemapper',
    version = '0.4',
    author = 'Pacific Biosciences',
    author_email = 'devnet@pacificbiosciences.com',
    license = open('LICENSE.txt').read(),
    packages = find_packages('.'),
    package_dir = {'':'.'},
    zip_safe = False,
    entry_points = dict(console_scripts=[
        'pbbridgemapper = pbbridgemapper.main:main'
    ]),
    install_requires = [
        'pbcore >= 0.6.0'
    ]
)
