from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class Conscious(Fact):
    pass


class PrescribedMedication(Fact):
    pass


class SymptomsLast(Fact):
    pass


# Fact - End

class HeartAttack(KnowledgeEngine):
    @Rule(Conscious('yes'))
    def conscious(self):
        instructions.append('Advise the casualty to immediately sit down to rest and reassure them.')
        self.checkPrescribedMedication()

    @Rule(Conscious('no'))
    def noConscious(self):
        instructions.append('Place casualty in recovery position.')
        instructions.append('Call the ambulance.')
        instructions.append('Stay with the casualty and monitor breathing. Be prepared to give CPR if symptoms worsen.')
        self.onComplete()

    @Rule(PrescribedMedication('yes'))
    def prescribedMedication(self):
        instructions.append('assist the prescribed medication to take it as they have been directed.')
        self.checkSymptomsLast()

    @Rule(PrescribedMedication('no'))
    def noPrescribedMedication(self):
        self.checkSymptomsLast()

    @Rule(SymptomsLast('yes'))
    def symptomsLast(self):
        instructions.append('Call the ambulance.')
        instructions.append('Give 300g (one tablet) of aspirin with water. DO NOT give aspirin to those allergic to '
                            'it or if their doctor has advised them against taking aspirin.')
        instructions.append('Stay with the casualty and monitor consciousness and vital signs. Be prepared to give '
                            'CPR if symptoms worsen.')
        self.onComplete()

    @Rule(SymptomsLast('no'))
    def symptomsNotLast(self):
        instructions.append('Give 300g (one tablet) of aspirin with water. DO NOT give aspirin to those allergic to '
                            'it or if their doctor has advised them against taking aspirin.')
        instructions.append('Stay with the casualty and monitor consciousness and vital signs. Be prepared to give '
                            'CPR if symptoms worsen.')
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        self.checkConscious()

    def checkConscious(self):
        self.reset()
        self.declare(Conscious(input('Is the casualty conscious? (yes / no)')))
        self.run()

    def checkPrescribedMedication(self):
        self.reset()
        self.declare(PrescribedMedication(input('Has the casualty prescribed medication ? (yes / no)')))
        self.run()

    def checkSymptomsLast(self):
        self.reset()
        self.declare(SymptomsLast(input('Did symptoms last for ten (10) minutes or become worse quickly or be severe? '
                                        '(yes / no)')))
        self.run()
