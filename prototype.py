import time
import random


class SentinelDog:
    def __init__(self):
        self.running = True
        print("SentinelDog Prototype Initialized")
        print("Monitoring environment...\n")

    def read_environment(self):
        """Simulate sensor input."""
        return random.choice([
            "normal activity",
            "movement detected",
            "sound detected",
            "silence detected"
        ])

    def analyze_event(self, event):
        """Decision-making logic."""
        if event == "silence detected":
            self.trigger_alert()
        else:
            print(f"Environment status: {event}")

    def trigger_alert(self):
        """Alert mechanism."""
        print("⚠ ALERT: Possible abnormal absence or silence detected!")

    def start_monitoring(self):
        """Main monitoring loop."""
        while self.running:
            event = self.read_environment()
            self.analyze_event(event)
            time.sleep(3)


if __name__ == "__main__":
    robot = SentinelDog()
    robot.start_monitoring()
