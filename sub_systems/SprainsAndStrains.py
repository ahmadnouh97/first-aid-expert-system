from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


class SprainsAndStrains(KnowledgeEngine):
    def startEngine(self):
        engine = DRSABCD()
        engine.onComplete = self.initEngine
        engine.startEngine()

    def initEngine(self):
        instructions.append('Rest and reassure the casualty.')
        instructions.append('Manage as a fracture if any doubt.')
        instructions.append('Follow the RICE management plan:\n'
                            '  + REST the casualty and the injured part.\n'
                            '  + ICEPACK (cold compress) for fifteen (15) minutes.\n'
                            '  + COMPRESSION bandage after the icepack – apply firmly and extend well beyond the '
                            'injury.\n'
                            '  + ELEVATE the limb.')
        instructions.append('Rules when using icepacks:\n'
                            '  + Wrap icepack in a damp cloth.\n'
                            '  + Apply to the injured site for fifteen (15) minutes and then reapply every two (2) '
                            'hours for first twenty-four (24) hours.\n'
                            '  + Never apply ice directly to the skin or onto an open wound. If no ice is available '
                            'use a cloth wrung out in cold water – this will need replacing every ten (10) minutes.')
        instructions.append('Seek medical attention if in doubt or if no improvement after RICE.')
        self.onComplete()

    pass
