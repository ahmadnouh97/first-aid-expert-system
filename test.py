from pyknow import *


# Facts
class Response(Fact):
    pass


class ForeignMaterialAirway(Fact):
    pass


class Breathing(Fact):
    pass


# End - Facts

# Engine - Start
class DRSABCD(KnowledgeEngine):
    @Rule(Response('yes'))
    def response(self):
        instructions.append("Make comfortable, monitor response and check for injuries.")
        checkForForeignMaterialAirway()

    @Rule(Response('no'))
    def noResponse(self):
        instructions.append("Send for help.")
        checkForForeignMaterialAirway()

    @Rule(ForeignMaterialAirway('yes'))
    def foreignMaterial(self):
        instructions.append("Place casualty in recovery position with mouth slightly downward.")
        instructions.append("Clear foreign material from airway with fingers.")
        instructions.append("Once foreign material is removed, open the airway with a head tilt and chin lift (adult) "
                            "and slight head tilt and chin lift (child).")
        checkForBreathing()

    @Rule(ForeignMaterialAirway('no'))
    def noForeignMaterial(self):
        instructions.append("Leave casualty in the position which they have been found. Open airway by tilting head "
                            "with chin lift (adult) and slight head tilt and chin lift (child).")
        checkForBreathing()

    @Rule(Breathing('normal'))
    def normalBreathing(self):
        print("Here")
        instructions.append("Place in recovery position, monitor breathing and responsiveness.")
        printInstructions()

    @Rule(Breathing('abnormal'))
    def abnormalBreathing(self):
        print("Here")
        instructions.append("Place on back and commence CPR.")
        performCPR()
        printInstructions()

    pass


# Engine - End

instructions = []

engine = DRSABCD()


# Functions - Start

def startEngine():
    instructions.append("Ensure the area is safe for yourself, others and the casualty")
    checkForResponse()


def checkForResponse():
    engine.reset()
    engine.declare(Response(input('Does the casualty show any response? (yes / no)')))
    engine.run()


def checkForForeignMaterialAirway():
    engine.reset()
    engine.declare(ForeignMaterialAirway(input('Is there any foreign material in the casualty\'s airway? (yes / no)')))
    engine.run()


def checkForBreathing():
    engine.reset()
    engine.declare(Breathing(input('Check for breathing—Look and feel for chest movement, listen for air escaping from '
                                   'mouth and nose (an occasional gasp is not adequate for normal breathing)\n'
                                   'Is breathing normal? (normal / abnormal)')))
    engine.run()


def performCPR():
    instructions.append("Place the heel of hand on the lower half of the breastbone in centre of the chest with other "
                        "hand on top of first.")
    instructions.append("Press down 1/3 of depth of chest and release, giving 30 compressions.")
    instructions.append("Open the casualty’s airway (head tilt and chin lift).")
    instructions.append("Pinch the soft part of the nose to seal and place your mouth over the casualty’s mouth.")
    instructions.append("Blow steadily into mouth for up to 1 second, watch for chest to rise and fall.")
    instructions.append("Give 2 breaths - Repeat 30:2.")
    instructions.append("Aim for approximately 100-120 compressions per minute.")
    instructions.append("Continue CPR (30:2) until ambulance arrives or casualty recovers.")
    instructions.append("Apply defibrillator as soon as possible (if available) and follow voice prompts.")


def printInstructions():
    for inst in instructions:
        print('- ' + inst + '\n')


# Functions - End

# Run - Start

startEngine()

# Run - End
