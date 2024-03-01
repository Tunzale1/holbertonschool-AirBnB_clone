# AirBnB clone - The console
- The goal of the project is to deploy on your server a simple copy of the AirBnB website.
- The AirBnB Console is a command-line application designed to manage AirBnB-like objects. It provides a user-friendly interface for creating, displaying, updating, and deleting instances of various classes such as BaseModel, User, State, City, Amenity, Place, and Review.
### Concepts to learn
- Unittest - and please work all together on tests cases
- Python packages concept page
- Serialization/Deserialization
- *args, **kwargs
- datetime
### The console
- The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
- This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
- The console will be a tool to validate this storage engine
### Storage
- Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.
- In this project, we will manipulate 2 types of storage: file and database. For the moment, we will focus on file.
- Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.
### File storage == JSON serialization
- For this first step, we have to write in a file all your objects/instances created/updated in our command interpreter and restore them when we start it.
### *args, **kwargs
What? What’s *args and **kwargs?
- *args is a Tuple that contains all arguments
- *kwargs is a dictionary that contains all arguments by key/value
- So, to make it clear, *args is the list of anonymous arguments, no name, just an order. **kwargs is the dictionary with all named arguments.
### datetime
- datetime is a Python module to manipulate date, time etc…

![image](https://github.com/Tunzale1/holbertonschool-AirBnB_clone/assets/114104944/3b85bbc5-5bb7-4b55-ae74-206cb98a4198)
