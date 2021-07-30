from setuptools import setup  # type: ignore


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='ytrssil',
    description=(
        'Subscribe to YouTube RSS feeds and keep track of watched videos'
    ),
    homepage='https://gitea.theedgeofrage.com/TheEdgeOfRage/ytrssil',
    repository='https://gitea.theedgeofrage.com/TheEdgeOfRage/ytrssil',
    documentation='https://gitea.theedgeofrage.com/TheEdgeOfRage/ytrssil',
    version='0.0.0',
    packages=['ytrssil'],
    package_data={'': ['py.typed']},
    include_package_data=True,
    install_requires=required,
    entry_points={
        'console_scripts': [
            'ytrssil = ytrssil.cli:main',
        ],
    },
)
