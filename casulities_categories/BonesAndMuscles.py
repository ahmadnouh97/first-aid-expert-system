from Casualty import *
from Symptom import *


class BonesAndMuscles(KnowledgeEngine):
    CASUALTIES = [
        Casualty(name='fractures',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Pain at or near the site of the injury.'),
                     Symptom(name='difficult_moving', displayValue='Difficult or impossible normal movement.'),
                     Symptom(name='loss_of_power', displayValue='Loss of function.'),
                     Symptom(name='abnormal_movement', displayValue='Deformity or abnormal mobility.'),
                     Symptom(name='tenderness and swelling', displayValue='Tenderness and swelling.'),
                     Symptom(name='discoloration_bruising', displayValue='Discolouration and bruising.'),
                 ]),

        Casualty(name='dislocation',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Pain at or near the site of injury.'),
                     Symptom(name='difficult_moving_joint', displayValue='Difficult or impossible to move the joint.'),
                     Symptom(name='loss_of_power', displayValue='Loss of power.'),
                     Symptom(name='abnormal_movement', displayValue='Deformity or abnormal movement.'),
                     Symptom(name='tenderness', displayValue='Tenderness.'),
                     Symptom(name='swelling', displayValue='Swelling.'),
                     Symptom(name='discoloration_bruising', displayValue='Discoloration and bruising.'),
                 ]),

        Casualty(name='spinal_injury',
                 symptoms=[
                     Symptom(name='pain_at_site', displayValue='Pain at or below site of injury.'),
                     Symptom(name='tenderness', displayValue='Tenderness.'),
                     Symptom(name='deformity', displayValue='Deformity.'),
                     Symptom(name='absent_or_altered_sensation', displayValue='Absent or altered sensation below site '
                                                                              'of injury e.g. tingling.'),
                     Symptom(name='faintness', displayValue='Faintness.'),
                     Symptom(name='dizziness', displayValue='Dizziness.'),
                     Symptom(name='impaired_movement',
                             displayValue='Loss of/or impaired movement below site of injury.')
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
                                                                       'consciousness.'),
                 ]),

    ]

    def __init__(self):
        super(BonesAndMuscles, self).__init__()

    @Rule(MySymptom(symptom='symptom' << W()))
    def update(self, symptom: str):
        self.updateCasualties(symptom)

    def updateCasualties(self, my_symptom: str):
        for casualty in self.CASUALTIES:
            if my_symptom in [symptom.name for symptom in casualty.symptoms]:
                casualty.increaseProbability()