from sub_engines.CasualtiesEngine import *
from sub_engines.SymptomsEngine import *
from pyknow import *


class Method(Fact):
    pass


class MainEngine(KnowledgeEngine):
    @Rule(Method('1'))
    def startCasualtiesEngine(self):
        engine = CasualtiesEngine()
        engine.startEngine()

    @Rule(Method('2'))
    def startSymptomsEngine(self):
        engine = SymptomsEngine()
        engine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Method(input('Please choose one of the 2 options:\n'
                                  '1- Casualties.\n'
                                  '2- Symptoms.\n'
                                  '(Enter 1 or 2): ')))
        self.run()


if __name__ == "__main__":
    engine = MainEngine()
    engine.startEngine()
