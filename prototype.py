# AI-based Robotic Dog Prototype (Initial Stage)

class RoboDog:
    def __init__(self, name):
        self.name = name

    def detect_motion(self):
        return "Motion detected"

    def respond(self):
        return f"{self.name} is responding to the environment"

# Simulating basic behavior
robodog = RoboDog("AI RoboDog")
print(robodog.detect_motion())
print(robodog.respond())
