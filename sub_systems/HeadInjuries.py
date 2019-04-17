from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD
from sub_systems.DRSABCDInfant import DRSABCDInfant


# Fact - Start

class Age(Fact):
    pass


class Conscious(Fact):
    pass


# Fact - End

class HeadInjuries(KnowledgeEngine):
    @Rule(Age('adult'))
    def adult(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    @Rule(Age('infant'))
    def infant(self):
        subEngine = DRSABCDInfant()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    @Rule(Conscious('yes'))
    def conscious(self):
        instructions.append('Rest and reassure the casualty.')
        instructions.append('If NO suspected neck or spinal injury, place casualty in a comfortable position with '
                            'head and shoulders slightly raised.')
        instructions.append('If neck or spinal injuries are suspected, keep the casualty flat and support the head on '
                            'either side to stop movement; improvise using rolled towels, blankets or clothing.')
        instructions.append('Observe for any changes in signs, symptoms and level of consciousness.')
        instructions.append('Call the ambulance.')
        self.onComplete()

    @Rule(Conscious('no'))
    def noConscious(self):
        instructions.append('Place the casualty into the recovery position being careful to support casualty’s head '
                            'and neck in neutral alignment during movement to avoid any twisting action.')
        instructions.append('If any blood or fluid is coming from the ear, place injured side down to allow the fluid '
                            'to drain, place a clean pad between ear and ground and observe the amount draining.')
        instructions.append('Monitor for any changes in signs, symptoms and level of consciousness and ensure the '
                            'airway is kept clear and open.')
        instructions.append('Control any bleeding, but do not apply direct pressure to the skull.')
        instructions.append('Call the ambulance.')
        self.onComplete()

    def startEngine(self):
        self.reset()
        self.declare(
            Age(input('Is the casualty adult child (over 1 year) or infant (under 1 year) ? (adult / infant)')))
        self.run()

    def initEngine(self):
        self.reset()
        self.declare(Conscious(input('Is the casualty conscious? (yes / no)')))
        self.run()
