"""
File: component.py
Version: 0.3
Purpose: Defines the basic component model and behavior for Black Box.
"""


class Component:
    def __init__(self, component_id, name, component_type):
        self.component_id = component_id
        self.name = name
        self.component_type = component_type

        self.powered = False
        self.failed = False
        self.running = False

        self.internal_state = {}
        self.observable_state = []

    def update_behavior(self):
        if self.component_type == "motor":
            self.running = self.powered and not self.failed
        else:
            self.running = False

    def update_observable_state(self):
        self.observable_state = []

        if self.component_type == "power_source":
            if self.powered:
                self.observable_state.append("Supplying electrical power.")
            else:
                self.observable_state.append("Not supplying electrical power.")

        elif self.component_type == "fuse":
            if self.powered and self.failed:
                self.observable_state.append(
                    "Electrical power reaches the fuse, but the fuse has failed and blocks downstream flow."
                )
            elif self.powered:
                self.observable_state.append("Electrical power passes through the fuse.")
            else:
                self.observable_state.append("No electrical power is reaching the fuse.")

        elif self.component_type == "switch":
            if self.powered:
                self.observable_state.append("Electrical power is reaching the switch.")
            else:
                self.observable_state.append("No electrical power is reaching the switch.")

        elif self.component_type == "motor":
            if self.running:
                self.observable_state.append("Motor is running.")
            elif self.powered and self.failed:
                self.observable_state.append(
                    "Electrical power reaches the motor, but the motor has failed and does not run."
                )
            elif self.powered:
                self.observable_state.append(
                    "Electrical power reaches the motor, but the motor is not running."
                )
            else:
                self.observable_state.append(
                    "Motor is stopped because no electrical power is reaching it."
                )

        else:
            self.observable_state.append("No observable information available.")

    def inspect(self):
        self.update_behavior()
        self.update_observable_state()

        return {
            "id": self.component_id,
            "name": self.name,
            "type": self.component_type,
            "powered": self.powered,
            "failed": self.failed,
            "running": self.running,
            "observable_state": self.observable_state,
        }