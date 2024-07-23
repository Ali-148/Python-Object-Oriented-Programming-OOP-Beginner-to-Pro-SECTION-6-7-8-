from dataclasses import dataclass, field


@dataclass
class Employee:
    name: str
    surname: str
    age: int
    status: str
    salary: float
    skills: list = field(default_factory=list)  # Mutable default


@dataclass
class Car:
    model: int
    name: str
    variant: str


c1 = Car(model=2010, name="GLI", variant="Toyota GLi 1.3 VVTi")
print(c1)


# Example usage
e1 = Employee(name="Andrew", surname="Doerte", age=42, status="FT", salary=46000.0)
print(e1)  # Output: Employee(name='Andrew', surname='Doerte', age=42, status='FT', salary=46000.0)

e2 = Employee(name="John", surname="Doe", age=30, status="PT", salary=35000.0)
print(e1 == e2)  # Output: False

e3 = Employee(name="Andrew", surname="Doerte", age=42, status="FT", salary=46000.0)
print(e1 == e3)  # Output: True

# Data classes provide a clear and concise way to define classes that are primarily used for storing data.
# They reduce the amount of boilerplate code, enhance readability, offer built-in features for automatic method generation, and support advanced features like immutability and default values.
# These benefits make data classes a powerful tool for object-oriented programming in Python.




# Named Tuples
# Advantages:
#
# Simplicity: Named tuples are simpler and have less overhead. They provide a lightweight way to define simple classes with named fields.
# Immutability: Named tuples are immutable by default, which means their fields cannot be changed once they are set.
# Built-in Methods: They come with useful methods such as _replace(), _asdict(), and _fields, which make it easy to work with their data.
from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'surname', 'age', 'status', 'salary'])

e1 = Employee(name="Andrew", surname="Doerte", age=42, status="FT", salary=46000.0)
print(e1)  # Output: Employee(name='Andrew', surname='Doerte', age=42, status='FT', salary=46000.0)


