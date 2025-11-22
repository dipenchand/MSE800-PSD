# Initialized dataTypes dictionary variable with values
dataTypes = {
    "Name": {
        "Data_Type": "String",
        "value": "John Doe",
    },
    "Age": {
        "Data_Type": "Integer",
        "value": 28,
    },
    "Skills": {
        "Data_Type": "List",
        "value": ["Python", "SQL", "Power BI"],
    },
    "Education": {
        "Data_Type": "Tuple",
        "value": ("BSc Computer Science", 2020),
    },
    "Contact Details": {
        "Data_Type": "Dictionary",
        "value": {"email": "personaldipen@gmail.com", "phone": "027 437 2485"},
    },
    "Certifications": {
        "Data_Type": "Set",
        "value": {"Azure", "AWS", "Azure"},
    }
}

# Print header with spaces
print(f"{'Component':<15} {'|':<5} {'Data Type':<10} {'|':<5} {'Example':<10}")
# Separated header with hyphen with length of 75 characters
print("-" * 75)

# looping through the dataTypes dictionary
for key, values in dataTypes.items():
    # print the key value inside the table body
    print(f"{key:<20} {values['Data_Type']:<17} {values['value']}")
