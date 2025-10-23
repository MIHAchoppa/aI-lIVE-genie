"""
Setup script for AI Live Genie (legacy support for older pip versions)
For modern installations, use pyproject.toml
"""

from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-live-genie",
    version="1.0.0",
    author="MIHAchoppa",
    description="AI-powered assistant for live streamers and content creators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MIHAchoppa/aI-lIVE-genie",
    project_urls={
        "Bug Tracker": "https://github.com/MIHAchoppa/aI-lIVE-genie/issues",
        "Documentation": "https://github.com/MIHAchoppa/aI-lIVE-genie/tree/main/docs",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "api": [
            "Flask>=2.0.0",
            "Flask-CORS>=3.0.0",
        ],
        "dev": [
            "Flask>=2.0.0",
            "Flask-CORS>=3.0.0",
            "black>=22.0.0",
            "pylint>=2.12.0",
            "mypy>=0.950",
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-live-genie=ai_live_genie.cli:main",
        ],
    },
)
