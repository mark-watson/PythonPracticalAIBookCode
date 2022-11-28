# kg-creator

[![PyPI](https://img.shields.io/pypi/v/kg-creator.svg)](https://pypi.org/project/kg-creator/)
[![Changelog](https://img.shields.io/github/v/release/mark-watson/kg-creator?include_prereleases&label=changelog)](https://github.com/mark-watson/kg-creator/releases)
[![Tests](https://github.com/mark-watson/kg-creator/workflows/Test/badge.svg)](https://github.com/mark-watson/kg-creator/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/mark-watson/kg-creator/blob/master/LICENSE)

Knowledge Graph Creator: converts text to RDF triples

## Installation

Install this tool using `pip`:

    pip install kg-creator

## Usage

For help, run:

    kg-creator --help
    kg-creator --inputdir=test_data --outputfile=out.rdf

You can also use:

    python -m kgcreator --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd kg-creator
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
