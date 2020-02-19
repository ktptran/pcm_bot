# Workshop Zero: Introduction to Python
![Python Workshop](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/What_is_Python.png)
## Goals & Content
By the end of this you will be able to:
1. Code in your free time with the applications you setup today.
2. State what Python is on a basic level.
2. Understand the differences between Python two and Python three.
3. Reiterate the differences between the Java and Python.
4. Talk about how Python is used in the real world.

## Setup
We will be setting up our programs and how we will communicate in the future. Before you start this portion, I suggest you also prepare an online notebook or some sort of way to also note down what you have learned here. Doing the programming is one thing, but developing your computer science knowledge is a whole new beast.

### Programs
We will be setting up an integrated development environment (PyCharm), text-editor (Atom), and the coding language (Python).
All of these programs will be used for the rest of this workshop during Spring quarter. The time and date of the workshop will be announced later in the week. 

#### Python
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.

To setup Python follow these instructions:
1. Navigate to the following link: <https://www.python.org/downloads/> then download the latest version of Python.
2. Follow the installation instructions outlined.


#### PyCharm
PyCharm is an integrated development environment used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains.

To setup the IDE follow these instructions:
1. Navigate to the following link <https://account.jetbrains.com/login> and create your account or login to your account.
2. Navigate to the following link <https://www.jetbrains.com/student/> and apply for a student account by pressing the "Apply Now" button under the "How do I apply" section of the webpage. You will then receive an email with further instructions to give you access to the applications.
3. Navigate to the following link <https://www.jetbrains.com/pycharm/download/#section=mac> download the free-open source for pure python development.
4. Follow the installation instructions outlined.

#### Atom
Atom is a free and open-source text and source code editor for macOS, Linux, and Microsoft Windows with support for plug-ins written in Node.js, and embedded Git Control, developed by GitHub.

To setup Atom folow these instructions:
1. Navigate to the following link: <https://atom.io/> then download the latest version of Atom.
2. Follow the installation instructions outlined.


### Communication
Throughout the class, join our discord server at <https://discord.gg/rHKN2sF> to talk with other participants about how they solved problems. We urge you to not post solutions directly to allow everyone the chance to learn how to answer these questions on their own.

#### Discord
Discord is a proprietary freeware VoIP application and digital distribution platform designed for video gaming communities, that specializes in text, image, video and audio communication between users in a chat channel.

There are two ways to access discord:
1. Through browser at <https://discord.gg/>
2. Downloading discord at the same link above and then opening the application. 
As stated before, we will be communicating through this server for the remaining workshops in 2020 Spring Quarter: <https://discord.gg/rHKN2sF>.

## Python Information
<b> What is Python? </b> "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together."

Read more about it here: <https://www.python.org/doc/essays/blurb/>


<b> Why do people prefer Python? </b> "Python’s simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages which allows program modularity and code reuse. No compilation test makes the edit-test-debug cycle incredibly fast. Increase in productivity."
Read more about it here: <https://www.python.org/doc/essays/blurb/>


<b> Java vs. Python: </b> "Python programs are generally expected to run slower than Java programs, but they also take much less time to develop. Python programs are typically 3-5 times shorter than equivalent Java programs. This difference can be attributed to Python's built-in high-level data types and its dynamic typing. Because of the run-time typing, Python's run time must work harder than Java's."
Read more about these differences and more here: <https://www.python.org/doc/essays/comparisons/>

<b> Python 2 vs. Python 3: </b> Starting out as a programmer, you may be asking, should I use Python 2 or Python 3? Now, Python 3 is a no-brainer, here is why:

1. Python 2 is no longer supported as of January 2020 and not receiving updates. <https://wiki.python.org/moin/Python2orPython3>
2. Python 3 is continually being updated and open-source code is continually being developed.
3. Python 3 is the future of where programming is going.

Companies still use Python 2 because Python 3 is not *backwards compatible,* meaning Python 3 does not run Python 2 code without having many errors. Hence, to run certain programs, you'll need to change lines upon lines of code to migrate over to Python 3. 
Want to learn more? Read about it here: <https://www.guru99.com/python-2-vs-python-3.html>

<b> Use cases: </b> Python's use cases are limitless. Everyday, you are interacting with Python programs such as Netflix, Uber, Lyft, Instagram, Google, Spotify, you name it! These companies use Python in many ways including web development, data analytics, and scripting. Some other cases where Python is used include insurance, retail banking, aerospace, finance, and business services. Want to learn more, read about it here: <https://www.techrepublic.com/article/python-5-use-cases-for-programmers/>


## Programming and Practice
Did you skip over the Python information? I know I would, so to learn more about Python, we'll be developing your "Hello World" programs with the addition of talking about Python itself! 

Some tips when writing these programs:
1. When you finish writing your program, before running it, read through your program backwards and ensure that it matches up with the code. This will decrease the amount of errors you make.
2. Write down the errors you make. Writing down the errors will make you more aware of your mistakes and it will decrease the chances of you making that error in the future.
3. Put a comment above every function as you are starting off. This will allow you to understand what your program is doing altogether.

### Running Python Programs
To run a Python program, there are two ways to do it. One is through the terminal, the other is through PyCharm, your IDE.

#### Terminal
1. Open up Atom and save a file as 'test.py'. Save it to a place where you will remember. 
2. Within the document, type print('Hello World!') on the first line. 
3. Save the document.
4. Navigate to your terminal.
* For Windows: go to your windows search bar and type cmd to get to your command prompt. Press enter.
* For Mac OSX: press command + space, a search bar will open, where you will then type 'terminal'. Press enter.

5. Navigate to the directory your test.py file is saved in by using ls (shows what is in your folder), then cd. 
* For example, if my test.py's file path was C:/Documents/projects/test.py, I would use the following commands:
  1. cd Documents
  2. cd projects

6. Run the following command: 'python3 test.py'. This will run your python file and print out "Hello World!".

You can also enter in the command: 'python3' or 'python' to run Python within your terminal.

#### PyCharm
1. Open up PyCharm and "Create a new Project". 
2. Save it to any location using Pure Python.
3. Create a new Python file by right clicking the directory window on the left, New -> Python File.
4. Name the file 'test.py'.
5. Type "print('Hello World!')"
6. In the upper right hand corner click "Add configuration"
7. Click the "+" symbol followed by Python
8. Under Python interpreter, make sure it reads Python 3.8 (or something similar). For script path, click the folder icon and then select the 'test.py' file you have just created.
9. Click open and then OK.
10. Click the play button in the right hand corner and the program will run.

### Exercises
These exercises are adjusted exercises from Zed A. Shaw's Learn Python 3 The Hard Way book. This is how I initially learned Python and it goes more indepth with all of the concepts. If you are interested in learning Python at a faster pace, I highly suggest buying or renting this book from him as his problems build your fundamentals as a computer scientist.

<b>Exercise 1:</b> This exercise introduces you to the basics of programming using print statements.
![Exercise 1](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%200/Exercise%201.png)

Takeaways: Notice how you can use the other quotations depending on which quotation marks you choose for your print statement.

<b>Exercise 2:</b> This exercises introduces you to comments in Python and how we can add additional notes.
![Exercise 2](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%200/Exercise%202.png)

Takeaways: The # symbol is very vital through all code to write down information.

<b>Exercise 3:</b> This exercise introduces you to adding integers and equations to your print statements.
![Exercise 3](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%200/Exercise%203.png)

Takeaways: You can do operations within print statements.

<b>Exercise 4:</b> This exercise introduces you to defining variables and manipulating them to use in print statements.
![Exercise 4](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%200/Exercise%204.png)

Takeaways: To store information, you can use variables.

<b>Exercise 5:</b> This exercise introduces you to using f strings to concatenate variables into your print statements.
![Exercise 5](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%200/Exercise%205.png)

Takeaways: F strings are one way to incorporate variables into your print statements.

### Practice Problems
1. Write a program to introduce your name, year, major, how many credits and classes you are taking, your age, your weight, where you live, and your school. All of these have to be in different variables. Then write a story out of it. You must put a statement where you are above 21 years old without putting that as a string.
2. Write about yourself reading through the Python information section.

Examples of these practice problems will be uploaded following the workshop. We highly suggest you try these on your own and then compare what you did to the examples.



### Quiz
To end off this workshop, we will be having a quiz to test your knowledge: <https://forms.gle/SqFHtKNJ63RRvuEx9>. Good luck!

## Ending
Thank you everyone for partaking in this workshop. This is still a growing workshop series and we plan to bring it back for a full course continuing off this one next quarter. Any feedback is welcomed for where to improve and when to schedule our workshop to make sure all of you are involved. Thanks again, and best of luck on your upcoming exams!

Final form: <https://forms.gle/CkjrS7YdTKVv7fqh7>
