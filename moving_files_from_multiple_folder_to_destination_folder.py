import shutil
import os

source = '/source/file/address'
dest1 = 'destination/file/address'


files = os.listdir(source)

for f in files:
	for ff in os.listdir(source+f):
		shutil.move(source+f+'/'+ff, dest1)
