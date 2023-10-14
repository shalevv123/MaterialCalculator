def addToDict(materialDict, material, amount):
    if material not in materialDict.keys():
        materialDict[material] = amount
    else:
        materialDict[material] += amount


def combineDict(dict1, dict2):
    for key, value in dict2.items():
        addToDict(dict1, key, value)


class Material:
    complexity = 0

    def __init__(self, name, requirements=None):
        if requirements is None:
            requirements = {}
        self.name = name
        self.requirements = requirements
        self.complexity_rating = Material.complexity
        Material.complexity += 1

    def produce(self, amount):
        materialDict = {}
        for material, requirement in self.requirements.items():
            addToDict(materialDict, material, requirement * amount)
            combineDict(materialDict, material.produce(requirement * amount))
        return materialDict

    def printProduction(self, amount):
        production = self.produce(amount)
        print("To produce ", amount, " of ", self.name, " you need:")
        for material, requirement in production.items():
            print(material.name, ": ", "{:.2f}".format(requirement))


ironOre = Material("Iron Ore")
copperOre = Material("Copper Ore")
limestone = Material("Limestone")
cateriumOre = Material("Caterium Ore")
coal = Material("Coal")
oil = Material("Oil")
ironIngot = Material("Iron Ingot", {ironOre: 0.4, copperOre: 0.4})
copperIngot = Material("Copper Ingot", {copperOre: 1})
cateriumIngot = Material("Caterium Ingot", {cateriumOre: 3})
concrete = Material("Concrete", {limestone: 3})
ironPlate = Material("Iron Plate", {ironIngot: 1.5})
steelIngot = Material("Steel Ingot", {ironIngot: 0.666, coal: 0.666})
ironRod = Material("Iron Rod", {steelIngot: 0.25})
wire = Material("Wire", {cateriumIngot: 0.033, copperIngot: 0.133})
steelBeam = Material("Steel Beam", {steelIngot: 4})
screw = Material("Screw", {steelBeam: 0.019})
reinforcedIronPlate = Material("Reinforced Iron Plate", {ironPlate: 3, screw: 16.666})
copperSheet = Material("Copper Sheet", {copperIngot: 2})
plastic = Material("Plastic", {oil: 0.666})
rubber = Material("Rubber", {oil: 0.666})
cable = Material("Cable", {wire: 0.45, rubber: 0.3})
steelPipe = Material("Steel Pipe", {steelIngot: 1.5})
rotor = Material("Rotor", {ironRod: 5, screw: 25})
encasedIndustrialBeam = Material("Encased Industrial Beam", {steelBeam: 4, concrete: 5})
stator = Material("Stator", {steelPipe: 3, wire: 8})
modularFrame = Material("Modular Frame", {reinforcedIronPlate: 1.5, screw: 28})
smartPlating = Material("Smart Plating", {reinforcedIronPlate: 1, stator: 1})
motor = Material("Motor", {rotor: 2, stator: 2})
automatedWiring = Material("Automated Wiring", {stator: 1, cable: 20})
circuitBoard = Material("Circuit Board", {copperSheet: 2, plastic: 4})
computer = Material("Computer", {circuitBoard: 10, cable: 9, plastic: 18, screw: 52})
heavyModularFrame = Material("Heavy Modular Frame",
                             {modularFrame: 5, steelPipe: 15, encasedIndustrialBeam: 5, screw: 100})
versatileFramework = Material("Versatile Framework", {modularFrame: 0.5, steelBeam: 6})
modularEngine = Material("Modular Engine", {motor: 2, rubber: 15, smartPlating: 2})
adaptiveControlUnit = Material("Adaptive Control Unit",
                               {automatedWiring: 7.5, circuitBoard: 5, heavyModularFrame: 1, computer: 1})
material_dict = {
    "Iron Ore": ironOre,
    "Copper Ore": copperOre,
    "Limestone": limestone,
    "Caterium Ore": cateriumOre,
    "Coal": coal,
    "Oil": oil,
    "Iron Ingot": ironIngot,
    "Copper Ingot": copperIngot,
    "Caterium Ingot": cateriumIngot,
    "Concrete": concrete,
    "Iron Plate": ironPlate,
    "Steel Ingot": steelIngot,
    "Iron Rod": ironRod,
    "Wire": wire,
    "Steel Beam": steelBeam,
    "Screw": screw,
    "Reinforced Iron Plate": reinforcedIronPlate,
    "Copper Sheet": copperSheet,
    "Plastic": plastic,
    "Rubber": rubber,
    "Cable": cable,
    "Steel Pipe": steelPipe,
    "Rotor": rotor,
    "Encased Industrial Beam": encasedIndustrialBeam,
    "Stator": stator,
    "Modular Frame": modularFrame,
    "Smart Plating": smartPlating,
    "Motor": motor,
    "Automated Wiring": automatedWiring,
    "Circuit Board": circuitBoard,
    "Computer": computer,
    "Heavy Modular Frame": heavyModularFrame,
    "Versatile Framework": versatileFramework,
    "Modular Engine": modularEngine,
    "Adaptive Control Unit": adaptiveControlUnit
}
