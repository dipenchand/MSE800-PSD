 # W8-A1 — Factory Design Pattern
 
 This code uses a Factory Pattern to split a person’s name into **first name** and **last name**. The user can type a name as `First Last` (with a space) or `Last, First` (with a comma). Instead of the program choosing the parser in many different places, it uses one factory class (`NamerFactory`) to decide which parser object to create (`FirstFirst` or `LastFirst`). The console code just asks the factory for a `Namer`, then reads `namer.first` and `namer.last` to show the result.
 
 For example, typing `Dipendra Thakur` or `Thakur, Dipendra` will end up showing **First: Dipendra** and **Last: Thakur**
