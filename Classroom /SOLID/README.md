## OCP : Open/Closed Principle 
Extending functionality with new classes instead of rewriting.

The OCP states a system must be:
**Open** for extension

But

**Closed** for modification

New features can be added without modifying the existing,stable code base.

New features can only be added on the Child class, not on the Parent/Base class (or the Interface).

## Sign of Violation of OCP 
Large or frequently changing **if-elif-else** (or **switch-case**) chains that choose behavior are often a sign that the code violates the Open/Closed Principle, **since new cases require modifying existing conditional logic.**

## Implementation of OCP in python
One of the way to implement OCP is using:
* **Inheritance + Polymorphism** :
* 
Step 1. Define an **Abstract Base Class** (aka **Interface**) that declares that methods but doesnot implement them. Also the Interface won't be modified.

Step 2. Build on top of the base class , i.e Create child classes that inherit from the base class and implement or override those methods to provide new/specific behavior.

Step 3.Orchestrate the program by selecting the class you want to call any time.


