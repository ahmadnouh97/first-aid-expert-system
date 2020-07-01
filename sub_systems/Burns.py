from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class ClothOnFire(Fact):
    pass


class SeriousSituation(Fact):
    pass


# Fact - End

class Burns(KnowledgeEngine):
    @Rule(ClothOnFire('1'))
    def clothOnFire(self):
        instructions.append('Stop the casualty from moving around.')
        instructions.append('Drop the casualty to the ground and wrap in a blanket or similar.')
        instructions.append('Roll the casualty along the ground until flames are smothered.')
        self.commonInstructions()

    @Rule(ClothOnFire('2'))
    def clothNotOnFire(self):
        self.commonInstructions()

    @Rule(SeriousSituation('1'))
    def seriousSituation(self):
        instructions.append('Call the ambulance')
        self.onComplete()

    @Rule(SeriousSituation('2'))
    def notSeriousSituation(self):
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        self.reset()
        self.declare(ClothOnFire(input('Is clothing on fire? \n1- Yes\n2- No\n')))
        self.run()

    @staticmethod
    def doNotInstructions():
        instructions.append('Do not peel off clothing that is stuck to the skin.')
        instructions.append('Do not use ice or iced water to cool a burn.')
        instructions.append('Do not apply lotions, ointments or creams.')
        instructions.append('Do not break blisters.')

    def commonInstructions(self):
        instructions.append('Assess the adequacy of the casualty’s airway and breathing.')
        instructions.append('Cool the burnt area with copious amounts of cool water for up to twenty (20) minutes.')
        instructions.append('Remove any clothing and jewellery from affected area unless stuck to the burn.')
        instructions.append('Cover burnt area with a light non-stick dressing or clean, dry non-fluffy material.')
        instructions.append('Rest and reassure the casualty and check for shock.')
        self.doNotInstructions()
        self.checkIfSeriousSituation()

    def checkIfSeriousSituation(self):
        self.reset()
        self.declare(SeriousSituation(input('If:\n'
                                            '- Burns involving airway, hands, feet, face or genitals.\n'
                                            '- Deep burn.\n'
                                            '- Superficial burn larger than twenty (20) cent piece on an adult or ten'
                                            '(10) cent piece on a child.\n'
                                            '- If in any doubt of what to do.\n'
                                            'say (yes):\n'
                                            '1- Yes\n2- No\n')))
        self.run()
