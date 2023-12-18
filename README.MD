Follow these steps to set up the project:

1. Create and activate a virtual environment named "myenv" by running the following commands in your terminal:

    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

2. Install the project dependencies from the requirements.txt file by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the required packages specified in the requirements.txt file.

3. You are now ready to run the project and execute the pytest tests.

## Getting Started with pytest

To get started with pytest, follow these steps:

1. Open a terminal.
2. Navigate to the root directory of your project.
3. Run the following command to execute your pytest tests and generate a cucumber report:

    ```bash
    python3 -m pytest --cucumberjson=reports/report.json
        ```
4. To run a specific test, you can use the `-k` option followed by the name of the test. For example, to run a test named `test_jsons`, you can use the following command:

        ```bash
        python3 -m pytest --cucumberjson=reports/report.json -k test_jsons
        ```

        This command will execute only the `test_jsons` test and generate a cucumber report json.

5. You can now view the test report by running Dash in `dash/pytest_reporter.py`. Open a terminal, navigate to the root directory of your project, and run the following command:

        ```bash
        python3 dash/pytest_reporter.py
        ```

        This command will start a Dash server and display the test report in a web browser.

That's it! You have now successfully executed your pytest tests and generated an HTML report.

## Locust Performance Testing
# Locust is a popular open-source load testing tool written in Python. It allows you to define user behavior using Python code and simulate thousands of concurrent users to test the performance of your application.

# To run locust performance testing, follow these steps:
# 2. Create a locust file in locust directory (e.g., locust_file.py) and define your user behavior using locust's API.
# 3. Open a terminal or command prompt and navigate to project directory
# 4. Run the locust command with the -f flag followed by the path to your locust file:
#    `locust -f locust_file.py`
# 5. Open a web browser and go to http://localhost:8089 to access the Locust web interface.
# 6. Enter the desired number of users and the hatch rate, and then click the "Start swarming" button to start the test.
# 7. Monitor the test progress and results in the Locust web interface.
# 8. After the test is complete, you can analyze the results and identify any performance bottlenecks or issues.

# Your code goes here
## Setting Up the Project


