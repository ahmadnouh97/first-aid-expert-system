from pyknow import *


class Symptom:
    def __init__(self, name, displayValue):
        self.name = name
        self.displayValue = displayValue


class MySymptom(Fact):
    pass
