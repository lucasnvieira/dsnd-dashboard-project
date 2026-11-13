from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements_file = cwd / 'employee_events' / 'requirements.txt'
requirements = [
    line.strip()
    for line in requirements_file.read_text().splitlines()
    if line.strip()
]

setup_args = dict(
    name='employee_events',
    version='0.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'': ['employee_events.db', 'requirements.txt']},
    install_requires=requirements,
    )

if __name__ == "__main__":
    setup(**setup_args)
