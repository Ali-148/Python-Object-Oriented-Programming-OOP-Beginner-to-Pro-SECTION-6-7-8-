# Attributes lookup chain


class GrandParents:
    name = "Robert"


class Parent(GrandParents):
    name = "james"


class Child(Parent):
    name = "Lion"

    def __init__(self, name=None):
        if name:
            self.name = name


c = Child()
print(c.name)


# Protocols -> contract between our objects and python

# __get__()
# __set__()
# __delete__()

# descriptors are objects that define some or all of the descriptor protocol when pointed to attribute in other
# objects,they take on special behaviour and allow us to customize attribute for that attribute alone


class Descriptor:
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

    # memory leak in descriptor instace storage used in OOP to Maintain Object State: Store attributes and data
    # specific to each object. Encapsulate Data: Keep object data private and secure within instances. Support Method
    # Functionality: Provide a context for methods to operate on the object's data. Enable Flexibility: Allow
    # different instances to have unique values and behavior Non-data descriptors in Python are descriptors that only
    # implement the __get__ method and do not implement __set__ or __delete__.
