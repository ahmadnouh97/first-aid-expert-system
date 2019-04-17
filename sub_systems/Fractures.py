from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD
from sub_systems.DRSABCDInfant import DRSABCDInfant


# Fact - Start

class Age(Fact):
    pass


# Fact - End

class Fractures(KnowledgeEngine):
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

    def startEngine(self):
        self.reset()
        self.declare(
            Age(input('Is the casualty adult child (over 1 year) or infant (under 1 year) ? (adult / infant)')))
        self.run()

    def initEngine(self):
        instructions.append('Control any bleeding and cover any wounds.')
        instructions.append('Rest and reassure, ask the casualty to remain still.')
        instructions.append('Immobilise the fracture in most comfortable position:\n'
                            '1- DO NOT attempt to force a fracture back into place.\n'
                            '2- Use broad bandages (where possible) to immobilise the fracture.\n'
                            '3- Place a padded splint along the injured limb then bandage above and below the '
                            'fracture site leaving a five (5) cm gap either side of the fracture to prevent movement. '
                            'DO NOT bandage over the fracture.\n')
        instructions.append('The casualty may be able to support the fracture themselves.')
        instructions.append('Check that bandages are not too tight or too loose and every fifteen (15) minutes and '
                            'watch for signs of loss of circulation to hands or feet.')
        instructions.append('Call the ambulance.')
        self.onComplete()
