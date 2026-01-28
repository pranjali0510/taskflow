from setuptools import setup, find_packages


setup(
    name="taskflow-cli",
    version="1.0.0",
    description="CLI-based Task Management System",
    author="Pranjali Sharma",
    packages=find_packages(),
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "taskflow=cli:main"
        ]
    },
    install_requires=[],
)
