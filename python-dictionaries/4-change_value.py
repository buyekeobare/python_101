'''
But wait, something interesting is happening! It seems like Eric told us he wants to change his name to Emily! 
What do we do? We go to our dictionary and find the key 'name', which currently says 'Eric'. 
We scratch out 'Eric' and write 'Emily' instead.

So, student['name'] = 'Emily'

Now, when we look inside our dictionary by printing student, Python will show us the updated information. 
Instead of 'Eric', the key 'name' now points to 'Emily'. 
Everything else in the box stays the same; only Eric's name has changed to Emily.
'''

student = {'name': 'Eric', 'age': 36, 'course': ['Math', 'Computer Science']}
student['name'] = 'Emily'

print(student)