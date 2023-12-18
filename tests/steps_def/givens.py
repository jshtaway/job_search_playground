import os
import importlib
from pytest_bdd import given, parsers
import pages
from tools.convert import to_camel_case
from tools import file_ops


@given(parsers.parse('I navigate to "{page}"'))
def navigate_to(driver, current_page, page):
    page = to_camel_case(page)
    module = importlib.import_module(f"pages.{page}")
    my_page = getattr(module, page[0].upper() + page[1:])(driver)
    url = my_page.url
    driver.get(url)
    current_page['page'] = my_page

@given(parsers.parse('I load "{file_name}"'))
def load_data(test_data, file_name):
    path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data"
    )
    test_data[file_name.split("/")[-1].split(".")[0]] = file_ops.load_csv(
        os.path.join(path, file_name)
    )
