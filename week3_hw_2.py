from example_data import lucid_codes

num_students = len(lucid_codes['students'])
num_trainers = len(lucid_codes['trainers'])

print(num_students)
print(num_trainers)

for student in lucid_codes['students']:
    print('Students name is: ' + student['name'])
    print('Students title is: ' + student['title'])
    print()

for trainer in lucid_codes['trainers']:
    print('Trainer name is: ' + trainer)

    
