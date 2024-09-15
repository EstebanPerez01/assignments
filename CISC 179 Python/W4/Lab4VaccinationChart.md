# Lab 4 Vaccination Charts

```python
# Nested Dictionary for Patient Records
patients = {}

# Function to insert new patient record into nested dictionary
def insert(recordNumber, firstName, lastName, vaccines):
    # Check if the record number already exists
    if recordNumber in patients:
        print(f"Record number {recordNumber} already exists.")
    else:
        patients[recordNumber] = {
            "name": {
                "first_name": firstName,
                "last_name": lastName,
            },
            "vaccinations": vaccines
        }
    print(f"Record {recordNumber} added successfully!")

# Function to verify if the patient dictionary has all the records
def verifyPatientData():
    for recordNumber, patientInfo in patients.items():
        print(f"Record Number: {recordNumber}")
        print(f"Name: {patientInfo['name']['first_name']} {patientInfo['name']['last_name']}")
        print("Vaccinations:")
        for vaccine, months in patientInfo["vaccinations"].items():
            print(f"  {vaccine}: {months}")
        print()

# Vaccination data John Smith
vaccinesJohnSmith = {
    "HepB": [0, 1, 6],
    "RV": [2, 4, 6],
    "DTaP": [2, 4, 6, 15],
    "Hib": [2, 4, 6, 12],
    "PCV13": [2, 4, 6, 12],
    "IPV": [2, 4, 6],
    "IIV4": "Annual",
    "MMR": [12],
    "VAR": [12],
    "HepA": [12]
}

# Inserting John Smith's record
insert("R001", "John", "Smith", vaccinesJohnSmith)

# Vaccination data Olivia James
vaccinesOliviaJames = {
    "HepB": [0, 1, 6],
    "RV": [2, 4, 7],
    "DTaP": [2, 5, 7, 12],
    "Hib": [2, 4, 6, 12],
    "PCV13": [2, 5, 7, 12],
    "IPV": [2, 5, 8],
    "IIV4": "Annual",
    "MMR": [12],
    "VAR": [12],
    "HepA": [12]
}

# Inserting Olivia James' record
insert("R002", "Olivia", "James", vaccinesOliviaJames)

# Verify the dictionary contains all data after adding Olivia James
verifyPatientData()

# Vaccination data Esteban Perez
vaccinesEstebanPerez = {
    "HepB": [0, 1, 6],
    "RV": [2, 4, 7],
    "DTaP": [2, 5, 7, 12],
    "Hib": [2, 4, 6, 12],
    "PCV13": [2, 5, 7, 12],
    "IPV": [2, 5, 8],
    "IIV4": "Annual",
    "MMR": [12],
    "VAR": [12],
    "HepA": [12]
}

# Inserting a new record for Esteban Perez
insert("R003", "Esteban", "Perez", vaccinesEstebanPerez)

# Verify the dictionary contains all data after adding Esteban Perez
verifyPatientData()
```



