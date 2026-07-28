# dictionaries (key - value pairs) - most powerful

student = {
    "name" : "amit",
    "age" : 21,
    "course" : "Python",
    "marks" : 92
  
}

#  Access
print(student["name"])
print(student.get("age"))
print(student.get("city", "not found")) # safe only


#  add / update
student.pop("marks")

#  loop through dictionary
for key, value in student.items ():
    print(f"{key} -> {value}")