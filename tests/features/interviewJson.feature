Feature: JSONS

Background: Load JSON
    Given I load "input.csv"
    And I load "output_stop.csv"
    And I load "output_order.csv"

    Examples:
        | file_name |
        | input.csv |
        | output.csv |

Scenario: Number of entries in input matches output_stops
    Then Number of entries should match

Scenario: Output_order should have one unique entry per input Output_order
    Then Output twm is unique and has one per input tmw