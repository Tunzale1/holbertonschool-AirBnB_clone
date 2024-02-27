# AirBnB clone - The console
- The goal of the project is to deploy on your server a simple copy of the AirBnB website.
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
