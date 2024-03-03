# PYTHON MATH TRICK 2

My second attempt at coding the logic behind a math trick: how to multiply any two 2-digits numbers.

- [PYTHON MATH TRICK 2](#python-math-trick-2)
    - [DETAILS:](#details)
    - [SOURCE](#source)
    - [WHAT IS IT](#what-is-it)
    - [WHY?](#why)
    - [OPPORTUNITY TO LEARN](#opportunity-to-learn)
    - [I'M AWARE THAT:](#im-aware-that)
    - [VISUALISATION OF THE LOGIC](#visualisation-of-the-logic)


****

### DETAILS:
- **Language**: Python v3.12 (virtual env.: anaconda)
- **IDE**: VScode
- **Team**: 1
  - **Members**: 1
    - Jean-Yves (Me)
-  **Scope**: Personal project

****

### SOURCE

The logic is from this  [YouTube video](<https://youtu.be/H98sVfOOK9k?si=aWz8zuMkvl6eumi>) (in French though).

****

### WHAT IS IT

This is not a trick intended for code efficiency. It is a trick to help anyone who wants
to quickly calculate the multiplication of any 2 numbers that are 2-digits numbers, like 78 and 91,
as long they are both > 9 and < 100 the trick will work. So this is more of a no-calculator-available solution.

****

### WHY?

This is the second attempt at coding the logic behind a math trick, and this one is a little more complicated.
Because it is not based on a 2-digits number multiplied by itself.

I was curious to see if I could pull it off in the first attempt and the sense of accomplishment I felt
once finished was great, so I decided to continue with math tricks.

****

### OPPORTUNITY TO LEARN

This is great for me to learn:
- collections' manipulation:
  -  int/str methods 
  - and manipulation, 
- and to practice on: 
  - basic conditionals
  - and loops

I also found myself interested in how I could improve the user experience delivered by the bare terminal UI of a code editor.   
This meant adding some code like a time.sleep to mimic a computer thinking process, to add prints of ANSII codes to clean the terminal for visual comfort, and to better structure my prints and inputs' strings.

>I learnt a lot more than that:
>- Git in VScode: basic GIT process (<mark>repo creation, commits)
>- VScode Virtual Environment: 
  >     - <mark>setting up a virtual environment (Anaconda)</mark>
  >     - and install modules.
>- VScode: setting up and customization: 
  >     - <mark>formatter
  >     - settings.json
  >     - <mark>pylance
  >     - <mark>vscode recommendations file
  >     - vscode customization: line height, font, comments' color, theme
>- Python best-practices: 
  >     - <mark>README in markdown</mark> (just like here)
  >     - <mark>type annotations (PEP8)
  >     - <mark>refactoring</mark>: in this case, turning redundant lines to functions

****

### I'M AWARE THAT:

The <mark>git of this repository has no pull request</mark>, because this is JUST ME coding here. I left the repo as is so that, maybe, sometime in the future, the code could be reviewed. 

During the refactoring process, one could argue that me using a function to refactor a 3 numbers' addition into a 6 or 4 parameters function is not optimal. I agree, and I still went with it because I wanted to practice functions. So this is purely for practice. 

I scattered many print functions that are here for logging and testing purposes. I know about py.test and I did not rewrite the code implementing it. I am not even sure if this would be a good idea as, TMHO, this project is at a reasonably small size and logging/testing with prints are ok, I guess.  
However, I am looking at icecream for future small projects like this one. 

****

### VISUALISATION OF THE LOGIC

I started to develop a preparation process before starting to code. I make a mind map of the logic I am trying to break down and code. This helps in many ways, first is better learning of the logic, better understanding and remembering too. It also serves as a reference if I need a refresher.

This <mark>SAVED me a TON of time</mark> during testings and during coding in general. I am starting to think that <mark>this is ESSENTIAL to any serious coding project</mark>, no matter the language. 

****

![alt text](image-1.png)

****

I will not describe the logic behind here, I prefer to do it in the main file instead. This way I add numbered bullet points that I can then use in the code for better code comprehension and referencing. I did this in my first attempt and I found it very helpful.
