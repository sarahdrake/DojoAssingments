def roll_call(**students):
    for key,data in students.iteritems():
        for value in data:
            print value["first_name"]," ",value["last_name"]
roll_call(students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
])

def roll_call(users):
    i = 0
    for val in users.iteritems():
        print '--',val[0],'--'
        for key in val[1]:
            i += 1
            print i,key['first_name'],key['last_name']





        # for keys1,values1 in values.iteritems():
        #     if keys1 is 'first_name':
        #         print keys1,values1
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}
roll_call(users)

# # users = {
#  'students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Trey', 'last_name' : 'Villafane'}
#   ]
#  }
#

# answer key
for key, data in users.items():
	print "\n%s" %key.title()
	counter = 0

	for value in data:
		counter = counter +1
		full_name = value["first_name"] + " " + value["last_name"]
		full_name_upper = full_name.upper()
		name_count = len(value["first_name"]) + len(value["last_name"])

		print "%d - %s - %d" %(counter, full_name_upper, name_count)
