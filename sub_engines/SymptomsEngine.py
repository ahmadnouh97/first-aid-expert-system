from casulities_categories.BonesAndMuscles import *
from casulities_categories.BurnsCasualties import *
from casulities_categories.CommonDiseases import *
from casulities_categories.HeartDiseases import *
from casulities_categories.StingsAndBites import *
from pyknow import *

BONES_AND_MUSCLES = 'Bones And Muscles'
BURNS = 'Burns And Scalds'
HEART_DISEASES = 'Heart Diseases'
COMMON_DISEASES = 'Common Diseases'
STINGS_AND_BITES = 'Stings And Bites'


class Case(Fact):
    pass


class SymptomsEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.subEngine = super()

    @Rule(Case('1'))
    def bonesAndMuscles(self):
        self.subEngine = BonesAndMuscles()
        self.subEngine.startEngine()

    @Rule(Case('2'))
    def burns(self):
        self.subEngine = BurnsCasualties()
        self.subEngine.startEngine()

    @Rule(Case('3'))
    def heartDiseases(self):
        self.subEngine = HeartDiseases()
        self.subEngine.startEngine()

    @Rule(Case('4'))
    def stingsAndBites(self):
        self.subEngine = StingsAndBites()
        self.subEngine.startEngine()

    @Rule(Case('5'))
    def commonDiseases(self):
        self.subEngine = CommonDiseases()
        self.subEngine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Case(input(f'Choose case: (1- {BONES_AND_MUSCLES} ,'
                                f' 2- {BURNS} ,'
                                f' 3- {HEART_DISEASES} ,'
                                f' 4- {STINGS_AND_BITES} ,'
                                f' 5- {COMMON_DISEASES})\n')))
        self.run()
