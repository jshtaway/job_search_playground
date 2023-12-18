import os
import importlib
from pytest_bdd import then, parsers
from tools.convert import to_camel_case


@then("Some result is expected")
def some_expectation(test_data):
    # breakpoint()
    pass

@then("Number of entries should match")
def do_stuff(test_data):
    assert (len(test_data["input"]) == len(test_data["output_stop"]))
    breakpoint()

@then("Output twm is unique and has one per input tmw")
def do_stuff(test_data):
    output_tmw_ids = [item['tmw_id'] for item in test_data['output_order']]
    assert (
        len([item['tmw_id'] for item in test_data['output_order']])
        == len({item['tmw_id'] for item in test_data['output_order']})
    )
    
    input_tmw_ids = {item['tripHdrNumber'] for item in test_data['input']}
    assert len(input_tmw_ids) == len(output_tmw_ids)
