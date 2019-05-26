from models.Casualty import *
from models.Symptom import *
from sub_systems.Burns import *
from Data import *


def onComplete():
    printInstructions()


class BurnsCasualties(KnowledgeEngine):
    SYMPTOMS = []
    CASUALTIES = [
        Casualty(name='superficial_burn_or_scald',
                 symptoms=[
                     Symptom(name='red_skin', displayValue='Red skin.'),
                     Symptom(name='pain_at_site', displayValue='Pain at burn site.'),
                     Symptom(name='may_blister', displayValue='May blister.'),
                     Symptom(name='swelling', displayValue='Swelling.'),
                 ],
                 engine=Burns()),

        Casualty(name='deep_burn_or_scald',
                 symptoms=[
                     Symptom(name='white_skin', displayValue='White skin.'),
                     Symptom(name='no_pain', displayValue='No pain where nerve endings have been destroyed.'),
                     Symptom(name='surrounded_by_superficial_burns', displayValue='Usually surrounded by superficial '
                                                                                  'burns.')
                 ],
                 engine=Burns())
    ]
    userSymptoms = []

    def __init__(self):
        super(BurnsCasualties, self).__init__()
        self.SYMPTOMS = self.init_symptoms()
        self.userSymptoms = []

    @Rule(MySymptom(symptom='symptom' << W()))
    def update(self, symptom: str):
        self.updateCasualties(symptom)

    def updateCasualties(self, my_symptom: str):
        for casualty in self.CASUALTIES:
            if my_symptom in [symptom.name for symptom in casualty.symptoms]:
                casualty.increaseProbability()

    def init_symptoms(self):
        mySet = set()
        for casualty in self.CASUALTIES:
            for symptom in casualty.symptoms:
                mySet.add(symptom)

        return list(mySet)

    def displaySymptoms(self):
        # display symptoms to the user
        print('symptoms:\n')
        for i, symptom in enumerate(self.SYMPTOMS):
            print(f'{i + 1} - {symptom.displayValue}')

        # read user input
        userInputs = input('What are the casualty symptoms ?\n').split()

        # the symptoms those user choose
        self.userSymptoms = [self.SYMPTOMS[int(index) - 1] for index in userInputs]
        for symptom in self.userSymptoms:
            print(f'{symptom.displayValue}\n')

    def startEngine(self):
        self.displaySymptoms()
        self.reset()
        for symptom in self.userSymptoms:
            self.declare(MySymptom(symptom=symptom.name))
        self.run()
        self.onComplete()

    def onComplete(self):
        maxProbability = -1
        maxCasualty = -1
        for casualty in self.CASUALTIES:
            print(f'{casualty.name}: {casualty.probability}\n')
            if casualty.probability > maxProbability:
                maxProbability = casualty.probability
                maxCasualty = casualty
        print(f'Most probability: {maxCasualty.name} with {maxProbability}')
        maxCasualty.engine.onComplete = onComplete
        maxCasualty.engine.startEngine()
