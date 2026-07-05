"""
File: main.py
Version: 0.1
Purpose: Loads a simple Black Box case and runs the first flow simulation.
"""

import json

from engine.component import Component
from engine.connection import Connection
from engine.system import System
from engine.flow_engine import FlowEngine


CASE_FILE_PATH = "cases/simple_motor.json"
SOURCE_COMPONENT_ID = "battery"


def load_case(file_path):
    with open(file_path, "r", encoding="utf-8") as case_file:
        case_data = json.load(case_file)

    system = System()

    for component_data in case_data["components"]:
        component = Component(
            component_id=component_data["id"],
            name=component_data["name"],
            component_type=component_data["type"],
        )
        system.add_component(component)

    for failure_data in case_data.get("failures", []):
        component = system.get_component(failure_data["component_id"])

        if component is not None:
            component.failed = True
            component.failure_type = failure_data.get("failure_type")
            component.failure_effect = failure_data.get("failure_effect")

    for connection_data in case_data["connections"]:
        connection = Connection(
            from_component=connection_data["from"],
            to_component=connection_data["to"],
            flow_type=connection_data["flow_type"],
        )
        system.add_connection(connection)

    return system


def print_inspection_results(system):
    print("\nInspection Results")
    print("------------------")

    for component_state in system.inspect_all():
        print(component_state)


def main():
    system = load_case(CASE_FILE_PATH)

    flow_engine = FlowEngine(system)
    flow_engine.simulate_electrical_flow(SOURCE_COMPONENT_ID)

    print_inspection_results(system)


if __name__ == "__main__":
    main()