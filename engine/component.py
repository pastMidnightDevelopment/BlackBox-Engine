"""
File: component.py
Version: 0.1
Purpose: Defines the basic component model for Black Box.
"""


class Component:
    def __init__(self, component_id, name, component_type):
        self.component_id = component_id
        self.name = name
        self.component_type = component_type
        self.powered = False
        self.failed = False

    def inspect(self):
        return {
            "id": self.component_id,
            "name": self.name,
            "type": self.component_type,
            "powered": self.powered,
            "failed": self.failed,
        }