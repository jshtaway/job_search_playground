from pytest_bdd import scenario
from tools import convert
import os
from tests.steps_def.givens import navigate_to

# -- import all steps --
steps_def = os.path.join(os.path.dirname(__file__),"steps_def")
for module in os.listdir(steps_def):
    if module == "__init__.py" or module[-3:] != ".py":
        continue
    exec(f"from tests.steps_def.{module[:-3]} import *")


@scenario('features/interviewJson.feature', 'Number of entries in input matches output_stops')
def test_jsons(test_data):
  test_data.current_scenario = 'Do stuff with JSONs'
  pass

@scenario('features/interviewJson.feature', 'Output_order should have one unique entry per input Output_order')
def test_jsons2(test_data):
  pass