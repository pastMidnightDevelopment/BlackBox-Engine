"""
File: flow_engine.py
Version: 0.1
Purpose: Simulates simple directional electrical flow through components.
"""


class FlowEngine:
    def __init__(self, system):
        self.system = system

    def reset_power(self):
        for component in self.system.components.values():
            component.powered = False

    def simulate_electrical_flow(self, source_id):
        self.reset_power()

        source = self.system.get_component(source_id)

        if source is None:
            return

        source.powered = True
        self._propagate_power(source.component_id)

    def _propagate_power(self, component_id):
        for connection in self.system.connections:
            if connection.from_component != component_id:
                continue

            if connection.flow_type != "electrical":
                continue

            next_component = self.system.get_component(connection.to_component)

            if next_component is None:
                continue

            if next_component.powered:
                continue

            next_component.powered = True

            if next_component.failure_effect == "blocks_flow":
                continue

            self._propagate_power(next_component.component_id)