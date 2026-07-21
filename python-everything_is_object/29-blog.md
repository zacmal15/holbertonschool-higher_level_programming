## Introduction

While studying Python, one of the first things I learnt is that everything in python is an object.
This demonstrates why lists and variables can affect other variables, why integers behave differently from lists
and how Python passes arguments to functions.
In this project, I learnt about object identities, object types, mutable and immutable objects, references, aliases, and how python handles variables in arguments.

---

## Object Identity `(id)` & Type `(type)`

Every object in Python has 3 important properties:
- Type
- Value
- Identity

Object's identities are unique and can be viewed using the `id()` function.
Object's type can be viewed using the `type()` function:

```python
x = 10

print(type(x))
print(id(x))
```
Possible output:
```python
<class 'int'>
140475236120752
```
The number returned by `id()` will be different everytime it runs.

Python also lets us compare 2 variables in different ways:
```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```
Output:
```python
True
False
```
`==` compares values
`is` compares if 2 variables refer to the exact same object as each other.

---

## Mutable Objects

Mutable objects are objects that can be modified after being created.
Common mutable objects include:
- Lists
- Dictionaries
- Sets

Example:
```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```
Output:
```python
[1, 2, 3, 4]
```
The list itself changed rather than creating a new object.
Another example is where 2 variables can refer to the same list:
```python
l1 = [1, 2, 3]
l2 = l1

l1.append(4)

print(l2)
```
Output:
```python
[1, 2, 3, 4]
```
Both of these variables point to the same list, so modifying the list through one variable affects the other.

---

## Immutable Objects

Immutable objects are objects that cannot be modified after they are created.
Common immutable objects are:
- Integers
- Floats
- Strings
- Tuples
- Booleans
Instead of changing the existing object, python creates a new one.
Example:
```python
x = 5

print(id(x))

x += 1

print(id(x))
```
Possible output:
```python
140476521968296
140476521968328
```
The object identifier changes because a new integer object is created.
Strings behave the same way:
```python
name = "Python"

name += "3"

print(name)
```
Output:
```python
Python3
```

---

## Why does mutability matter in Python?

