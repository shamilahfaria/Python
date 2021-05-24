
import random
# allocate list types for the requested lists
# names = ["ROSIE Ferrero MARTINEZ",	"JOE LIU",	"SALLY SUE",	"BOB JOHNSON",	"DELIA AGHO"]

ids = []
emails = []
# request user input for names
names = []
for k in range(1,6):
  names.append(input(f'Enter full name with space #{k}: '))

# for each name, generate random ID number in the range requested 
for l in range(len(names)):
  id = random.randint(111111, 999999)

  # check that id does not already exist
  # while id exists in list, regenerate id to append to list.
  while id in ids:
    id = random.randint(111111, 999999)
  ids.append(id)

# create an email that appends the first initial, last name, and last 3 numbers of the id number
j=0
for j in range(len(names)):
  name = names[j]
  id = ids[j]
  # email = name[0]+name[name.index(" ")+1:]+str(id)[3:]+'@example.org'

  # account for first names with a space in them

  # email name will start with first initial of first name
  email_name = name[0]
  # find and store last name for appending later
  last_name = name[name.rindex(" ")+1:]
  # search for spaces between the beginning of the name and the last name 
  for m in range(0,name.rindex(" ")): 
    if name[m] == " ":
        email_name+=(name[m+1])

                    # # next time try .split(), which splits at spaces
                    # name = name.split(" ")
                    # for x in (range(len(name)-1)):
                    #   email_name += name[x][0]
                    # email_name += name[-1]
                    # print(email_name)
                   

  email_name+=last_name
  email = email_name + str(id)[3:] +'@example.org'
  # append email to emails list
  emails.append(email)


# print name, id, and email
i=0
for i in range(len(names)): # can't use a for-each loop because it will store as str and not be useable across all 3 lists. must use range.
  print(f'name: {names[i]} \n'f'id: {ids[i]}\n'f'email: {emails[i]}\n')
