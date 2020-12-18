from pathlib import Path
import os
import shutil
import stat

if __name__ == '__main__':
	# fetch the mod name
	modName = os.getcwd().split('\\')[-1]
	os.chdir('../')
	
	# create a 
	os.mkdir('temp')
	shutil.copytree(modName, os.getcwd() + '\\temp\\' + modName, ignore = shutil.ignore_patterns('*.py', '.git'))
	
	# create zip of mod
	shutil.make_archive(modName, 'zip', 'temp')
	
	# remove temp directory
	shutil.rmtree('temp')
	
	# copy mod to factorio directory
	factorioModDirectory = os.getenv('APPDATA') + '\\' + 'Factorio\Mods'
	shutil.copy(modName + '.zip', factorioModDirectory)