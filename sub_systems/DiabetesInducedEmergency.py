from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start
class Conscious(Fact):
    pass


class BloodSugarLevel(Fact):
    pass


# Fact - End
class DiabetesInducedEmergency(KnowledgeEngine):
    @Rule(Conscious('yes'))
    def conscious(self):
        self.reset()
        self.declare(
            BloodSugarLevel(input('Does the patient suffer from (low / high) blood sugar level? (low / high)')))
        self.run()

    @Rule(Conscious('no'))
    def noConscious(self):
        instructions.append('Place the casualty into the recovery position.')
        instructions.append('Give nothing by mouth.')
        instructions.append('Call the ambulance.')
        self.onComplete()

    @Rule(BloodSugarLevel('low'))
    def lowBloodSugar(self):
        instructions.append('Help casualty into a comfortable position and reassure them.')
        instructions.append('Give sugar such as glucose tablets, jellybeans or a sweet drink (such as a soft drink or '
                            'cordial).\n DO NOT give diet soft drinks or sugar free cordials.')
        instructions.append('Continue giving sugar every 15 minutes until the casualty recovers.')
        instructions.append('Follow up with a sandwich or other food.')
        instructions.append('If there is no improvement call the ambulance.')
        self.onComplete()

    @Rule(BloodSugarLevel('high'))
    def highBloodSugar(self):
        instructions.append('Call the ambulance.')
        instructions.append('If help delayed give sips of water only.')
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        self.reset()
        self.declare(Conscious(input('Is the casualty conscious? (yes / no)')))
        self.run()
