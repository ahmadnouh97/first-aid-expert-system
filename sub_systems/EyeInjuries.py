from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class MajorOrMinor(Fact):
    pass


class PenetratingInjury(Fact):
    pass


# Fact - End

class EyeInjuries(KnowledgeEngine):
    @Rule(MajorOrMinor('major'))
    def major(self):
        instructions.append('DO NOT remove any embedded object.')
        instructions.append('Lay casualty flat on their back and reassure.')
        self.checkIfPenetratingInjury()

    @Rule(MajorOrMinor('minor'))
    def minor(self):
        instructions.append('Wash out the eye gently with water or normal saline, from the corner closest to the nose '
                            'outwards.')
        instructions.append('If unsuccessful, pad eye and seek medical aid.')
        self.onComplete()

    @Rule(PenetratingInjury('yes'))
    def penetratingInjury(self):
        instructions.append('Carefully place pads around the object and bandage gently in place. DO NOT place '
                            'pressure on the eye.')
        self.performCommonInstruction()

    @Rule(PenetratingInjury('no'))
    def noPenetratingInjury(self):
        self.performCommonInstruction()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Wash hands thoroughly and wear gloves if available.')
        instructions.append('DO NOT:\n'
                            '1- Touch the eyeball or any contact lens.\n'
                            '2- Allow the casualty to rub their eye.\n'
                            '3- Try to remove any object which is penetrating the eye.\n'
                            '4- Apply pressure when bandaging the eye.\n')
        self.checkMajorOrMoinor()

    def checkMajorOrMoinor(self):
        self.reset()
        self.declare(MajorOrMinor(input('Is the injury major or minor ? (major / minor)')))
        self.run()

    def checkIfPenetratingInjury(self):
        self.reset()
        self.declare(PenetratingInjury(input('Is it a penetrating eye injury? (yes / no)')))
        self.run()


    def performCommonInstruction(self):
        instructions.append('Pad the head on each side with blankets/towels to stop the casualty from moving their '
                            'head.')
        instructions.append('Reassure casualty and ask them to keep their head as still as possible as they will be '
                            'anxious.')
        instructions.append('Call the ambulance')
        self.onComplete()
