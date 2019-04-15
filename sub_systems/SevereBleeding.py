from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class Case(Fact):
    pass


class BloodOozing(Fact):
    pass


# Fact - End

class SevereBleeding(KnowledgeEngine):

    def startEngine(self):
        instructions.append('IMPORTANT wear gloves to prevent infection, if possible.')
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        self.reset()
        self.declare(Case(input("Is the casualty:\n"
                                "1- Conscious\n"
                                "2- Unconscious\n")))
        self.run()

    @Rule(Case('1'))
    def conscious(self):
        instructions.append("Reassure and lie the casualty down and remove or cut their clothing to expose the wound.")
        instructions.append('Apply direct pressure over the wound using a pad or your hands. Instruct the casualty to '
                            'do this if possible.')
        instructions.append('Squeeze the wound edges together if possible.')
        instructions.append('Raise and support the injured part above the level of the casualty’s heart. Handle '
                            'gently if you suspect a broken bone.')
        instructions.append('Apply a pad over the wound and secure by bandaging over the wound.')
        self.reset()
        self.declare(BloodOozing(input('Is blood oozing through the original bandage?\n'
                                       '1- Yes\n'
                                       '2- No\n')))
        self.run()

    @Rule(Case('2'))
    def unconscious(self):
        instructions.append("Control bleeding as for a conscious casualty.")
        instructions.append("Urgent medical aid. Call Triple Zero (000) for an ambulance.")
        self.onComplete()

    @Rule(BloodOozing('1'))
    def bloodOozing(self):
        instructions.append("Do not remove the original bandage.")
        instructions.append("Place another pad and bandage over the top of the original one.")
        self.continueConscious()
        self.onComplete()

    @Rule(BloodOozing('2'))
    def bloodNotOozing(self):
        self.continueConscious()
        self.onComplete()

    @staticmethod
    def continueConscious():
        instructions.append('Monitor consciousness and vital signs.')
        instructions.append('Urgent medical aid. Call Triple Zero (000) for an ambulance.')
        instructions.append('DO NOT give the casualty anything to eat or drink.')
