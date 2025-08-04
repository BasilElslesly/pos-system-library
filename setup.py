#!/usr/bin/env python3
"""
نظام نقطة البيع المتكامل - ملف الإعداد
POS System - Setup Script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pos-system",
    version="1.0.0",
    author="POS System Team",
    author_email="support@pos-system.com",
    description="نظام نقطة بيع متكامل ومتطور",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/pos-system",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: Arabic",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "analytics": [
            "numpy>=1.24.0",
            "pandas>=2.0.0",
            "matplotlib>=3.7.0",
            "scikit-learn>=1.3.0",
            "seaborn>=0.12.0",
            "plotly>=5.17.0",
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-mock>=3.12.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pos-system=simple_pos:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["templates/*", "static/*", "static/**/*"],
    },
    keywords="pos, point-of-sale, retail, inventory, sales, arabic, flask",
    project_urls={
        "Bug Reports": "https://github.com/your-username/pos-system/issues",
        "Source": "https://github.com/your-username/pos-system",
        "Documentation": "https://github.com/your-username/pos-system/blob/main/README_COMPLETE.md",
    },
)
