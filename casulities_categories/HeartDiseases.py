from models.Casualty import *
from models.Symptom import *


class HeartDiseases(KnowledgeEngine):
    SYMPTOMS = []
    CASUALTIES = [
        Casualty(name='shock',
                 symptoms=[
                     Symptom(name='weakness', displayValue='Weak.'),
                     Symptom(name='rapid_pulse', displayValue='Rapid pulse.'),
                     Symptom(name='feeling_cold', displayValue='Feeling cold.'),
                     Symptom(name='clammy_skin', displayValue='Clammy skin.'),
                     Symptom(name='rapid_breathing', displayValue='Rapid breathing.'),
                     Symptom(name='faintness', displayValue='Faintness.'),
                     Symptom(name='dizziness', displayValue='Dizziness.'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='pale', displayValue='Pale face, fingernails, lips.')
                 ]),

        Casualty(name='stroke',
                 symptoms=[
                     Symptom(name='consciousness_decrease', displayValue='Sudden decrease in level of consciousness.'),
                     Symptom(name='weakness', displayValue='Weakness or paralysis on either one or both sides of the '
                                                           'body.'),
                     Symptom(name='feeling_of_numbness', displayValue='Feeling of numbness in face, arm or leg.'),
                     Symptom(name='difficulty_speaking', displayValue='Difficulty speaking or understanding.'),
                     Symptom(name='dizziness', displayValue='Dizziness, loss of balance, unexplained fall.'),
                     Symptom(name='disturbed_vision', displayValue='Disturbed vision.'),
                     Symptom(name='confused', displayValue='Confusion.')
                 ]),

        Casualty(name='heart_attack',
                 symptoms=[
                     Symptom(name='chest_pain', displayValue='Pain in the chest.'),
                     Symptom(name='breathlessness', displayValue='Breathlessness.'),
                     Symptom(name='dizziness', displayValue='Dizziness.'),
                     Symptom(name='feel_sick', displayValue='Feel sick.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='pale', displayValue='Pale.'),
                     Symptom(name='feeling_cold', displayValue='Feeling Cold.'),
                     Symptom(name='clammy_skin', displayValue='Clammy skin.'),
                     Symptom(name='cardiac_arrest', displayValue='May collapse and suffer a cardiac arrest.')
                 ]),
    ]
    userSymptoms = []

    def __init__(self):
        super(HeartDiseases, self).__init__()
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