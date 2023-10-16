def addToDict(materialDict, material, amount):
    if material not in materialDict.keys():
        materialDict[material] = amount
    else:
        materialDict[material] += amount


def combineDict(dict1, dict2):
    for key, value in dict2.items():
        addToDict(dict1, key, value)

def receipeToText(recipe):
    text = ""
    for material, amount in recipe.items():
        text += material + "  X " + str(amount) + "\n"
    return text

class Material:
    complexity = 0

    def __init__(self, names, requirements=None, *, default_recipe=0):
        if requirements is None:
            requirements = [{}]
        self.names = names
        self.requirements = requirements
        self.recipe = default_recipe
        self.complexity_rating = Material.complexity
        Material.complexity += 1

    def produce(self, amount):
        materialDict = {}
        for material, requirement in self.requirements[self.recipe].items():
            addToDict(materialDict, material, requirement * amount)
            combineDict(materialDict, material.produce(requirement * amount))
        return materialDict

    def printProduction(self, amount):
        production = self.produce(amount)
        print("To produce ", amount, " of ", self.names[self.recipe], " you need:")
        for material, requirement in production.items():
            print(material.name, ": ", "{:.2f}".format(requirement))


ironOre = Material(["Iron Ore"])
copperOre = Material(["Copper Ore"])
limestone = Material(["Limestone"])
cateriumOre = Material(["Caterium Ore"])
coal = Material(["Coal"])
oil = Material(["Oil"])
ironIngot = Material(["Iron Ingot", "Iron Alloy ingot"], [{ironOre: 1}, {ironOre: 0.4, copperOre: 0.4}], default_recipe=1)
copperIngot = Material(["Copper Ingot"], [{copperOre: 1}])
cateriumIngot = Material(["Caterium Ingot"], [{cateriumOre: 3}])
concrete = Material(["Concrete"], [{limestone: 3}])
ironPlate = Material(["Iron Plate"], [{ironIngot: 1.5}])
steelIngot = Material(["Steel Ingot", "Solid Steel Ingot"], [{ironOre: 1, coal: 1}, {ironIngot: 0.666, coal: 0.666}], default_recipe=1)
ironRod = Material(["Iron Rod", "Steel Rod"], [{ironOre: 1}, {steelIngot: 0.25}], default_recipe=1)
wire = Material(["Wire", "Fused Wire"], [{copperIngot: 0.5},{cateriumIngot: 0.033, copperIngot: 0.133}], default_recipe=1)
quickwire = Material(["Quickwire"], [{cateriumIngot: 0.2}])
steelBeam = Material(["Steel Beam"], [{steelIngot: 4}])
screw = Material(["Screw", "Cast Screw", "Steel Screw"], [{ironRod: 0.25}, {ironIngot: 0.25}, {steelBeam: 0.019}], default_recipe=2)
reinforcedIronPlate = Material(["Reinforced Iron Plate", "Stitched Iron Plate", "Bolted Iron Plate"],
                               [{ironPlate: 6, screw: 12}, {ironPlate: 3.333, wire: 6.666 }, {ironPlate: 6, screw: 16.666}], default_recipe=2)
copperSheet = Material(["Copper Sheet"], [{copperIngot: 2}])
plastic = Material(["Plastic"], [{oil: 1.5}])
rubber = Material(["Rubber"], [{oil: 1.5}])
cable = Material(["Cable", "Insulated Cable"], [{wire: 2}, {wire: 0.45, rubber: 0.3}], default_recipe=1)
steelPipe = Material(["Steel Pipe"], [{steelIngot: 1.5}])
rotor = Material(["Rotor"], [{ironRod: 5, screw: 25}])
encasedIndustrialBeam = Material(["Encased Industrial Beam"], [{steelBeam: 4, concrete: 5}])
stator = Material(["Stator", "Quickwire Stator"], [{steelPipe: 3, wire: 8}, {steelPipe: 2, quickwire: 7.5}], default_recipe=1)
modularFrame = Material(["Modular Frame", "Bolted Frame"], [{reinforcedIronPlate: 1.5, ironRod: 6}, {reinforcedIronPlate: 1.5, screw: 28}], default_recipe=1)
smartPlating = Material(["Smart Plating"], [{reinforcedIronPlate: 1, stator: 1}])
motor = Material(["Motor"], [{rotor: 2, stator: 2}])
automatedWiring = Material(["Automated Wiring"], [{stator: 1, cable: 20}])
circuitBoard = Material(["Circuit Board"], [{copperSheet: 2, plastic: 4}])
computer = Material(["Computer"], [{circuitBoard: 10, cable: 9, plastic: 18, screw: 52}])
heavyModularFrame = Material(["Heavy Modular Frame"], [{modularFrame: 5, steelPipe: 15, encasedIndustrialBeam: 5, screw: 100}])
versatileFramework = Material(["Versatile Framework"], [{modularFrame: 0.5, steelBeam: 6}])
modularEngine = Material(["Modular Engine"], [{motor: 2, rubber: 15, smartPlating: 2}])
adaptiveControlUnit = Material(["Adaptive Control Unit"], [{automatedWiring: 7.5, circuitBoard: 5, heavyModularFrame: 1, computer: 1}])
material_list = [
    ironOre,
    copperOre,
    limestone,
    cateriumOre,
    coal,
    oil,
    ironIngot,
    copperIngot,
    cateriumIngot,
    concrete,
    ironPlate,
    steelIngot,
    ironRod,
    wire,
    quickwire,
    steelBeam,
    screw,
    reinforcedIronPlate,
    copperSheet,
    plastic,
    rubber,
    cable,
    steelPipe,
    rotor,
    encasedIndustrialBeam,
    stator,
    modularFrame,
    smartPlating,
    motor,
    automatedWiring,
    circuitBoard,
    computer,
    heavyModularFrame,
    versatileFramework,
    modularEngine,
    adaptiveControlUnit
]
name_to_item_dict = {}

for item in material_list:
    for i, name in enumerate(item.names):
        name_to_item_dict[name] = (item, i)
