import setuptools
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

_version_ = "0.0.1"

REPO_NAME = "Document-Summarizer"
AUTHOR_USER_NAME = "Pranay Nalla"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "pranay6243@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for an end-to-end text summarization pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "transformers",
        "transformers[sentencepiece]",
        "datasets",
        "sacrebleu",
        "rouge_score",
        "py7zr",
        "pandas",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "torch",
        "boto3",
        "python-box==6.0.2",
        "ensure==1.0.2"
    ],
    python_requires=">=3.8",
)



# import setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()


# _version_ = "0.0.0"

# REPO_NAME = "Document-Summarizer"
# AUTHOR_USER_NAME = "Pranay Nalla"
# SRC_REPO = "TextSummarizer"
# AUTHOR_EMAIL = "pranay6243@gmail.com"



# setuptools.setup(
#     name=SRC_REPO,
#     version=_version_,
#     author=AUTHOR_USER_NAME,
#     author_email=AUTHOR_EMAIL,
#     description="A small python package for NLP app",
#     long_description=long_description,
#     long_description_content="text/markdown",
#     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     project_urls={
#         "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
#     },
#     package_dir={"": "src"},
#     packages=setuptools.find_packages(where="src")
# )