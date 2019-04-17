from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD
from sub_systems.DRSABCDInfant import DRSABCDInfant


# Fact - Start

class Age(Fact):
    pass


class CoughingSufficed(Fact):
    pass


class ConsciousAdult(Fact):
    pass


class ConsciousInfant(Fact):
    pass


class ObstructionClearedAdult(Fact):
    pass


class ObstructionClearedInfant(Fact):
    pass


# Fact - End

class Chocking(KnowledgeEngine):
    @Rule(Age('adult'))
    def adult(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine1
        subEngine.startEngine()

    @Rule(Age('infant'))
    def infant(self):
        subEngine = DRSABCDInfant()
        subEngine.onComplete = self.initEngine2
        subEngine.startEngine()

    @Rule(CoughingSufficed('yes'))
    def coughingSufficed(self):
        self.onComplete()

    @Rule(CoughingSufficed('no'))
    def coughingNotSufficed(self):
        instructions.append('Immediately call Triple Zero (000) for an ambulance.')
        self.checkConscious(is_infant=False)

    @Rule(ConsciousAdult('yes'))
    def consciousAdult(self):
        instructions.append('Position the casualty leaning forward with their head and chest low and give up to five '
                            '(5) sharp back blows between the shoulder blades with heel of one hand.')
        instructions.append('Check after each back blow to see if the obstruction has been cleared.')
        self.checkIfObstructionCleared(is_infant=False)

    @Rule(ConsciousAdult('no'))
    def noConsciousAdult(self):
        instructions.append('Commence CPR.')
        instructions.append('Call Triple Zero (000) for an ambulance.')
        self.onComplete()

    @Rule(ConsciousInfant('yes'))
    def consciousInfant(self):
        instructions.append('Give up to five (5) sharp back blows:\n'
                            '1- Position infant with head and shoulders on your hand and forearm facing downwards.\n'
                            '2- Hold infant’s mouth open with your fingers.\n'
                            '3- Give up to five (5) sharp blows between shoulders with heel of one hand.\n'
                            '4- Check if obstruction has been cleared after each back blow and remove any foreign '
                            'material that may have loosened.\n')
        self.checkIfObstructionCleared(is_infant=True)

    @Rule(ConsciousInfant('no'))
    def noConsciousInfant(self):
        instructions.append('Commence CPR.')
        instructions.append('Call the ambulance.')
        self.onComplete()

    @Rule(ObstructionClearedAdult('yes'))
    def obstructionClearedAdult(self):
        self.onComplete()

    @Rule(ObstructionClearedAdult('no'))
    def obstructionNotClearedAdult(self):
        instructions.append('Use the heel of the hand on the breastbone.')
        instructions.append('Place other hand flat between the shoulder blades to support the casualty and deliver up '
                            'to five (5) chest thrusts. Chest thrusts are similar to chest compressions but sharper '
                            'and delivered at a slower rate.')
        instructions.append('Check to see if the obstruction has cleared after each thrust.')
        instructions.append('If obstruction does not clear continue alternating with five (5) back blows and five (5) '
                            'chest thrusts until medical aid arrives.')
        instructions.append('If the casualty becomes unresponsive Commence CPR and call the ambulance.')
        self.onComplete()

    @Rule(ObstructionClearedInfant('yes'))
    def obstructionClearedInfant(self):
        instructions.append('Position infant with head pointing downwards on forearm, and remove any foreign material '
                            'that may have loosened carefully with your little finger.')
        self.onComplete()

    @Rule(ObstructionClearedInfant('no'))
    def obstructionNotClearedInfant(self):
        instructions.append('Continue alternating with five (5) back blows and five (5) chest thrusts until medical '
                            'aid arrives.')
        instructions.append('If the infant becomes unresponsive Commence CPR and call the ambulance.')
        self.onComplete()

    def startEngine(self):
        self.reset()
        self.declare(
            Age(input('Is the casualty adult child (over 1 year) or infant (under 1 year) ? (adult / infant)')))
        self.run()

    def initEngine1(self):
        instructions.append('Encourage the casualty to relax, breathe deeply and encourage coughing to remove object '
                            'and observe for any deterioration.')
        self.checkCoughingSufficed()

    def initEngine2(self):
        self.checkConscious(is_infant=True)

    def checkCoughingSufficed(self):
        self.reset()
        self.declare(CoughingSufficed(input('Was coughing sufficient in removing the object? (yes / no)')))
        self.run()

    def checkConscious(self, is_infant: bool):
        self.reset()
        if is_infant:
            self.declare(ConsciousInfant(input('Is the infant conscious? (yes / no)')))
        else:
            self.declare(ConsciousAdult(input('Is the casualty conscious? (yes / no)')))
        self.run()

    def checkIfObstructionCleared(self, is_infant: bool):
        self.reset()
        if is_infant:
            self.declare(ObstructionClearedInfant('Has the obstruction been cleared ? (yes / no)'))
        else:
            self.declare(ObstructionClearedAdult('Has the obstruction been cleared ? (yes / no)'))
        self.run()
