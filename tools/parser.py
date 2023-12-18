from datetime import datetime
import pandas as pd
import os
from tools import file_ops

class Parser:
    def __init__(self) -> None:
        self.my_list = file_ops.load_json(
            "/Users/jennifershtaway/Projects/JobSearchAutomation/tests/data/baton.json"
        )

    def parse_cucumber_report(self, report, output_type = list):
        if isinstance(report, str) and os.path.exists(report):
            report = file_ops.load_json(report)
        if output_type == pd.DataFrame:
            df = pd.DataFrame.from_dict({
                (feature['name'], scenario['name']): {
                    "status": (
                        "pass" if all([step['result']['status'] == 'passed' for step in scenario['steps']])
                        else "fail"
                    ),
                    "duration": sum([step['result']['duration'] for step in scenario['steps']])
                }
                for feature in report
                for scenario in feature['elements']
            }, orient="index")
            df = df.reset_index(names=['feature', 'scenario'])
            return df
        elif output_type == list:
            tests = []
            for feature in report:
                for scenario in feature['elements']:
                    status = all([
                        step['result']['status'] == 'passed'
                        for step in scenario['steps']
                    ])
                    duration = sum([
                        step['result']['duration']
                        for step in scenario['steps']
                    ])
                    tests.append({
                        'Feature': feature['name'],
                        'Scenario': scenario['name'],
                        'Status': status,
                        'Duration': duration
                    })
            return tests
        
    def convert_to_datetime(self, my_list):
        my_list = [
            self.make_date_object(entry)
            for entry in my_list
        ]
        return my_list
    
    def filter_by_date_facility(self, date, facility):
        my_list = self.convert_to_datetime(self.my_list)
        return [
            entry
            for entry in self.my_list
            if (
                entry['entrance_time'].date() <= date
                and (entry['exit_time'] == None or entry['exit_time'].date() >= date)
                and entry['facility_id'] == facility
            )
        ]


    def make_date_object(self, entry):
        entry['entrance_time'] = datetime.fromisoformat(entry['entrance_time'])
        entry['exit_time'] = (
            datetime.fromisoformat(entry['exit_time'])
            if entry['exit_time'] is not None else None
        )
        return entry
    
    def max_occupancy(self, date, facility):
        my_list = self.filter_by_date_facility(date, facility)
        in_sorted = sorted(my_list, key = lambda entry: entry['entrance_time'])
        with_out = [entry for entry in my_list if entry['exit_time'] != None]
        out_sorted = sorted(with_out, key = lambda entry: entry['exit_time'])
        counter = [0]
        pointer = 0
        for i, in_trailer in enumerate(in_sorted):
            for j, out_trailer in enumerate(out_sorted[pointer:], pointer):
                if (
                    out_trailer['exit_time'] <= in_trailer['entrance_time']
                    and out_trailer['exit_time'] > in_sorted[i-1]['entrance_time']
                ):
                    pointer = j
                    counter.append(counter[-1]-1)
                else:
                    # avoid extra loop time w/ break once dates don't match
                    break
            counter.append(counter[-1]+1)
        print(max(counter))


if __name__ == "__main__":
    my_parser = Parser()
    date = datetime(year=2022, month=1, day=18).date()
    my_parser.max_occupancy(date, 1)