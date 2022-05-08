# Ayoub Maimmadi: 76678

# Language: Python3
def name_check(name):
    if len(name) < 2 or len(name) > 40:
        return False
    # check that the name only includes alphabetical characters, -, or
    # a single quote.
    for char in name:
        if not char.isalpha() and char != '-' and char != "'":
            return False
        #check if name has --
    if '--' in name:
        return False
    return True

names = [
  '--badcode','a','Ayoubot82102','SommerVill','Ayoub-Maimmadi','a','Ayoub',
]

# loop through the names and print whether they are valid or not
for name in names:
    if name_check(name):
        print(name, '\tis a valid name\t\tok')
    else:
        print(name, '\tis not a valid name\t\tFAIL')







