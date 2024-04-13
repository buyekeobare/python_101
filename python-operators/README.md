# Python Operators

Python operators allow us to do common processing on variables.
They are the special symbols that can manipulate the values of one or more operands.

## List of Python Operators

Python operators can be classified into several categories.

- Assignment Operators
- Arithmetic Operators
- Logical Operators
- Comparison Operators
- Bitwise Operators
- Python Assignment Operators

Assignment operators include the basic assignment operator equal to sign (=).

To simplify code, and reduce redundancy, Python also includes arithmetic assignment operators.

This includes the += operator in Python used for addition assignment, //= floor division assignment operator, and others.

Here’s a list of all the arithmetic assignment operators in Python.

Operator Description

- += a+=b is equivalent to a=a+b
- _= a_=b is equivalent to a=a\*b
- /= a/=b is equivalent to a=a/b
- %= a%=b is equivalent to a=a%b
- **= a**=b is equivalent to a=a\*\*b (exponent operator)
- //= a//=b is equivalent to a=a//b (floor division)

## Python Arithmetic Operators

Operator Description Example

- - used to add two numbers sum = a + b
- – used for subtraction difference = a – b
- - used to multiply two numbers. If a string and int is multiplied then the string is repeated the int times. mul = a*b>>> “Hi”*5
    ‘HiHiHiHiHi’
- / used to divide two numbers div = b/a
- % modulus operator, returns the remainder of division mod = a%b
- \*\* exponent operator

## Python Comparison Operators

Operator Description Example

- == returns True if two operands are equal, otherwise False. flag = a == b
- != returns True if two operands are not equal, otherwise False. flag = a != b
- >     returns True if left operand is greater than the right operand, otherwise False.	flag = a > b
- < returns True if left operand is smaller than the right operand, otherwise False. flag = a < b
- > = returns True if left operand is greater than or equal to the right operand, otherwise False. flag = a > b
- <= returns True if left operand is smaller than or equal to the right operand, otherwise False. flag = a < b

## Python Bitwise Operators

Operator Description Example

- & Binary AND Operator x = 10 & 7 = 2
- Binary OR Operator
- ^ Binary XOR Operator x = 10 ^ 7 = 13
- ~ Binary ONEs Compliment Operator x = ~10 = -11
- << Binary Left Shift operator x = 10<<1 = 20
- > >     Binary Right Shift Operator	x = 10>>1 = 5

## Python Operator Precedence

Precedence of these operators means the priority level of operators. This becomes vital when an expression has multiple operators in it.
For example consider the following expression:

> > > 2+3\*4
> > > From the above expression, what do you think the series of operation would be? We can add 2 and 3, then multiply the result by 4. Also, we can multiply 3 and 4 first, then add 2 with it. Here we can see that the operators’ precedence is important.

Below is a list of operators indicating the precedence level. It’s in descending order.
The upper group has more precedence than that of the lower group.

- Parenthesis – ()
- Exponentiation – \*\*
- Compliment, unary plus and minus – ~, +, -
- Multiply, Divide, modulo – \*, /, %
- Addition and Subtraction – +, -
- Right and Left Shift – >>, <<
- Bitwise AND – &
- Bitwise OR and XOR – |, ^
- Comparison Operators – ==, !=, >, <, >=, <=
- Assignment Operator- =
