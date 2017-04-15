import re, sys
import os.path

# Obtain a file to parse
inputFile = file(os.pathS3_Test.map)

# Parse the file
for line in inputFile:
	# DO STUFF
	match = re.search(r"\.bss", line)
	if match:
		print(line)

# Close the file
inputFile.close()

