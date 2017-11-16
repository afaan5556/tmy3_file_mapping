# tmy3_file_mapping
This Python script extracts station ID and lat-lon coordinates from TMY3 files.

## Variables
* `directory` is the head (excluding file name, which is the tail) of the path to your TMY3 files
* `tmy_mapping` is an empty list which will be popoulated line by line with staion ID's and lat-lon coordinates
* `output_file` is a variable that points to a pre-gnereated blank text file (in this case called "mapped.txt") to which the extracted Station ID and lat-lon coordinates will be written

## Use
Place the script in a folder relative to where you have the TMY3 data files and check the `directory` variable to make sure the relative path from the script to the files is correct.

Running the script should populate the "mapped.txt" file with the Station ID and lat-lon pairs for each of your TMY3 files as a new line.
