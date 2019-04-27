from Casualty import *
from Symptom import *


class BurnsCasualties(KnowledgeEngine):
    CASUALTIES = [
        Casualty(name='superficial_burn_or_scald',
                 symptoms=[
                     Symptom(name='red_skin', displayValue='Red skin.'),
                     Symptom(name='pain_at_site', displayValue='Pain at burn site.'),
                     Symptom(name='may_blister', displayValue='May blister.'),
                     Symptom(name='swelling', displayValue='Swelling.'),
                 ]),

        Casualty(name='deep_burn_or_scald',
                 symptoms=[
                     Symptom(name='white_skin', displayValue='White skin.'),
                     Symptom(name='no_pain', displayValue='No pain where nerve endings have been destroyed.'),
                     Symptom(name='surrounded_by_superficial_burns', displayValue='Usually surrounded by superficial '
                                                                                  'burns.')
                 ])
    ]

    def __init__(self):
        super(BurnsCasualties, self).__init__()

    @Rule(MySymptom(symptom='symptom' << W()))
    def update(self, symptom: str):
        self.updateCasualties(symptom)

    def updateCasualties(self, my_symptom: str):
        for casualty in self.CASUALTIES:
            if my_symptom in [symptom.name for symptom in casualty.symptoms]:
                casualty.increaseProbability()
