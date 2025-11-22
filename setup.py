from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()


long_description = (here / "README.md").read_text(encoding="utf-8")


install_requires = []


dev_requires = [
    "setuptools==80.9.0"
]


extras_require = {
    "dev": dev_requires
}


console_scripts = [
    "pf=cli:main",
]


entry_points={
    "console_scripts": console_scripts,
}


setup_options = dict(
    name="personalfinance",
    version="0.1.0",
    description="Tools to manage your personal finances",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juan-sicardo/personal-finance",
    author="Juan Sicardo",
    author_email="contacto@juansicardo.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points=entry_points,
)


setup(**setup_options)
