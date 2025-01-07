from setuptools import setup, find_packages

setup(
    name="coding-agent",
    version="0.1.0",
    author="Harshit",
    description="A coding AI agent with deep thinking ability using open source LLM such as Qwen.",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "numpy",
        "pandas",
        "scikit-learn"
    ],
    entry_points={
        "console_scripts": [
            "coding-agent=src.agent:main",
        ],
    },
)
