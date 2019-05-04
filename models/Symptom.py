from pyknow import *


class Symptom:
    def __init__(self, name, displayValue):
        self.name = name
        self.displayValue = displayValue

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class MySymptom(Fact):
    pass
