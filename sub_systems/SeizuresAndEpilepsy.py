from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Facts - Start

class DuringOrAfterSeizure(Fact):
    pass


class ConditionsMet(Fact):
    pass


# Facts - End

class SeizuresAndEpilepsy(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.checkDuringOrAfterSeizure
        engine.startEngine()

    def checkDuringOrAfterSeizure(self):
        self.reset()
        self.declare(DuringOrAfterSeizure(input('Is the casualty is IN a seizure or recovering from it?\n'
                                                '1- In it.\n'
                                                '2- Recovering from it.\n')))
        self.run()

    @Rule(DuringOrAfterSeizure('1'))
    def during(self):
        self.completeDuring()
        self.onComplete()

    @staticmethod
    def completeDuring():
        instructions.append('DO NOT')
        instructions.append(' + Restrain the casualty or restrict movement.')
        instructions.append(' + Put anything in the casualty’s mouth.')
        instructions.append(' + Move the casualty, unless in danger.')
        instructions.append('Protect casualty from environment: move furniture, cushion head and shoulders.')
        instructions.append('Ensure the airway is maintained.')
        instructions.append('Follow the casualty’s Seizure Management Plan if in place.')
        instructions.append('Record the duration of the seizure.')

    @Rule(DuringOrAfterSeizure('2'))
    def after(self):
        instructions.append('Place casualty into Recovery Position, ensure that the airway is clear and open.')
        instructions.append('Manage any injuries. Rest and reassure.')
        instructions.append('Seek medical aid.')
        instructions.append('DO NOT disturb if casualty falls asleep, but continue to monitor breathing and response.')
        self.checkForConditions()

    def checkForConditions(self):
        self.reset()
        self.declare(ConditionsMet(input('Are any of these true?\n'
                                         ' + First ever seizure.\n'
                                         ' + The seizure continues for more than five (5) minutes or another seizure '
                                         'quickly follows.\n'
                                         ' + The casualty has been injured, is a diabetic or is pregnant.\n'
                                         '1- Yes\n'
                                         '2- No\n')))
        self.run()

    @Rule(ConditionsMet('1'))
    def conditionsMet(self):
        instructions.append('Call Triple Zero (000) for an ambulance.')
        self.onComplete()

    @Rule(ConditionsMet('2'))
    def conditionsNotMet(self):
        self.onComplete()

    pass
