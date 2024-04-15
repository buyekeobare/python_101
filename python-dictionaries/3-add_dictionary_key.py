'''
Eric just got a new phone number, and we want to add it to our dictionary too!

Using this formula, student['phone'] = '0112 345 678', we are adding a new key to our dictionary called 'phone' that contains Eric's phone number.
When we run this code, Python will print out '0112 345 678', because that's the phone number we just added to our student dictionary."
'''

student = {'name': 'Eric', 'age': 36, 'course': ['Math', 'Computer Science']}
student['phone'] = '0112 345 678'

print(student.get('phone'))