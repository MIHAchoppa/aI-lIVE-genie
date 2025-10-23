from setuptools import setup, find_packages

setup(
    name="ai-live-genie",
    version="0.1.0",
    description="Master set of AI fine-tuned Groq models for live streaming platforms with strategy and host training bot",
    author="MIHAchoppa",
    packages=find_packages(),
    install_requires=[
        "groq>=0.4.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "pyyaml>=6.0",
        "asyncio>=3.4.3",
        "aiohttp>=3.9.0",
        "websockets>=12.0",
    ],
    python_requires=">=3.8",
)
