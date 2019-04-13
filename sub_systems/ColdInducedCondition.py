from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


class ColdInducedCondition(KnowledgeEngine):
    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Remove the casualty to a warm, dry place.')
        instructions.append('Protect the casualty and yourself from wind, rain, sleet, cold or wet ground.')
        instructions.append('Help the casualty to lie down in a comfortable position.')
        instructions.append('Handle the casualty as gently as possible and avoid excess activity or movement.')
        instructions.append('Remove any wet clothing.')
        instructions.append('Warm the casualty by:\n'
                            '1- Placing between blankets, in a sleeping bag, or wrap in a thermal/emergency rescue '
                            'blanket or similar and cover their head to maintain body heat\n'
                            '2- Hot water bottles, heat packs may be applied to the casualty’s neck, armpits and '
                            'groin taking care to avoid burning the casualty. Body to body contact may be used if '
                            'there are no other means available.\n')
        instructions.append('Aim to stop the temperature dropping any lower rather than attempt rapid rewarming:\n'
                            '1- DO NOT use radiant heat such as fire or electric heater.\n'
                            '2- DO NOT rub affected areas.\n')
        instructions.append('Give casualty warm drinks if conscious. DO NOT give alcohol.')
        instructions.append('Call the ambulance')
        self.onComplete()