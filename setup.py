from pathlib import Path

from setuptools import setup

root = Path(__file__).parent
long_description = (root / "README.md").read_text()

setup(
    name="modulinedtc",
    version="0.0.1",
    description="A script to format Fault codes for the Moduline Web UI",
    url="https://github.com/GOcontroll/Moduline-WebUI",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GOcontroll",
    author_email="info@gocontroll.com",
    maintainer="Maud Spierings",
    packages=["modulinedtc"],
    entry_points={
        "console_scripts": [
            "go-print-dtcs = modulinedtc.errors:print_errors",
        ]
    },
)
