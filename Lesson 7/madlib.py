# initialize dictionary with keys whose values will be populated by user input.
Madlib = {
    'noun':'',
    '~exotic~ noun':'',
    'name':'',
    'number greater than 1':'',
    'adjective':'',
    'intangible noun':'',
    'verb': '',

}

# Loop through dict keys to solicit user input
for key in Madlib.keys():
  # Populate values to associated key
  Madlib[key] = input(f'Please enter a/n {key}: ').strip() 

# Output Madlib with input values
print(f'\nHere\'s your Madlib: \nIt all started when our flying {Madlib["noun"]} crash-landed on Planet {Madlib["~exotic~ noun"].capitalize()}. \nMy best buddy {Madlib["name"].capitalize()} and I were trapped with no way to get back.\nIn our search, we came across {Madlib["number greater than 1"]} aliens, who were very {Madlib["adjective"]}. We asked them for {Madlib["intangible noun"]} to get back.\nFortunately, they were very accommodating and were very eager to {Madlib["verb"]}.\nWith the aliens\' help, {Madlib["name"].capitalize()} and I left Planet {Madlib["~exotic~ noun"].capitalize()} and returned home.')