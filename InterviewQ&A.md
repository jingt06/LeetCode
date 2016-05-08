###What is inheritance and why do we use inheritance.

**Inheritance** is when a object or class is based on anohter object or class, using the same implementation specifying implementation to maintain the same behavior.

**Why to use**: code reuse, provide polymorphism

**Types of inheritance**: 

- **Single inheritance**: subclass inherit the features of one super class
- **Multiple inheritance**: one class can have more than onesuper class and inherit features from all paretn classes
- **Multilevel inheritance**
- **Hirarchical inheritance**: one class serves as a superclass for more than one subclass

-
###What is Polymorphism
**polymorphism** is the characteristic of being able to assign a different meaning or usage to something in different contexts.

C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.(ususally with an abstract base class)

-
###What is Override

An **override** is a type of function which occurs in a class which inherits from another class. An override function "replaces" a function inherited from the base class, but does so in such a way that it is called even when an instance of its class is pretending to be a different type through polymorphism

-
###What is Design Pattern
**Design patterns** is a general repeatable solution to a commonly occurring problem in software design

####Singleton Pattern
In software engineering, the **singleton pattern** is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system.


-
###C++ Vs Java
- **Inheritance difference**: Multiple inheritance is not supported in Java
- **Resource management**: 
  - Java offers automatic **garbage collection**, 
-Memory management in C++ is usually done through constructors, destructors, and smart pointers.
  - C++ can allocate arbitrary blocks of memory. Java only allocates memory through object instantiation


-

###Java Vs JavaScript
|Java|JavaScript|
|---|---|
|statically typed language| dynamic typed language|
|class-based|prototype-based|
|block-based scoping| function-based scoping|
| Two-Stage | Runtime-only Debugging|
| OOP programming language|OOP scripting language|
| run in a virtual machine or browser | run on a browser only|










