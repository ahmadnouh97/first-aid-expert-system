from DRSABCD import *
from Data import *

# Facts - Start

CASE_DRSABCD = "DRSABCD"


# Facts - End

class Case(Fact):
    pass


def onComplete():
    printInstructions()


# Engine - Start

class MainEngine(KnowledgeEngine):

    @Rule(Case(CASE_DRSABCD))
    def startDRSABCD(self):
        subEngine = DRSABCD()
        subEngine.onComplete = onComplete
        subEngine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Case(input(f"Choose case: ({CASE_DRSABCD})\n")))
        self.run()

    @Rule(NOT(Case(CASE_DRSABCD)))
    def default(self):
        print("Error, exiting")

    pass


# Engine - End

if __name__ == "__main__":
    engine = MainEngine()
    engine.startEngine()
    pass
