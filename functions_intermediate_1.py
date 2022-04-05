# UPDATE VALUES IN DICTIONARIES AND LISTS

x = [ [5,2,3], [10,8,9] ]

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1
x[1][0] = 15
print(x)

# 2
students[0]['last_name'] = 'Bryant'
print(students[0])

# 3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# 4
z[0]['y'] = 30
print(z)

# ITERATE THROUGH A LIST OF DICTIONARIES

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(dictionary):
    i = 0
    while i < len(dictionary):
        for key, value in dictionary[i].items():
            print(key, '-', value)
        i += 1

x = iterateDictionary(students)

# GET VALUES FROM A LIST OF DICTIONARIES

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary2(key, dictionary):
    i = 0
    while i < len(dictionary):
        print(dictionary[i][key])
        i += 1

x = iterateDictionary2('first_name', students)
y = iterateDictionary2('last_name', students)

# ITERATE THROUGH A DICTIONARY WITH LIST VALUES

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dic):
    for key, value in dic.items():
        print(len(value), key)
        for childValue in value:
            print(childValue)

        


x = printInfo(dojo)
print(x)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon