'''
In our code below, student is our dictionary, and inside it, we have three things: 'name', 'age', and 'course'. 
'name' is a key for one thing, 'age' is a key for another thing, and 'course' is a key for a list of things.

When we write student['name'], we are asking Python to look inside the dictionary called student and find the key 'name'. 
Once Python finds it, it gives us back the value associated with that key.
When we run this code, Python will print out 'John', because that's what's stored in the key 'name' inside the student dictionary.

If we tried to find a key that doesn't exist like 'address', python would be confused. It would make a big fuss about it and give us an error.
'''

student = {'name': 'Eric', 'age': 36, 'course': ['Math', 'Computer Science']}
print(student['name'])