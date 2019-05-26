from models.Casualty import *
from models.Symptom import *
from sub_systems.TropicalJellyfishStings import *
from sub_systems.NonTropicalJellyfishStings import *
from sub_systems.MarineStings import *
from sub_systems.InsectBite import *
from sub_systems.RedBackSpiderBite import *
from sub_systems.BlueRingedBites import *
from sub_systems.SnakeBite import *
from Data import *


def onComplete():
    printInstructions()


class StingsAndBites(KnowledgeEngine):
    SYMPTOMS = []
    CASUALTIES = [
        Casualty(name='tropical_jellyfish_stings',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Pain at site.'),
                     Symptom(name='respiratory_cardiac_arrest', displayValue='Respiratory and cardiac arrest in '
                                                                             'minutes.'),
                     Symptom(name='pain_back_and_abdomen', displayValue='Severe pain (back and abdomen).'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='sweating.', displayValue='Sweating.'),
                     Symptom(name='feeling_of_impending_doom', displayValue='Feeling of impending doom.'),
                 ],
                 engine=TropicalJellyfishStings()),

        Casualty(name='non_tropical_jellyfish',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Immediate pain ranging from mild irritation to '
                                                               'intense, sharp or burning pain.'),
                     Symptom(name='whip_like_marks', displayValue='Whip like marks.'),
                     Symptom(name='redness_skin', displayValue='Raised welts and redness on the skin.'),
                     Symptom(name='muscle_aches', displayValue='Muscle aches and cramps.'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                 ],
                 engine=NonTropicalJellyfishStings()),

        Casualty(name='marine_stings',
                 symptoms=[
                     Symptom(name='confused', displayValue='Confused.'),
                     Symptom(name='drowsiness', displayValue='Drowsiness.'),
                     Symptom(name='delirium', displayValue='Delirium.'),
                     Symptom(name='unconsciousness', displayValue='Unconsciousness.'),
                     Symptom(name='skin_lips_throat_burns', displayValue='Burns to skin, lips and throat.'),
                     Symptom(name='eyes_skin_irritation', displayValue='Irritation to eyes and skin.'),
                     Symptom(name='difficult_breathing', displayValue='Respiratory distress, such as slow breathing '
                                                                      'or airway blockage.'),
                     Symptom(name='affected_heart_function', displayValue='Affected heart function.'),
                     Symptom(name='abdominal_pain', displayValue='Abdominal pain.'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='blurred_vision', displayValue='Blurred vision.'),
                     Symptom(name='headache', displayValue='Headache.')
                 ],
                 engine=MarineStings()),

        Casualty(name='insect_bites_and_stings',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Pain at site (sometimes extreme).'),
                     Symptom(name='swelling', displayValue='Swelling.'),
                     Symptom(name='site_redness', displayValue='Redness.'),
                     Symptom(name='muscle_weakness', displayValue='Muscle weakness (tick bite).'),
                     Symptom(name='difficult_breathing', displayValue='Difficulty in breathing.'),
                     Symptom(name='swallowing', displayValue='Swallowing.'),
                     Symptom(name='itchy_and_painful_blisters', displayValue='Itchy and painful blisters.')
                 ],
                 engine=InsectBite()),

        Casualty(name='red_back_spider_bite',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Immediate pain at the bite site'),
                     Symptom(name='site_becomes_hot_red_swollen', displayValue='The bite site becomes hot, red and '
                                                                               'swollen.'),
                     Symptom(name='intense_local_pain', displayValue='Intense local pain which increases and spreads.'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='abdominal_pain', displayValue='Abdominal pain.'),
                     Symptom(name='sweating_at_bite_site',
                             displayValue='Profuse sweating, especially at the bite site.'),
                     Symptom(name='swelling', displayValue='Swelling.'),
                 ],
                 engine=RedBackSpiderBite()),

        Casualty(name='blue_ringed_octopus_and_cone_shell_bites',
                 symptoms=[
                     Symptom(name='painless_bite_with_visible_blood_spot', displayValue='A painless bite with a spot '
                                                                                        'of blood visible.'),
                     Symptom(name='feeling_of_numbness', displayValue='Numbness to lips and tongue, muscle weakness '
                                                                      'which can stop the casualties breathing.'),
                 ],
                 engine=BlueRingedBites()),

        Casualty(name='snake_bite',
                 symptoms=[
                     Symptom(name='puncture_marks_or_scratches', displayValue='Puncture marks or scratches,may bleed.'),
                     Symptom(name='nausea', displayValue='Nausea.'),
                     Symptom(name='vomiting', displayValue='Vomiting.'),
                     Symptom(name='diarrhoea', displayValue='Diarrhoea.'),
                     Symptom(name='headache', displayValue='Headache.'),
                     Symptom(name='drowsiness', displayValue='Drowsiness.'),
                     Symptom(name='giddiness_or_faintness', displayValue='Giddiness or faintness.'),
                     Symptom(name='blurred_vision', displayValue='Blurred vision.'),
                     Symptom(name='drooping_eyelids', displayValue='Drooping eyelids.'),
                     Symptom(name='voice_changes', displayValue='Voice changes.'),
                     Symptom(name='trouble_speaking', displayValue='Trouble speaking.'),
                     Symptom(name='swallowing', displayValue='Swallowing.'),
                     Symptom(name='throat_tightness', displayValue='Throat tightness.'),
                     Symptom(name='chest_tightness', displayValue='Chest tightness.'),
                     Symptom(name='difficult_breathing', displayValue='Difficult breathing.'),
                     Symptom(name='respiratory_weakness_or_arrest', displayValue='respiratory weakness or arrest.'),
                 ],
                 engine=SnakeBite()),
    ]
    userSymptoms = []

    def __init__(self):
        super(StingsAndBites, self).__init__()
        self.SYMPTOMS = self.init_symptoms()
        self.userSymptoms = []

    @Rule(MySymptom(symptom='symptom' << W()))
    def update(self, symptom: str):
        self.updateCasualties(symptom)

    def updateCasualties(self, my_symptom: str):
        # increase the probability of each casualty that contains this symptom
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
        # for symptom in self.userSymptoms:
        #     print(f'{symptom.displayValue}\n')

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
