### **--> Importing \& Using Python Modules**



* Module is a file containing large code(functions, variables)
* we can import and reuse them
* Common built-in Modules

  * math- import math
  * random- import random
  * OS- Operating System interaction
  * \& others
* we can create our own module

  * create .py file \& import it in any code file \& use functions





### **--> Understanding the Need For OOP**

* gradually understanding \& tracking large program codes becomes difficult
* to organized huge code created OOP(Object-Oriented programming)
* **Encapsulation:** related data is encapsulated into a single object

  * function related to those variables are grouped together
* **Object:** combination of related variables \& functions

  * Stores data (attributes)
  * Performs actions(methods)
* **Data Abstraction:** means that we do not need to show all data and functions to the outside world

  * like in computer we can not show inside circuitry
  * e.g. promotes code reusability
  * Enhance modularity
  * improves maintainability
  * makes programs closer to real-world thinking





### **--> Instance Variables \& Instance Methods**

* **Instance:** refers to object created from a class
* purpose of multiple objects is that, each object has its own attributes and methods
* use **self** keyword to create instance object and method \& access them



### **--> Encapsulation in Python - Public \& Private Attributes**

* Encapsulation means keeping all data (attributes \& methods) of an object inside that object
* **Private attributes** are those attributes that can only be used within the class's own methods can not be used globally
* access private attributes by using getters and setters methods
* **Getters:** Getters are functions used to retrieve the attributes of a class
* **Setters:** Setters are functions used to assign or modify the data attributes of a class



### **--> Inheritance in Python - Parent \& Child Classes**

* Inheritance allows a new class to reuse the properties \& methods of an existing class
* **Method Overriding:** feature allowing a subclass to provide a specific implementation of a method already defined in its parent class



### **--> Polymorphism in Python - Overriding \& Overloading**

* refers to the ability of a function or method to exist in multiple forms
* **Method Overriding:** feature allowing a subclass to provide a specific implementation of a method already defined in its parent class
* **Method Overloading:** in method overlading we can use multiple forms of one method \& differentiate between multiple forms by sending arguments



### **--> Python Special Methods**

* **Function:** function can be used in global context \& operates independently of a class
* **Method:** method is a function defined within a class
* **Special Functions:** defines built-in behavior automatically associated with certain operations



### **--> Reading from \& Writing to Files in Python**

* Different formats of data
* **Text File:** contains simple, human-readable textual data
* **CSV(Comma=separated values):** A file format in which data is stored in tabular form, separated by commas
* **Web Applications:** Commonly use JSON(JavaScript Object natation) format for structured data exchange
* Use context manager to use context for how much time and python close it automatically



### **--> Handling Exceptions During File Operation**

* Common issues in file handling, like:

  * file not found
  * wrong path
  * wrong file mode
* to solve this issue, there will be use of exception handling
* an **exception handling** is an error that occurs during the execution of program
* User input can potentially break our code
* **Importance of Exception handling:** Due to an error, python will stop the program \& display an error message, instead , we should handle the error \& allow the program to continue running
* Errors, like:

  * divide by zero
  * file not found
  * invalid user input

