from setuptools import setup

setup(
    name="stoppy",
    version="0.0.1",
    packages=["stoppy"],
    install_requires=["mouse", "keyboard"],
    entry_points={
        "console_scripts": ["stoppy = stoppy.__main__:main"]
    }
)