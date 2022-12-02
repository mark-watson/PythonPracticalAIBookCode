# Knowledge Graph Creator command line tool: kgcreator

[![PyPI](https://img.shields.io/pypi/v/kgcreator.svg)](https://pypi.org/project/kgcreator/)
[![Changelog](https://img.shields.io/github/v/release/mark-watson/kgcreator?include_prereleases&label=changelog)](https://github.com/mark-watson/kgcreator/releases)
[![Tests](https://github.com/mark-watson/kgcreator/workflows/Test/badge.svg)](https://github.com/mark-watson/kgcreator/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/mark-watson/kgcreator/blob/master/LICENSE)

### Knowledge Graph Creator: converts text to RDF triples

The Knowledge Graph Creator (kgcreator) is a tool for automating the generation of data for Knowledge Graphs from raw text data. 

Data created by kgcreator generates data is in the format of RDF triples suitable for loading into any linked data/semantic web data store.

This example application works by identifying entities in text and then using the DBPedia SPARQL interface. Example entity types are people, companies, country names, city names, broadcast network names, political party names, and university names.

## Installation

Install this tool using `pip`:

    pip install kgcreator

## Usage

For help, run:

    kgcreator --help
    kgcreator --inputdir=test_data --outputfile=out.rdf

You can also use:

    python -m kgcreator --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd kgcreator
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
