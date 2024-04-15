'''
From our file 0-dictionary.py, we learnt how to find a dictionary key and its associated information. 
In this code student.get('name'), we are doing the same thing but in a cool way using .get().
The cool part about using .get(): If for some reason John's name wasn't in the dictionary, Python wouldn't get confused. 
Instead, it would just say, "Hmm, I couldn't find John's name, but that's okay." It won't make a big fuss about it. It will instead give us none.
'''

student = {'name': 'Eric', 'age': 36, 'course': ['Math', 'Computer Science']}
print(student.get('name'))
