import csv
import os
from pprint import pprint

# Constants
directory = "../Data/Raw_Data/" # The file used later is just the tail of the path (i.e. file name only) Need to add this to give full path
tmy_mapping = [] # Empty array to put our final station_ID, Lat, Lon points into
output_file = "extracted.txt" # A text file in the root folder to which the extracted data will be written

# Function that takes a csv file and iterates 1 time to read the first row and appends the needed data to a list
def get_head(csv_file):
	head = []
	with open(csv_file, "rt") as f:
		for i in range(0, 1):
			for i in csv.reader(f):
				head.append(i)
				break
	return head[0][0] + "," + head[0][4] + "," + head[0][5]

# Loop that walks the data folder and grabs files one at a time, and calls the get_head function on each file 
for roots, dirs, files in os.walk(directory):
	for file in files:
		full_path = directory + file
		tmy_mapping.append(get_head(full_path))

# pprint(tmy_mapping)


with open(output_file, "w") as f:
	# Write the column headers in as the first row of the file
	mywriter = csv.writer(f)
	mywriter.writerow(csv_columns)
	# Write the extracted station data in as the subsequent rows of the file
	for line in tmy_mapping:
		f.write("%s\n" % line) #This writes the line followed by a new line escape slash
