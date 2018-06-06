import csv
import os

# Constants
directory = "../tmy_data/" # The file used later is just the tail of the path (i.e. file name only) Need to add this to give full path
tmy_mapping = [] # Empty array to put our final station_ID, Lat, Lon points into
output_file = "extracted.txt" # A text file in the root folder to which the extracted data will be written
csv_columns = ['Station_ID', 'Station_Name', 'State', 'Time_Zone', 'Lat', 'Lon', 'Elevation']

# Function that takes a csv file and iterates 1 time to read the first row and appends the needed data to a list
def get_head(csv_file):
	with open(csv_file, "rt") as f:
		# Read in the first line, split it on end line character, then split the first element on the comma
		head = f.readline().split('/n')[0].split(',')
	# Set up a blank string to populate for each station
	output_string = ""
	for i in range(0, len(head)):
		output_string += head[i] + ","
	output_string = output_string[:-1]
	return output_string

# Loop that walks the data folder and grabs files one at a time, and calls the get_head function on each file 
for roots, dirs, files in os.walk(directory):
	for file in files:
		full_path = directory + file
		tmy_mapping.append(get_head(full_path))


with open(output_file, "w") as f:
	# Write the column headers in as the first row of the file
	mywriter = csv.writer(f)
	mywriter.writerow(csv_columns)
	# Write the extracted station data in as the subsequent rows of the file
	for line in tmy_mapping:
		f.write("%s\n" % line) #This writes the line followed by a new line escape slash