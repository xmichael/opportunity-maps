"""Setup tools configuration file"""
from setuptools import setup, find_packages

setup(
    name="opportunity-maps",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=["jenkspy==0.1.5", "pandas >= 0.25.3", "matplotlib>=3.2.2"],
    zip_safe=True,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["natural_breaks_csv = natural_breaks_csv:main",]},
)
