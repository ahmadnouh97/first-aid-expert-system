from sub_systems.DRSABCD import *
from sub_systems.InsectBite import *
from sub_systems.AsthmaAttack import *
from sub_systems.BlueRingedBites import *
from sub_systems.ColdInducedCondition import *
from sub_systems.DiabetesInducedEmergency import *
from sub_systems.Burns import *
from sub_systems.Dislocation import *
from Data import *

# Facts - Start

CASE_DRSABCD = "DRSABCD"
CASE_INSECT_BITE = "Insect Bite"
ASTHMA_ATTACK = "Asthma Attack"
BLUE_RINGED_BITES = "Blue Ringed Bites"
BURNS = "Burns and Scalds"


# Facts - End

class Case(Fact):
    pass


def onComplete():
    printInstructions()


# Engine - Start

class MainEngine(KnowledgeEngine):

    @Rule(Case("1"))
    def startDRSABCD(self):
        engine = DRSABCD()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("2"))
    def startInsectBite(self):
        engine = InsectBite()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("3"))
    def startColdInducedCondition(self):
        engine = ColdInducedCondition()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("4"))
    def startDiabtes(self):
        engine = DiabetesInducedEmergency()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("5"))
    def startDisLocation(self):
        engine = Dislocation()
        engine.onComplete = onComplete
        engine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Case(input(f"Choose case: (1- {CASE_DRSABCD}, 2- {CASE_INSECT_BITE})\n")))
        self.run()

    @Rule(NOT(Case(CASE_DRSABCD) & Case(CASE_INSECT_BITE)))
    def default(self):
        # print("Error, exiting")
        pass

    pass


# Engine - End

if __name__ == "__main__":
    engine = MainEngine()
    engine.startEngine()
    pass
