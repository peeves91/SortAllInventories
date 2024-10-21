import json
import os
import shutil

MOD_NAME	= "Sort-All-Inventories"

if __name__ == '__main__':
	# get the version of the mod
	with open('info.json', 'r') as file:
		infoData = json.load(file)
		version = infoData['version']
	
	# fetch the mod name
	modName = f'{MOD_NAME}_{version}'
	modTempRootPath = os.path.join('/tmp', modName)
	modTempSrcPath = os.path.join(modTempRootPath, modName)
	
	# create a temp directory of the files
	if os.path.exists(modTempRootPath) == True:
		shutil.rmtree(modTempRootPath)
	
	os.mkdir(modTempRootPath)
	
	# copy files to the src directory of the root temp path
	shutil.copytree(src=os.getcwd(), dst=modTempSrcPath, ignore=shutil.ignore_patterns('*.py', '*.git'))
	
	# create zip of mod
	shutil.make_archive(base_name=modName, format='zip', root_dir=modTempRootPath)