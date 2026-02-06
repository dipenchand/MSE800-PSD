 # W8-A1 — Factory Design Pattern
 
 This code uses a Factory Pattern to split a person’s name into **first name** and **last name**. The user can type a name as `First Last` (with a space) or `Last, First` (with a comma). Instead of the program choosing the parser in many different places, it uses one factory class (`NamerFactory`) to decide which parser object to create (`FirstFirst` or `LastFirst`). The console code just asks the factory for a `Namer`, then reads `namer.first` and `namer.last` to show the result.
 
 For example, typing `Dipendra Thakur` or `Thakur, Dipendra` will end up showing **First: Dipendra** and **Last: Thakur**

 
<img width="800" height="100%" alt="Screenshot 2026-02-07 at 12 18 10 PM" src="https://github.com/user-attachments/assets/9674051d-43d4-4e15-9568-69207c3a6aa9" />
<br>
<img width="413" height="100%" alt="Screenshot 2026-02-07 at 12 38 45 PM" src="https://github.com/user-attachments/assets/563a714d-6f07-4217-9895-1e8769bde6b9" />
