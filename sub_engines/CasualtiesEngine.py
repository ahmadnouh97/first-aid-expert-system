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
from sub_systems.AsthmaAttack import *
from sub_systems.BlueRingedBites import *
from sub_systems.ColdInducedCondition import *
from sub_systems.DiabetesInducedEmergency import *
from sub_systems.Burns import *
from sub_systems.Dislocation import *
from sub_systems.ElectricShock import *
from sub_systems.EyeInjuries import *
from sub_systems.Chocking import *
from sub_systems.Fractures import *
from sub_systems.HeartAttack import *
from sub_systems.HeadInjuries import *
from sub_systems.HeatInducedConditions import *
from Data import *

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
CASE_ASTHMA_ATTACK = "Asthma Attack"
CASE_BLUE_RINGED_BITES = "Blue Ringed Bites"
CASE_BURNS = "Burns and Scalds"

CASE_HEART_ATTACK = "Heart Attack"
CASE_COLD_INDUCED_CONDITION = "Cold Induced Condition"
CASE_HEAT_INDUCED_CONDITIONS = "Heat Induced Conditions"
CASE_DIABETES_INDUCED_EMERGENCY = "Diabetes Induced Emergency"
CASE_DISLOCATION = "Dislocation"
CASE_ELECTRIC_SHOCK = "Electric Shock"
CASE_EYE_INJURIES = "Eye Injuries"
CASE_CHOCKING = "Chocking"
CASE_FRACTURES = "Fractures"
CASE_HEAD_INJURIES = "Head Injuries"


# Facts - End

class Case(Fact):
    pass


def onComplete():
    printInstructions()


# Engine - Start

class CasualtiesEngine(KnowledgeEngine):

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
    def startSprainsAndStrains(self):
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

    @Rule(Case("16"))
    def startDisLocation(self):
        engine = Dislocation()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("17"))
    def startElectricShock(self):
        engine = ElectricShock()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("18"))
    def startEyeInjuries(self):
        engine = EyeInjuries()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("19"))
    def startChocking(self):
        engine = Chocking()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("20"))
    def startFractures(self):
        engine = Fractures()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("21"))
    def startHeartAttack(self):
        engine = HeartAttack()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("22"))
    def startHeadInjuries(self):
        engine = HeadInjuries()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("23"))
    def startHeatInducedConditions(self):
        engine = HeatInducedConditions()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("24"))
    def startColdInducedCondition(self):
        engine = ColdInducedCondition()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("25"))
    def startBlueRingedBites(self):
        engine = BlueRingedBites()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("26"))
    def startAsthmaAttack(self):
        engine = AsthmaAttack()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("27"))
    def startDiabetesInducedEmergency(self):
        engine = DiabetesInducedEmergency()
        engine.onComplete = onComplete
        engine.startEngine()

    @Rule(Case("28"))
    def startBurns(self):
        engine = Burns()
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
                                f" 15- {CASE_TROPICAL_JELLYFISH_STINGS},"
                                f" 16- {CASE_DISLOCATION},"
                                f" 17- {CASE_ELECTRIC_SHOCK},"
                                f" 18- {CASE_EYE_INJURIES},"
                                f" 19- {CASE_CHOCKING},"
                                f" 20- {CASE_FRACTURES},"
                                f" 21- {CASE_HEART_ATTACK},"
                                f" 22- {CASE_HEAD_INJURIES},"
                                f" 23- {CASE_HEAT_INDUCED_CONDITIONS},"
                                f" 24- {CASE_COLD_INDUCED_CONDITION},"
                                f" 25- {CASE_BLUE_RINGED_BITES},"
                                f" 26- {CASE_ASTHMA_ATTACK},"
                                f" 27- {CASE_DIABETES_INDUCED_EMERGENCY},"
                                f" 28- {CASE_BURNS}\")\n")))
        self.run()

    @Rule(NOT(Case(CASE_DRSABCD) & Case(CASE_INSECT_BITE)))
    def default(self):
        # print("Error, exiting")
        pass

# Engine - End
