import os
from pytest_bdd import when, parsers
import pages
import pandas as pd
from tools.convert import to_camel_case
from tools import file_ops, parser
import random

@when("I do things")
def do_stuff(test_data):
    pass
    breakpoint()

@when("I parse an example cucumber report to csv")
def parse_example_report(test_data):
    report = file_ops.load_json(
        os.path.join(test_data.data_path, 'report.json')
    )
    my_parser = parser.Parser()
    df = my_parser.parse_cucumber_report(report, pd.DataFrame)
    file_ops.write_csv(df, os.path.join(test_data.data_path, 'out.csv'))


@when(parsers.parse('I search for "{search}" in location "{location}"'))
def search_zr(driver, current_page, search, location):
    current_page['page'].search(search, location)


@when("Make a test graph")
def make_test_graph(test_data, grapher):
    grapher.line(
        ['a', 'b', 'c', 'd', 'e', 'f'],
        [random.randint(1,10) for i in range(6)],
        "My Graph", "make_test_graph"
    )
