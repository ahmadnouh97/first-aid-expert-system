from pyknow import *
from Data import *
from sub_systems.DRSABCD import DRSABCD


# Fact - Start

class DownedPowerLine(Fact):
    pass


class VehicleTouchedByCable(Fact):
    pass


# Fact - End
class ElectricShock(KnowledgeEngine):
    @Rule(DownedPowerLine('yes'))
    def downedPowerLine(self):
        instructions.append('When calling Triple Zero (000) advise that there are downed cables.')
        instructions.append(
            'Remain at least 6 metres from any cable and do not approach until advised that it is safe to do so.')
        instructions.append('DO NOT attempt to remove the cable.')
        self.checkIfVehicleTouchedByCable()

    @Rule(DownedPowerLine('no'))
    def notDownedPowerLine(self):
        self.onComplete()

    @Rule(VehicleTouchedByCable('yes'))
    def vehicleTouchedByCable(self):
        instructions.append('DO NOT go near the vehicle or try to remove the casualty from the vehicle.')
        instructions.append('Advise the casualty not to move.')
        self.onComplete()

    @Rule(VehicleTouchedByCable('no'))
    def vehicleNotTouchedByCable(self):
        instructions.append('Advise the casualty not to move.')
        self.onComplete()

    def startEngine(self):
        subEngine = DRSABCD()
        subEngine.onComplete = self.initEngine
        subEngine.startEngine()

    def initEngine(self):
        instructions.append('Check for danger to yourself and bystanders.')
        instructions.append('Switch off the power if possible.')
        instructions.append('If safe to do so, remove the casualty from the electrical supply without directly '
                            'touching them. Use non-conductive, dry materials, for example a dry wooden broom handle.')
        instructions.append('Cool any burnt areas with copious amounts of cool water for up to twenty (20) minutes.')
        instructions.append('Remove any clothing and jewellery from affected area unless stuck to the burn.')
        instructions.append('Cover burnt area with a light non-stick dressing or clean, dry non-fluffy material.')
        instructions.append('Reassure the casualty.')
        instructions.append('Always seek medical aid immediately for electrical burns. call the ambulance.')
        self.checkIfDownedPowerLine()

    def checkIfDownedPowerLine(self):
        self.reset()
        self.declare(DownedPowerLine(input('Was the (DOWNED POWER LINES) the reason of the shock? (yes / no)')))
        self.run()

    def checkIfVehicleTouchedByCable(self):
        self.reset()
        self.declare(VehicleTouchedByCable(input('Is the vehicle touched by high voltage cable ? (yes / no)')))
        self.run()
