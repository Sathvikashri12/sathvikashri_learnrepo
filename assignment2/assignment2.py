import json

# Read the JSON data from the file
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Find the specific donut with the name "Old Fashioned"
for item in ex5:
    if item['name'] == 'Old Fashioned':
        # Add a new batter named "Coffee"
        item['batters']['batter'].append({'id': '1005', 'type': 'Coffee'})
        break

# Write the updated data back to the JSON file
with open('ex5.json', 'w') as file:
    json.dump(ex5, file)
