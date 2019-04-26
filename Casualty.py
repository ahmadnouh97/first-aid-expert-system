
class Casualty:
    def __init__(self, name, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.counter = 0
        self.totalSymptomsNumber = len(symptoms)
        self.probability = 0

    def increaseProbability(self):
        self.counter = self.counter + 1
        self.probability = self.counter / self.totalSymptomsNumber
