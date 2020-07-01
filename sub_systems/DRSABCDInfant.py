from pyknow import *
from Data import *


# Fact - Start

class Response(Fact):
    pass


class ForeignMaterialAirway(Fact):
    pass


class Breathing(Fact):
    pass


# Fact - End

class DRSABCDInfant(KnowledgeEngine):
    @Rule(Response('1'))
    def response(self):
        instructions.append("Make comfortable, monitor response and check for injuries.")
        self.checkForForeignMaterialAirway()

    @Rule(Response('2'))
    def noResponse(self):
        instructions.append("Send for help.")
        self.checkForForeignMaterialAirway()

    @Rule(ForeignMaterialAirway('1'))
    def foreignMaterial(self):
        instructions.append("Place infant casualty face down on forearm with head supported, with mouth slightly "
                            "downward.")
        instructions.append("Clear foreign material from airway with little finger.")
        instructions.append("Once foreign material is removed, open the airway by tilting head gently into a neutral "
                            "position.")
        self.checkForBreathing()

    @Rule(ForeignMaterialAirway('2'))
    def noForeignMaterial(self):
        instructions.append("Leave casualty in the position that they have been found. Open airway by tilting head "
                            "gently into a neutral position.")
        self.checkForBreathing()

    @Rule(Breathing('1'))
    def normalBreathing(self):
        instructions.append("Place infant casualty face down on forearm with head supported, monitor breathing and "
                            "responsiveness, check for and treat any injuries.")
        self.onComplete()

    @Rule(Breathing('2'))
    def abnormalBreathing(self):
        instructions.append("Place on back on a firm surface. Keep head in neutral position and commence CPR.")
        self.performCPR()
        self.onComplete()

    def startEngine(self):
        instructions.append("Ensure the area is safe for yourself, others and the casualty")
        self.checkForResponse()

    def checkForResponse(self):
        self.reset()
        self.declare(Response(input('Does the infant show any response? \n1- Yes\n2- No\n')))
        self.run()

    def checkForForeignMaterialAirway(self):
        self.reset()
        self.declare(
            ForeignMaterialAirway(input('Is there any foreign material in the infant\'s airway? \n1- Yes\n2- No\n')))
        self.run()

    def checkForBreathing(self):
        self.reset()
        self.declare(
            Breathing(input('Check for breathing—Look and feel for chest movement, listen for air escaping from '
                            'mouth and nose (an occasional gasp is not adequate for normal breathing)\n'
                            'Is breathing normal? \n1- Normal\n2- Abnormal\n')))
        self.run()

    @staticmethod
    def performCPR():
        instructions.append(
            "Use 2 fingers (index and middle) over the lower half of the breastbone in centre of the chest.")
        instructions.append("Press down 1/3 of depth of chest and release - give 30 compressions.")
        instructions.append("Open the casualty’s airway (neutral position)")
        instructions.append("Place your mouth over the casualty’s mouth and nose to seal.")
        instructions.append("Blow gently into mouth for up to 1 second, just enough to see the chest rise and fall.")
        instructions.append("Give 2 breaths. Repeat 30:2")
        instructions.append("Aim for approximately 100-120 compressions per minute.")
        instructions.append("Continue CPR (30:2) until ambulance arrives or casualty recovers.")
        instructions.append("Obtain a defibrillator if available and follow the instructions of the 000 operator "
                            "before applying.")
