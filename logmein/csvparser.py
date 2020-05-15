import csv

def parse(file):
    retVal = []
    with open(file) as f:
        reader = csv.DictReader(f)
        # fieldNames = reader.fieldNames
        for row in reader:
            retVal = retVal + [row]
    return retVal

def dump(data, fieldNames):
    with open('info.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldNames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)