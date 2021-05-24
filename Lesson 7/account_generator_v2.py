

import random
# allocate list types for the requested lists
# names = ["ROSIE Ferrero MARTINEZ",	"JOE LIU",	"SALLY SUE",	"BOB JOHNSON",	"DELIA AGHO"]

# allocate list for student data, that will be comprised of dicts. new student information will be appended to existing list as new dict. 
student_data=[]

# populate list with 5 dicts based on user input for student name
for k in range(1,6):
  student_data.append({"name":(input(f'Enter student full name with space #{k}: '))})
  
  # for each name, generate random ID number in the range requested 
  id = random.randint(111111, 999999)
  
  # check that id does not already exist
  # while id exists in dict, regenerate id
  for i in range(0,len(student_data)):
    while id == student_data[i].get("id"):
      id = random.randint(111111, 999999)
  # once checked, add generated id to dict for that student
  student_data[k-1]["id"]= id

  # create an email that appends the first initial, last name, and last 3 numbers of the id number
  name = student_data[k-1]["name"].split(" ")
  id = student_data[k-1]["id"]
  email_name = ""
  for x in (range(len(name)-1)): # for each word in name that is not the last name (that's len(name)-1)
    email_name += name[x][0] # append the first letter of that word to the email name
  email_name += name[-1] # then append the last name (the last element of the name list)
  student_data[k-1]["email"] = email_name + str(id)[3:] +'@example.org'
  
print(student_data)