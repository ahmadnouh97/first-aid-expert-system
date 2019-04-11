from sub_systems.DRSABCD import *
from sub_systems.InsectBite import *
from Data import *

# Facts - Start

CASE_DRSABCD = "DRSABCD"
CASE_INSECT_BITE = "Insect Bite"


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
