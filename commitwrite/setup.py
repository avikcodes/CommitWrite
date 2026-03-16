from setuptools import setup


setup(
    name="commitwrite",
    version="1.0.0",
    install_requires=["groq", "python-dotenv"],
    py_modules=["commitwrite"],
    entry_points={
        "console_scripts": [
            "commitwrite=commitwrite:main",
        ],
    },
)
