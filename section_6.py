class Employee:
    __slots__ = ('name', 'surname', 'age', 'status',
                 'salary')  # Less memory usage, potentially faster attribute access, but fixed attribute set.

    def __init__(self, name, surname, age, status, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.status = status
        self.salary = salary


# Example usage
e1 = Employee("Andrew", "Doer", 42, "FT", 46000)
print(e1.name, e1.age, e1.status)

# Explanation: __slots__ reduce memory usage and can potentially make attribute access faster by preventing the
# creation of a __dict__ for each instance. However, __slots__ restrict the ability to add new attributes
# dynamically, making them less flexible. Descriptors are special Python objects that implement one or more of the
# descriptor methods: __get__, __set__, and __delete__. Descriptors allow customization of attribute access behavior.
# __slots__ and descriptors can be used together to optimize memory usage and customize attribute access. __slots__
# are best used when memory optimization and attribute management are crucial, as they impose limitations on
# flexibility, inheritance, and compatibility.
