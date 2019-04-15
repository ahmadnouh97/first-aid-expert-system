from sub_systems.InsectBite import *
from sub_systems.MarineStings import *
from sub_systems.NonTropicalJellyfishStings import *
from sub_systems.Poisoning import *
from sub_systems.SeizuresAndEpilepsy import *
from sub_systems.SevereAllergicReaction import *
from sub_systems.SevereBleeding import *
from sub_systems.RedBackSpiderBite import *
from sub_systems.Shock import *
from sub_systems.SnakeBite import *
from sub_systems.SpinalInjury import *
from sub_systems.SprainsAndStrains import *
from sub_systems.Stroke import *
from sub_systems.TropicalJellyfishStings import *

# Facts - Start

CASE_DRSABCD = "DRSABCD"
CASE_INSECT_BITE = "Insect Bite"
CASE_MARINE_STING = "Marine Sting"
CASE_NONE_TROPICAL_JELLYFISH_STINGS = "Non-Tropical Jellyfish Stings"
CASE_POISONING = "Poisoning"
CASE_RED_BACK_SPIDER_BITE = "Red-Back Spider Bite"
CASE_SEIZURES_AND_EPILEPSY = "Seizures And Epilepsy"
CASE_SEVERE_ALLERGIC_REACTION = "Severe Allergic Reaction"
CASE_SEVERE_BLEEDING = "Severe Bleeding"
CASE_SHOCK = "Shock"
CASE_SNAKE_BITE = "Snake Bite"
CASE_SPINAL_INJURY = "Spinal Injury"
CASE_SPRAINS_AND_STRAINS = "Sprains And Strains"
CASE_STROKE = "Stroke"
CASE_TROPICAL_JELLYFISH_STINGS = "Tropical Jellyfish Stings"
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
    def startMarineStings(self):
        engine = MarineStings()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("4"))
    def startNonTropicalJellyfishStings(self):
        engine = NonTropicalJellyfishStings()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("5"))
    def startPoisoning(self):
        engine = Poisoning()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("6"))
    def startRedBackSpiderBite(self):
        engine = RedBackSpiderBite()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("7"))
    def startSeizuresAndEpilepsy(self):
        engine = SeizuresAndEpilepsy()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("8"))
    def startSevereAllergicReaction(self):
        engine = SevereAllergicReaction()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("9"))
    def startSevereBleeding(self):
        engine = SevereBleeding()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("10"))
    def startShock(self):
        engine = Shock()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("11"))
    def startSnakeBite(self):
        engine = SnakeBite()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("12"))
    def startSpinalInjury(self):
        engine = SpinalInjury()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("13"))
    def startSpinalInjury(self):
        engine = SprainsAndStrains()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("14"))
    def startStroke(self):
        engine = Stroke()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("15"))
    def startTropicalJellyfishStings(self):
        engine = TropicalJellyfishStings()
        engine.onComplete = onComplete
        engine.startEngine()

    def startEngine(self):
        self.reset()
        self.declare(Case(input(f"Choose case: (1- {CASE_DRSABCD},"
                                f" 2- {CASE_INSECT_BITE},"
                                f" 3- {CASE_MARINE_STING},"
                                f" 4- {CASE_NONE_TROPICAL_JELLYFISH_STINGS},\n"
                                f" 5- {CASE_POISONING},"
                                f" 6- {CASE_RED_BACK_SPIDER_BITE},"
                                f" 7- {CASE_SEIZURES_AND_EPILEPSY},"
                                f" 8- {CASE_SEVERE_ALLERGIC_REACTION},"
                                f" 9- {CASE_SEVERE_BLEEDING},"
                                f" 10- {CASE_SHOCK},\n"
                                f" 11- {CASE_SNAKE_BITE},"
                                f" 12- {CASE_SPINAL_INJURY},"
                                f" 13- {CASE_SPRAINS_AND_STRAINS},"
                                f" 14- {CASE_STROKE},"
                                f" 15- {CASE_TROPICAL_JELLYFISH_STINGS})\n")))
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
