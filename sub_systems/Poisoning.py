from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Facts - Start

class Case(Fact):
    pass


# Facts - End

class Poisoning(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.initEngine
        engine.startEngine()

    def initEngine(self):
        instructions.append('Urgent medical aid required. Call Triple Zero (000) for an ambulance.')
        instructions.append('Call Poisons Information 13 11 26 and/or follow instructions on any containers.')
        instructions.append('Send any vomit, containers or notes with the casualty to hospital.')
        self.determineCasualtyCase()

    def determineCasualtyCase(self):
        self.reset()
        self.declare(Case(input('What\'s the case?\n'
                                '1- Conscious casualty.\n'
                                '2- Injected.\n'
                                '3- Unconscious casualty.\n'
                                '4- Absorbed poisons.\n'
                                '5- Inhaled Poisons.\n')))
        self.run()

    @Rule(Case('1'))
    def conscious(self):
        instructions.append('Listen to the casualty and give reassurance.')
        instructions.append('Find out what sort of poison is involved and keep any containers for the medical aid to '
                            'see.')
        instructions.append('DO NOT induce vomiting or give anything to eat or drink.')
        instructions.append('Wash any corrosive substance off the mouth and face with water, or wipe off.')
        self.onComplete()

    @Rule(Case('2'))
    def unconscious(self):
        instructions.append('Place the casualty in the recovery position and continue to check their airway and '
                            'breathing regularly.')
        self.onComplete()

    @Rule(Case('3'))
    def inhaled(self):
        instructions.append('Move casualty and yourself to fresh air.')
        instructions.append('Loosen tight clothing.')
        self.onComplete()

    @Rule(Case('4'))
    def absorbedPoisons(self):
        instructions.append('Protect yourself (if possible) use protective clothing such as gloves, goggles and so on.')
        instructions.append('Wash the substance off immediately.')
        instructions.append('Ask the casualty to remove any contaminated clothing.')
        instructions.append('Flush the casualty’s skin with running water.')
        self.onComplete()

    @Rule(Case('5'))
    def injected(self):
        instructions.append('avoid needle stick injuries to yourself and casualty.')
        instructions.append('Treat any other signs and symptoms. Send any empty syringes, bottles and vials with the '
                            'casualty to hospital. ')
        self.onComplete()

    pass
