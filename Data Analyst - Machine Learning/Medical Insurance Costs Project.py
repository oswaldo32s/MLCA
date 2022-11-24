names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

names.append('Priscilla')
insurance_costs.append(8320.0)

medical_records = list(zip(names,insurance_costs))

print(medical_records)

num_medical_records = len(medical_records)

print('There are ' + str(num_medical_records) + ' medical records.')

first_medical_record = medical_records[0]

print('Here is the first medical record: ' + str(first_medical_record) )

print('Here are the medical records sorted by insurance cost: ' + str(sorted(medical_records, key=lambda l:l[1])))

cheapest_three = sorted(medical_records, key=lambda l:l[1])[:3]

pricest_three = sorted(medical_records, key=lambda l:l[1], reverse=True)[:3]

print(cheapest_three)
print(pricest_three)