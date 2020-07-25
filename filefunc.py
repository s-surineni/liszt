#!/usr/bin/env python3
# Created on July 24, 2020. remember-file.py
# contains the functions for adding and removing
# files for the Quick Note software

import sys
import os.path
from os import path

# Given a filename, adds a dot file with
# the given name, which will then be set 
# as the default file for memories
def add_file(filename):
	if path.isfile(filename):
		print('A note with this name already exists. Please choose a different name, delete the other note, or rename the other note.')
		return;
	else:
		open(filename, 'w+')	
