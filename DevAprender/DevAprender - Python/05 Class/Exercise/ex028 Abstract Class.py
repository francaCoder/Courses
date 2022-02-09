"""
Create an abstract class called 'Monitor', that will have 2 abstract methods
- Increase clarity
- Decrease clarity

Then, create a new class called 'MonitorFullHD' and put the methods inside it
"""

from abc import ABC, abstractmethod

class Monitor(ABC):
    def increase_clarity(self, number):
        pass

    @abstractmethod
    def decrease_clarity(self, number):
        pass

class MonitorFullHD(Monitor):
    def increase_clarity(self, number):
        print(f"Increasing in {number}%")

    def decrease_clarity(self, number):
        print(f"Decreasing in {number}%")


monitor = MonitorFullHD()
monitor.increase_clarity(20)
monitor.decrease_clarity(20)