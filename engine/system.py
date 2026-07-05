"""
File: system.py
Version: 0.1
Purpose: Holds components and connections for a loaded system.
"""


class System:
    def __init__(self):
        self.components = {}
        self.connections = []

    def add_component(self, component):
        self.components[component.component_id] = component

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_component(self, component_id):
        return self.components.get(component_id)

    def inspect_all(self):
        return [
            component.inspect()
            for component in self.components.values()
        ]