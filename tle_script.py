# This script scrapes the NORAD database for a given object and creates a TLE file for it.

import urllib.request

target_object = "M6P"
database_url =  "https://celestrak.org/NORAD/elements/active.txt"

# Get the entire database of elements
print("Getting database...")
web_request = urllib.request.urlopen(database_url)
all_lines = web_request.read().decode()

# Set initial variables for loop
line_array = all_lines.splitlines()
output_lines = []
output_content = []

# Loop through each line of 
print("Looking for ["+target_object+"]...")
for i in range(0, len(line_array)):
    line = line_array[i]

    # Check if the current line in the loop matches our target
    if line.strip() == target_object:
        # If it does - set the next two lines as the contents of resulting TLEs
        output_content = [
            line_array[i+1],
            line_array[i+2]
        ]
        print("["+target_object+"] found")
        break



if len(output_content) == 0:
    # create an error if we don't find what we look for
    raise "No object ["+target_object+"] found in database"
else:
    # Output the TLE file to the script's directory
    with open("./"+target_object+"_TLE.txt", 'w') as output_file:
        for line in output_content:
            output_file.write(line)
            # only add newline after the first line
            if line == output_content[0]:
                output_file.write("\n")

    print("File "+target_object+"_TLE.txt created")


        

