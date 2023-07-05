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
target_found = False

# Loop through each line of the databse file
print("Looking for ["+target_object+"]...")
for i in range(0, len(line_array)):
    line = line_array[i]

    # Check if the current line in the loop matches our target
    if line.strip() == target_object:
        # If it does - output the next two lines to a new file
        target_found = True
        with open("./"+target_object+"_TLE.txt", 'w') as output_file:
            output_file.write(
                line_array[i+1]+"\n"
                +line_array[i+2]
            )


        print("["+target_object+"] found")
        print("File "+target_object+"_TLE.txt created")
        break

if not target_found:
    raise Exception("No object ["+target_object+"] found in database")