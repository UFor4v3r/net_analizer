from setuptools import setup, find_packages

setup(
    name="net_analizer",
    version="1.0.0",
    description="Advanced Packet Sniffer & Network Analysis Framework by V01D",
    author="V01D",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "scapy",
    ],
    entry_points={
        "console_scripts": [
            "net_analizer=main:main",
        ],
    },
    python_requires=">=3.7",
)

