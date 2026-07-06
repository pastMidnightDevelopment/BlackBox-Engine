"""
File: component_registry.py
Version: 0.1
Purpose: Loads component definitions and failure definitions for Black Box.
"""

import json
from pathlib import Path


COMPONENT_DEFINITION_FOLDER = "component_definitions"


class ComponentRegistry:
    def __init__(self):
        self.definitions = {}

    def load_definitions(self):
        definition_folder = Path(COMPONENT_DEFINITION_FOLDER)

        for definition_file in definition_folder.glob("*.json"):
            with open(definition_file, "r", encoding="utf-8") as file:
                definition_data = json.load(file)

            component_type = definition_data["type"]
            self.definitions[component_type] = definition_data

    def get_failure_definition(self, component_type, failure_type):
        component_definition = self.definitions.get(component_type)

        if component_definition is None:
            return None

        possible_failures = component_definition.get("possible_failures", {})

        return possible_failures.get(failure_type)