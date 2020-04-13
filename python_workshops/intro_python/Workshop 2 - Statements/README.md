# Workshop Two: Statements
We have decided to swap week 2 and week 3 content. So, we will be covering statements (while loops, for loops, if statements, and definitions) before going into data structures.

Having these tools will help you make beginner level programs to give you more tools to program on your own.

Lecture: https://docs.google.com/presentation/d/1Hqs3p0iCXdp98B3oYCCNKF-FEJcPWq6qQZpkO9JNYvo/edit#slide=id.g8347ba00cb_0_333

Recording: https://drive.google.com/drive/u/1/folders/1543fqIZM_SifdfLDSi194oK1yGGSGqsq

## Announcements
1. Github repositories will be released Monday morning. Lectures will contain indepth information building on the github material.
2. Lectures will start at 12:30.
3. Office hours for coding together and talking about course material are 3pm - 4pm on Wednesday and Friday. Office hours will be held in the discord channel: https://discord.gg/rHKN2sF

## Course Goal
The main goal for this course is to build basic programs from Riot Games API where participants will be able to manipulate data through Python's basic commands and the Pandas package.

# Lecture Concepts
Today we will be covering for loops, while loops, if statements, and functions.

Goals for today:
1. Understand the fundamentals of if, for, and while loops
2. Have the skills to make your own functions/definitions

## For loops
For loops are used to iterate over a block of code a fixed number of times.

Example 1
![Range from number](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/For%20loop%20-%20number%20range.png)

Example 2
![Range from String](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/For%20loop%20-%20number%20range%20string.png)

Example 3
![Loop over string](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/For%20loop%20-%20string.png)

Example 4
![Changing Range](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/For%20loop%20-%20changing%20range.png)


## Conditional Statements (If statements)
Conditional statements are represented as if, elif, and else within Python. They allow you to run different blocks of code depending on the truth value to the given statement(s). 

Example 1: If a statement is true, then the inner code block will run, but if it is not, then the inner code block will not run.
![Introduction If-statement](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/If%20statement%20Introduction.png)

Example 2: When a statement is not true, you can make an else statement. The else will only run if all the given statement(s) within the if and elif statements are false.
![If-else](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/If-else.png)

Example 3: When having multiple branches of if and else if, all of those statements will be evaluated from top to bottom. So, 2 < 1 will be evaluated first (which is false), then it will evaluate 3 < 2 (which is also false). Thus, we enter the else branch as all other truth statements are false.
![If-else](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/Multiple%20branch%20if-else.png)

Example 4: If two statements are true within the if and elif branch, the first branch that is true will be evaluted first. Here, the first branch would only run and we would proceed past the 'elif True' branch.
![If-elif](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/Multiple%20branch%20if-elif.png)


## While loops
While loops repeat a block of code every time the given statement is true. You can think of it as a repetitive conditional statement that continues to run until proven false.
![while](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/while%20loop.png)

## Functions
Functions are ways to save a piece of code you used in one part of your program and save it to use at another time. This way, you can prevent redundancy within your program.
![Functions](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Example%20Pictures/Functions.png)

## Examples of using course material
Within these two examples, you'll see example situations where we can use both statements and basic types to make programs.

![Python Example One](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Python%20Combination%20Example%201.ipynb)

![League of Legends Python Example](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Python%20Combination%20Example%202.ipynb)


# Practice problems
1. Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.
2. Write a Python program to guess a number between 1 to 9. Consider using the random module.
3. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For ones that are both divisible by three and five print "fizzbuzz".
4. Write a Python program to print the alphabet pattern 'D'.
5. Write a Python program to print alphabet pattern 'E'.

All programs can be programmed in multiple ways. ![Solutions](https://github.com/ktptran/pcm_functions/blob/master/python_workshops/intro_python/Workshop%202%20-%20Statements/Week%202%20Practice%20Problem%20Solutions.ipynb)
