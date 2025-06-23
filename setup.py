from setuptools import setup, find_packages

setup(
    name="ml_ia_journey",
    version="0.1.0",
    description="Jornada de aprendizado em Python, ML e IA",
    author="joaohgp-dev",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest",
        "flake8",
        "pyyaml",
        "black",
        "pre-commit",
    ],
)
# For future implementations:
# "jupyter",
# "pandas",
# "numpy",
# "scikit-learn",
# "matplotlib",
# "seaborn"
