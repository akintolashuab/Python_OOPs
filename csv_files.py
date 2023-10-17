import csv

# data = [
#     ["Name", "Age", "Location"],
#     ["Alice", 25, "New York"],
#     ["Bob", 30, "Los Angeles"],
#     ["Eve", 22, "Chicago"]
#     ]
# with open('Data.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)
    
# with open('Data.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row[2::])
    
    
# data = [
#     ["Bright", 40, "Alaska"],
#     ["Stones", 27, "Los Angeles"],
#     ["Emmanuel", 25, "Atlanta"]
#     ]
# with open('Data.csv', 'a') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)

# with open('Data.csv', 'r') as file:
#     fieldname = ["Name", "Age", "Location"]
#     csv_reader = csv.DictReader(file, fieldname)
#     for row in csv_reader:
#         if csv_reader.line_num != 1:
#             print(row['Name'], row['Age'], row['Location'])
# try:
#     data = [
#         {'Name': 'Bright', 'Age': 40, 'Location': 'Alaska'},
#         {'Name': 'Stones', 'Age': 27, 'Location': 'Los Angeles'},
#         {'Name': 'Emmanuel', 'Age': 25, 'Location': 'Atlanta'}
#     ]
#     with open('Dict_data.csv', 'w', newline='') as files:
#         fieldname = ['Name', 'Age', 'Location']
#         csv_writer = csv.DictWriter(files, fieldname)
#         csv_writer.writeheader()
#         csv_writer.writerows(data)
        
# except Exception as e:
#     print(e)

# import pandas as pd
# data = pd.DataFrame({
#         'Name': ['Bright', 'Stones', 'Emmanuel'],
#         'Age' : [40, 27, 25],
#         'Location': ['Alaska', 'Los Angeles', 'Atlanta']
#         })
# print(data)

data = [
    {'Name': 'Bill', 'Age': 40, 'Location': 'DC'},
    {'Name': 'Energy', 'Age': 27, 'Location': 'Texas'},
    {'Name': 'Mighty', 'Age': 25, 'Location': 'Ontario'}
    ]
with open('Dict_data.csv', 'a', newline='') as files:
    fieldname = ['Name', 'Age', 'Location']
    csv_writer = csv.DictWriter(files, fieldname)
    csv_writer.writerows(data)