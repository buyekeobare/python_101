# Python for Loop

The for loop in Python is an iterating function. If you have a sequence object like a list, you can use the for loop to iterate over the items contained within the list.

The functionality of the for loop isn’t very different from what you see in multiple other programming languages.

## When to use for Loop

Anytime you have need to repeat a block of code a fixed amount of times. If you do not know the number of times it must be repeated, use a “while loop” statement instead.

## For loop Python Syntax

The basic syntax of the for loop in Python looks something similar to the one mentioned below.

for itarator_variable in sequence_name:
Statements
. . .
Statements

### Python for loop Syntax in Detail

- The first word of the statement starts with the keyword “for” which signifies the beginning of the for loop.
- Then we have the iterator variable which iterates over the sequence and can be used within the loop to perform various functions
- The next is the “in” keyword in Python which tells the iterator variable to loop for elements within the sequence
- The sequence variable which can either be a list, a tuple, or any other kind of iterator.
- The statements part of the loop is where you can play around with the iterator variable and perform various function.

### Print individual letters of a string using the for loop

Python string is a sequence of characters. If within any of your programming applications, you need to go over the characters of a string individually, you can use the for loop here.

The reason why this loop works is because Python considers a “string” as a sequence of characters instead of looking at the string as a whole.

### Nesting Python for loops

Nested fir loop is When we have a for loop inside another for loop. There are multiple applications of a nested for loop.

### Python for loop with range() function

Python range is one of the built-in functions. When you want the for loop to run for a specific number of times, or you need to specify a range of objects to print out, the range function works really well.

When working with range(), you can pass between 1 and 3 integer arguments to it:

start states the integer value at which the sequence begins, if this is not included then start begins at 0
stop is always required and is the integer that is counted up to but not included
step sets how much to increase (or decrease in the case of negative numbers) the next iteration, if this is omitted then step defaults to 1
Consider the following example where I want to print the numbers 1, 2, and 3

The range function also takes another parameter apart from the start and the stop. This is the step parameter. It tells the range function how many numbers to skip between each count.

In this example, I’ve used number 3 as the step and you can see the output numbers are the previous number + 3.

We can also use a negative value for our step argument to iterate backwards, but we’ll have to adjust our start and stop arguments accordingly:

Here, 100 is the start value, 0 is the stop value, and -10 is the range, so the loop begins at 100 and ends at 0, decreasing by 10 with each iteration. This occurs in the output

When programming in Python, for loops often make use of the range() sequence type as its parameters for iteration.

### Break statement with for loop

The break statement is used to exit the for loop prematurely. It’s used to break the for loop when a specific condition is met.

Let’s say we have a list of numbers and we want to check if a number is present or not. We can iterate over the list of numbers and if the number is found, break out of the loop because we don’t need to keep iterating over the remaining elements.

In this case, we’ll use the Python if else condition along with our for loop.

### The continue statement with for loop

We can use continue statements inside a for loop to skip the execution of the for loop body for a specific condition.

Let’s say we have a list of numbers and we want to print the sum of positive numbers. We can use the continue statements to skip the for loop for negative numbers.

### Python for loop with an else block

We can use else block with a Python for loop. The else block is executed only when the for loop is not terminated by a break statement.

Let’s say we have a function to print the sum of numbers if and only if all the numbers are even.

We can use break statement to terminate the for loop if an odd number is present. We can print the sum in the else part so that it gets printed only when the for loop is executed normally.

### For Loops using Sequential Data Types

Lists and other data sequence types can also be leveraged as iteration parameters in for loops. Rather than iterating through a range(), you can define a list and iterate through that list.

We’ll assign a list to a variable, and then iterate through the list

In this case, we are printing out each item in the list. Though we used the variable shark, we could have called the variable any other valid variable name and we would get the same output:

The output above shows that the for loop iterated through the list, and printed each item from the list per line.

Lists and other sequence-based data types like strings and tuples are common to use with loops because they are iterable. You can combine these data types with range() to add items to a list, for example

When iterating through a dictionary, it’s important to keep the key : value structure in mind to ensure that you are calling the correct element of the dictionary. Here is an example that calls both the key and the value:

When using dictionaries with for loops, the iterating variable corresponds to the keys of the dictionary, and dictionary_variable[iterating_variable] corresponds to the values. In the case above, the iterating variable key was used to stand for key, and sammy_shark[key] was used to stand for the values.

Loops are often used to iterate and manipulate sequential data types.
