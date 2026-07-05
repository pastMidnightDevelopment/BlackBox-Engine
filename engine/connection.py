"""
File: connection.py
Version: 0.1
Purpose: Defines directional connections between components.
"""


class Connection:
    def __init__(self, from_component, to_component, flow_type):
        self.from_component = from_component
        self.to_component = to_component
        self.flow_type = flow_type