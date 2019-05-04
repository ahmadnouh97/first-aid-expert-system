from models.Casualty import *
from models.Symptom import *


class CommonDiseases(KnowledgeEngine):
    SYMPTOMS = []
    CASUALTIES = [
        Casualty(name='asthma_attack',
                 symptoms=[
                     Symptom(name='wheezing', displayValue='Increasing wheeze.'),
                     Symptom(name='coughing', displayValue='Persistent cough.'),
                     Symptom(name='shortness_breathing', displayValue='Difficulty breathing, shortness of breath.'),
                     Symptom(name='difficulty_speaking', displayValue='Only able to speak in short sentences.'),
                     Symptom(name='chest_tightness', displayValue='Chest tightness.')
                 ]),

        Casualty(name='seizures_and_epilepsy',
                 symptoms=[
                     Symptom(name='muscle_stiffening', displayValue='Sudden spasm of muscles producing stiffness or '
                                                                    'rhythmic jerking movements. If standing, '
                                                                    'the casualty will fall which may result in '
                                                                    'injury.'),
                     Symptom(name='suddenly_cry_out', displayValue='Suddenly cry out.'),
                     Symptom(name='difficult_breathing', displayValue='Shallow breathing or breathing may temporarily '
                                                                      'stop.'),
                     Symptom(name='pale', displayValue='Pale, blue tinged lips and face.'),
                     Symptom(name='excessive_saliva_frothing', displayValue='Excessive saliva (frothing) from the '
                                                                            'mouth.'),
                     Symptom(name='changes_in_conscious', displayValue='Changes in conscious state from being fully '
                                                                       'alert to confused, drowsy or loss of '
                                                                       'consciousness.')
                 ]),

        Casualty(name='severe_allergic_reaction',
                 symptoms=[
                     Symptom(name='difficult_breathing', displayValue='Difficult and/or noisy breathing.'),
                     Symptom(name='wheezing', displayValue='Wheeze.'),
                     Symptom(name='persistent_cough', displayValue='Persistent cough.'),
                     Symptom(name='face_tongue_swelling', displayValue='Swelling of the face and tongue.'),
                     Symptom(name='throat_swelling', displayValue='Swelling of the throat.'),
                     Symptom(name='throat_tightness', displayValue='Tightness of the throat.'),
                     Symptom(name='difficulty_speaking', displayValue='Difficulty talking and/or “hoarse” voice.'),
                     Symptom(name='dizziness', displayValue='Persistent dizziness.'),
                     Symptom(name='collapse', displayValue='Persistent collapse.'),
                     Symptom(name='pale', displayValue='Young children may become pale and floppy.'),
                     Symptom(name='abdominal_pain', displayValue='Abdominal pain.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='Hives_welts_and_body_redness', displayValue='Hives, welts and body redness.')
                 ]),

        Casualty(name='cold_induced_condition',
                 symptoms=[
                     Symptom(name='feeling_cold', displayValue='Feeling cold.'),
                     Symptom(name='shivering', displayValue='Shivering.'),
                     Symptom(name='clumsiness_and_slurred_speech', displayValue='Clumsiness and slurred speech.'),
                     Symptom(name='apathy_and_irrational_behaviour', displayValue='Apathy and irrational behaviour.'),
                     Symptom(name='pulse_difficult_to_find', displayValue='Pulse may be difficult to find.'),
                     Symptom(name='slow_heart_rate', displayValue='Heart rate may slow.'),
                     Symptom(name='low_consciousness', displayValue='Level of consciousness continues to decline.'),
                     Symptom(name='unconsciousness', displayValue='Unconsciousness.'),
                     Symptom(name='cardiac_arrest', displayValue='Cardiac arrest may occur.')
                 ]),

        Casualty(name='heat_induced_conditions_stroke',
                 symptoms=[
                     Symptom(name='high_body_temperature', displayValue='High body temperature <40°C.'),
                     Symptom(name='feeling_hot', displayValue='Flushed hot.'),
                     Symptom(name='dry_skin', displayValue='Dry skin.'),
                     Symptom(name='pounding', displayValue='Pounding.'),
                     Symptom(name='rapid_pulse', displayValue='Rapid pulse which gradually weakens.'),
                     Symptom(name='thirst', displayValue='Thirst.'),
                     Symptom(name='headache', displayValue='Headache.'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='dizziness', displayValue='Dizziness.'),
                     Symptom(name='faintness', displayValue='Faintness.'),
                     Symptom(name='altered_mental_state', displayValue='Altered mental state which may progress to '
                                                                       'seizures unconsciousness/death.')
                 ]),

        Casualty(name='heat_induced_conditions_stroke_exhaustion',
                 symptoms=[
                     Symptom(name='painful_muscle_cramps', displayValue='Painful muscle cramps in legs and abdomen.'),
                     Symptom(name='feeling_hot', displayValue='Feeling hot.'),
                     Symptom(name='exhausted', displayValue='Exhausted.'),
                     Symptom(name='weakness', displayValue='Weakness.'),
                     Symptom(name='rapid_breathing', displayValue='Rapid breathing.'),
                     Symptom(name='shortness_breathing', displayValue='Shortness of breath.'),
                     Symptom(name='pale', displayValue='Pale.'),
                     Symptom(name='cool_clammy_skin', displayValue='Cool clammy skin.')
                 ]),

        Casualty(name='low_blood_sugar',
                 symptoms=[
                     Symptom(name='hungry', displayValue='Hungry.'),
                     Symptom(name='pale', displayValue='Pale.'),
                     Symptom(name='sweaty', displayValue='Sweaty.'),
                     Symptom(name='weakness', displayValue='Weak.'),
                     Symptom(name='confused', displayValue='Confused.'),
                     Symptom(name='aggressive', displayValue='Irritable or aggressive.')
                 ]),

        Casualty(name='high_blood_sugar',
                 symptoms=[
                     Symptom(name='thirst', displayValue='Excessive thirst.'),
                     Symptom(name='feeling_hot', displayValue='Feeling hot.'),
                     Symptom(name='dry_skin', displayValue='Dry skin.'),
                     Symptom(name='tired', displayValue='Feeling tired.'),
                     Symptom(name='blurred_vision', displayValue='Blurred vision.'),
                     Symptom(name='acetone_breath_smell', displayValue='Smell of acetone on the breath.')
                 ]),
    ]
    userSymptoms = []

    def __init__(self):
        super(CommonDiseases, self).__init__()
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
            self.declare(symptom.name)
        self.run()