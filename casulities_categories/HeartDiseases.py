from Symptom import *


class HeartDiseases(KnowledgeEngine):
    CASUALTIES = [

    ]

    def __init__(self):
        super(HeartDiseases, self).__init__()

    @Rule(MySymptom(symptom='symptom' << W()))
    def update(self, symptom: str):
        self.updateCasualties(symptom)

    def updateCasualties(self, my_symptom: str):
        for casualty in self.CASUALTIES:
            if my_symptom in [symptom.name for symptom in casualty.symptoms]:
                casualty.increaseProbability()
