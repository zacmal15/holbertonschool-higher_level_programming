Introduction:

While studying Python, one of the first things I learnt is that everything in python is an object.
This demonstrates why lists and variables can affect other variables, why integers behave differently from lists
and how Python passes arguments to functions.

In this project, I learnt about object identities, object types, mutable and immutable objects, references, aliases, and how python handles variables in arguments.

Object Identity `(id)` & Type `(type)`:

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