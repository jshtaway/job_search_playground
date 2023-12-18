import os
import pytest
from pytest_bdd import given
from selenium import webdriver
from tools import convert, visualization, file_ops
import plotly.express as px
import plotly.io as io

current_test = convert.MyCoolDict({})
repo_path = os.path.join(
    os.path.dirname(__file__),
    ".."
)

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    global current_test
    current_test.feature = scenario.feature.name
    current_test.scenario = scenario.name
    current_test.step = step.name

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')

# Fixtures
@pytest.fixture(autouse = False, scope = "session")
def driver():
    # A better practice would be to get browser choice from a config file.
    b = webdriver.Chrome()
    b.implicitly_wait(2)
    yield b
    b.quit()

@pytest.fixture(scope="function")
def test_data():
    return convert.MyCoolDict({
        'data_path': os.path.join(repo_path, 'tests', 'data')
    })

@pytest.fixture(autouse=True, scope="function")
def grapher():
    grapher = visualization.Grapher(False)
    yield grapher
    for _, graph in grapher.graphs.items():
        io.write_json(
            graph,
            os.path.join(repo_path, 'reports', f"{convert.to_camel_case(current_test.scenario)}.json"),
            pretty=True,
            engine='orjson'
        )

    

# --- REPORTS -- -- --- -- -- --- -- --- -- --- --- --- --

pytest.hookimpl(tryfirst=True)  # run our hookimpl before pytest-html does its own postprocessing
def pytest_sessionfinish(session):
    pass