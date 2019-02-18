import pathlib
import setuptools


def read(*args):
    file_path = pathlib.Path(__file__).parent.joinpath(*args)
    with file_path.open(encoding="utf-8") as f:
        return f.read()


setuptools.setup(
    name="pytest-emoji",
    version="0.2.0",
    author="Raphael Pierzina",
    author_email="raphael@hackebrot.de",
    maintainer="Raphael Pierzina",
    maintainer_email="raphael@hackebrot.de",
    license="MIT",
    url="https://github.com/hackebrot/pytest-emoji",
    description="A pytest plugin that adds emojis to your test result report",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.4",
    install_requires=["pytest>=4.2.1"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["emoji = pytest_emoji.plugin"]},
    keywords=["pytest", "emoji"],
)
