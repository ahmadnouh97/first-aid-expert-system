from sub_systems.DRSABCD import *
from sub_systems.InsectBite import *
from sub_systems.AsthmaAttack import *
from sub_systems.BlueRingedBites import *
from sub_systems.MarineStings import *
from sub_systems.NonTropicalJellyfishStings import *
from sub_systems.Burns import *
from Data import *

# Facts - Start

CASE_DRSABCD = "DRSABCD"
CASE_INSECT_BITE = "Insect Bite"
CASE_MARINE_STING = "Marine Sting"
CASE_NONE_TROPICAL_JELLYFISH_STINGS = "Non-Tropical Jellyfish Stings"
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
    def startInsectBite(self):
        engine = MarineStings()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("4"))
    def startInsectBite(self):
        engine = NonTropicalJellyfishStings()
        engine.onComplete = onComplete
        engine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Case(input(f"Choose case: (1- {CASE_DRSABCD},"
                                f" 2- {CASE_INSECT_BITE},"
                                f" 3- {CASE_MARINE_STING},"
                                f" 4- {CASE_NONE_TROPICAL_JELLYFISH_STINGS})\n")))
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
