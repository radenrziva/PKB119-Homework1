def init_data():
    data = [
        {
            'leaf_width': 2.7,
            'leaf_length': 4.9,
        },
        {
            'leaf_width': 3.2,
            'leaf_length': 5.5,
        },
        {
            'leaf_width': 2.9,
            'leaf_length': 5.1,
        },
        {
            'leaf_width': 3.4,
            'leaf_length': 6.8,
        },
    ]

    return data

def predicted_species(data):
    leaf_width = data.get('leaf_width', 0.0)  # Default to 0.0 if 'leaf_width' is missing
    leaf_length = data.get('leaf_length', 0.0)  # Default to 0.0 if 'leaf_length' is missing

    if (leaf_width > 3.0 and leaf_length > 5.1):
        return 'big-leaf'
    else:
        return 'small-leaf'
    
def predicted_species_new(data):
    leaf_width = data.get('leaf_width', 0.0)  # Default to 0.0 if 'leaf_width' is missing
    leaf_length = data.get('leaf_length', 0.0)  # Default to 0.0 if 'leaf_length' is missing
    thickness = data.get('thickness', 1.0)  # Default to 1.0 if 'thickness' is missing

    if (leaf_width > 3.0 and leaf_length > 5.1 and thickness < 2):
        return 'big-leaf'
    elif (leaf_width > 3.0 and leaf_length > 5.0 and thickness >= 2):
        return 'thick-leaf'
    else:
        return 'small-leaf'

def main():
    data = init_data()

    print("The provided leaf dataset and their species:")
    for entry in data:
        entry['species'] = predicted_species(entry)

    for entry in data:
        leaf_width = entry.get('leaf_width', 'N/A')  # Handle cases where 'leaf_width' is missing
        leaf_length = entry.get('leaf_length', 'N/A')  # Handle cases where 'leaf_length' is missing
        print(f"leaf_width: {leaf_width}, leaf_length: {leaf_length}, Species: {entry['species']}")

    # 1. Predict species of a new sample
    new_data = {
        'leaf_width': 3.0,
        'leaf_length': 5.6,
    }
    data.append(new_data)
    new_entry = data[-1]
    new_entry['species'] = predicted_species(new_entry)

    print("\n1. Predict species of a new sample:")
    print(f"leaf_width: {new_entry.get('leaf_width', 'N/A')}, leaf_length: {new_entry.get('leaf_length', 'N/A')}, Species: {new_entry['species']}")

    # 2. Predict species of a new sample without leaf_length column
    new_data2 = {
        'leaf_width': 3.4,
    }
    data.append(new_data2)
    new_entry = data[-1]
    new_entry['species'] = predicted_species(new_entry)

    print("\n2. Predict species of a new sample without leaf_length column:")
    print(f"leaf_width: {new_entry.get('leaf_width', 'N/A')}, leaf_length: {new_entry.get('leaf_length', 'N/A')}, Species: {new_entry['species']}")

    # 3. Predict species of a new sample with an additional column
    new_data3 = {
        'leaf_width': 2.5,
        'leaf_length': 9.5,
        'thickness': 1.1,
    }
    data.append(new_data3)
    new_entry = data[-1]
    new_entry['species'] = predicted_species_new(new_entry)

    print("\n3. Predict species of a new sample with an additional column:")
    print(f"leaf_width: {new_entry.get('leaf_width')}, leaf_length: {new_entry.get('leaf_length')}, Thickness: {new_entry['thickness']}, Species: {new_entry['species']}")

    # 4. Predict species of a new sample with a new species category
    new_species_data = {
        'leaf_width': 3.1,
        'leaf_length': 5.4,
        'thickness': 2.1,
    }
    data.append(new_species_data)
    new_entry = data[-1]
    new_entry['species'] = predicted_species_new(new_entry)

    print("\n4. Predict species of a new sample with a new species category:")
    print(f"leaf_width: {new_entry.get('leaf_width', 'N/A')}, leaf_length: {new_entry.get('leaf_length', 'N/A')}, Thickness: {new_entry['thickness']}, Species: {new_entry['species']}")

if __name__ == "__main__":
    main()
