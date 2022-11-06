import csv
list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
print(len(list_data))
single_state = [state for state in list_data if state['STATE']== "NEW_JERSEY"]
#print(single_state)
print(len(single_state))

# I want to analyize fed revenue vs. grades_pk in new jersey
#filter out rows without data for federal revenue
new_info=[row for row in single_state if row['FEDERAL_REVENUE']!='']