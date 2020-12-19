--shared.lua

--the dictionary that contains the list of entities (as keys) and their respective define.inventory (as the value)
entityInventoryToSort =
{
	["car"] = defines.inventory.car_trunk,
	["cargo-wagon"] = defines.inventory.cargo_wagon,
	["container"] = defines.inventory.chest,
	["logistic-container"] = defines.inventory.chest,
	["roboport"] = {defines.inventory.roboport_robot, defines.inventory.roboport_material},
	["spider-vehicle"] = defines.inventory.spider_trunk
}