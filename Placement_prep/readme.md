# PEP8

### Table of Contents
</br>

- [What is PEP8](#1)
- [Why use PEP 8?](#2)
- [PEP 8 Conventions](#3)
     - [Coding Order](#4)
     - [Naming Coneventions](#5)
        - [For Class](#6)
        - [For Variables](#7)
        - [For Methods/Functions](#8)
        - [For Modules and packages](#9)
- [PEP 8 Coding Structure](#10)
    - [WhiteSpaces](#11)
    - [Line length, Line break And Indentation](#12)
    - [Comments](#13)
    - [Return Statements](#14)
    - [Exception Handling](#15)
- [Auto Formatting Tools](#16)
    - [Black](#17)
    - [autopep8](#18)
    - [yapf](#19)






</br>
</br></br>
</br>

> <center> <h1 id="1"> What is PEP8 </h1></center>

 **Python Enhancement Proposal** 8, or PEP 8, is a style guide for Python code which was developed and defined by Guido van Rossum, Barry Warsaw, and Nick Coghlan in 2001. It helps python programmers to write consistent and readable code. it is not mandatory to follow but it is a good practice in the programming world. PEP8 involves rules/conventions for variable names, whitespace, inline comments, indentation, and much more. It has great resources to write clear, consistent, and readable code. It also portrays one's ability to write code as <ins> "*most of peoples can code but very few of them can code that others also can understand* "</ins>

> <center> <h1 id="2"> Why use PEP 8? </h1></center>

**“code is read much more often than it is written”**,</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; according to Guido van Rossum, the author of Python.
Coding is mostly done in a collaborative environment so that code has to be analyzed by multiple times by multiple users and programmers so that it becomes mandatory to write code in such a way that any person can read and understand the code easily and with less effort to improve code reusability .so it is prommers/code writers tasks is to write code by following some rules and best practices.  </br> It will take time to write code in well-documented form rather than messy form, but it will be worth it anytime. So that’s why we regularly follow coding conventions. Every language has its own rules and practices defined by experts, creators, and developers . </br>
From my personal experiences , code get messy when it evolves so to understand code at later stages , it should be written and documented in a way that , it will be globally acceptable and easily human-readable

</br>
</br>

<!--  this should be make as comparison/side by side -->
<h1># Normal Code of some programmers
<img src="./Images/messy.jpg" />

<h1># Well Documented code by following best practices 
<img src="./Images/neetcode.jpg" />

</br>
</br>
<center> <h1 id="3"> PEP8 Conventions </h1></center>
</br>
</br>

> <h2 id="4"> 1. Coding Order </h2>

Python code must follow the order which is mentioned in PEP8 so to increase code readability, Also it will make modification easier
 
At the TOP of the code always have a docstring (“””  “””) , docstring contains metadata about code like Author name, Author contact details, Module purpose, Offered functionalities, etc.
Docstring always starts and ends with 3 double quotes (“””) 
```python
"""
Author: Rahul Agrawal
Github: https://github.com/rahul-agrawal-99
Module: PEP8-Example
Functions: PEP8-conventions, PEP8-Details
"""
```
 
After Docstring, the Import Statement Should be there. In PEP8, some rules define the writing of import statements.
 
Following are some tips to write import statements :
multiple modules from 1 package can be imported on single line code
Use different import statements for 2 distinct packages
Try to be specific that only needy functionalities from the package should be imported
Also, try to mention why you are requiring the library that is getting imported 
```python
# Allowed
 
import numpy as np    
from pandas import read_csv , read_excel  
 
# Not allowed
 
from os import *    
import os, sys    
 
```
After the Import statement, try to write Constants that will be used later by any of the Functionalities. use only UpperCasing for naming constants.
```python
PIE = 3.1472
ACCESS_POINT = "http://my-url.co/"
PORT = "8080"
SECREAT_PASSWORD = "secret"  
 ```
After 2 - 3 black lines, write actual code and functionalities

#### Sample Code with Proper order
 
```python
"""
Author: Rahul Agrawal
Github: https://github.com/rahul-agrawal-99
Module: PEP8-Example
Functions: PEP8-conventions , PEP8-Details
"""
 
import numpy as np      # For mathematical operations
from pandas import read_csv , read_excel   # reading CSV and excel files for data 
 
PIE = 3.1472
ACCESS_POINT = "http://my-url.co/"
PORT = "8080"
SECREAT_PASSWORD = "secret"  
 
 
# Actual code starts here

```

</br>
</br>

> <h2 id="5"> 2. Naming Coneventions </h2>


Choosing names for your variables, functions, methods, etc. is not always simple. It's critical to think carefully about the names you select to make sure they are understandable, pertinent, and practical. To make the meaning of an object crystal apparent, we advise adopting descriptive names. You will benefit both now and later if you choose descriptive names. If you give one of your functions a hazy name, you risk forgetting what it does when you revisit your code in a few days or weeks. This is where PEP 8 is useful.
 
Naming in Python should be well defined as per functionality so that code readers can understand the meaning and use of variable, class, or function


<h3 id="6"> 2.1 For Class </h3>

Use camelcase or capitalized words for the class name.
Avoid the use of underscores to separate words
CamelCase is a style of word separation that does not use spaces and capitalize the first letter of each word in a sentence like CamelCase , LikeMe etc.
```python
# Allowed 
class MyClass():
 	pass
 
# Not allowed 
class myclass():         # also my_class or myClass
	pass 
```

<h3 id="7"> 2.2 For Variables </h3>
There can be multiple types of variables such as a class object, constants, and data structure names.
The naming of variables involves:

<ul> <li>Use lowercase single letter or word</li> 
<li>If contains more than 1 word then use “_” to separate 2 lower cased words</li> 
<li>Do not use capitalized/Uppercased word unless it is actually constant </li> 
<li>Try to name variables as per their functionality such as the list of prime integers that can be named as prime_list </li> 
</ul>



Almost all the variable has the same convention but there are also some exception like, in constant naming, it should be always uppercased 


```python
# Allowed 

list_prime = []

COLOR_WHITE = (255,255,255)

new_date  = Date()

x  = 20

# Not Allowed 

Mylist  = []

list123 = []


```

<h3 id="8"> 2.3 For Methods / Functions </h3>
Following are some guidelines for Function or method naming 
<ul> 
<li>Always name should be lower cased </li> 
<li>Use of “_” allowed to join 2 different words</li> 
<li>Avoid use of in built methods of python </li> 
<li>Use of “_” at beginning is allowed only in class methods like __init__</li> 
</ul>






```python
# Allowed

def fun_add():
	pass 

class MyClass():

    def  __fun_read():   # private functions
		Pass

```

<h3 id="9"> 2.4 For Module and packages </h3>
Following are some guidelines for module and package naming
<ul> 
<li>Naming should be short as possible </li> 
<li>Use of “_” is allowed to join 2 words except in package naming</li> 
<li>Use only lowercase words </li> 

</ul>





```python
# Allowed 

my-module  , module_1

# Not Allowed

Module , Module_for_so_so_funtion


```

</br>
</br>

<center> <h1 id="10"> PEP 8 Coding Structure </h1></center>


</br>
</br>

> <h2 id="11"> 1. WhiteSpaces </h2>
Spacing between 2 characters is a way to make code easy to read, that's why it is important to follow correct spacing, it should not be too much or too less

Spacing for variable and value

```python
# right way
X = 10     # keep one black space from both side
Mylist = [1, 2, 3]   # value + “,” + 1 whitespace + next value    and so on

#  Wrong way 
X=10  or  X =   10
Mylist = [1,2,3,   4]

```
Spacing between operator and operands
```python
# right way
i = i + 1   # keep 1 blank space in between
i += 1 
x = x*2 + 1   # for multiply/divide keep both operands together
y = (a+b)    # if operation is in brackets , then dont keep blank spaces
 
 
#  Wrong way
i=i+1
i +=1
c = c * 2     or  c = c* 2
x = (a + b)


```

</br>
</br>

> <h2 id="12"> 2. Line length, Line break And Indentation </h2>
For List :
```python
li = [      # use if list has multiple list inside
    [ ],
    [ ]
]
```

For Dictionary :
```python
 # always write dictionary as this
dictionary = {       
    "key" : "value",
}
```
 
For Conditional Statements:
```python
#  In IF statements
 
# Correct:
if foo == 'blah':
    do_blah_thing()
 
# Wrong:
if foo == 'blah': do_blah_thing()
 ```

For Function :
 ```python
# one blank space between arguments, also keep return type whenever possible
def fun(a, b) -> int:     
return fun(a=a+1 ,b=b-1)   

 
# at max 79 char as last one is newline character
def myfun(arg1,arg1,arg1,arg1,arg1,arg1,arg1,arg1,arg1,arg1,
        arg1,arg1,arg1,arg1,arg1,arg1): 
        # use newline for extra arguments with 4 indention tabs left
  	mycode = none           # code should be start from 2 indention tabs
 ```
FOr Class and its methods : 
 ```python
class A():
    pass
# 1
# 2             , exact 2 black new line spaces before declaring a class or any function
class B():    
  def __init__(self):
    pass
# 1 blank line between methods of a class  
  def __repr__(self):
    pass

```
</br>
</br>

> <h2 id="13"> 3. Comments </h2>
Comments play an important role in the coding process. It is critical that they are clear, up to date, and useful. Comments not only help us, but they also help anyone else who comes into contact with our code.
It's best to write comments in full sentences, with the first letter of the first word capitalized. This is known as a sentence-style case. It's fine to use a lowercase letter here if our code starts with an identifier. We should never, ever change the name of an identifier.

```python

def func():
	# comment also should be indented inside class or function
	pass

var = 10  # keep 2 to 5 whitespaces between value and # sign

“”” in case of docstring start from the first line
End line here so that the last 3 quotes should be always on a new line
”””


```
</br>
</br>

> <h2 id="14"> 4. Return Statements </h2>
Consistant in return , always statement should return something (except Nonetype) irrespective of any condition
```python
# Correct:
 
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return False
 
# Wrong:
 
def foo(x):
    if x >= 0:
        return math.sqrt(x)


```
</br>
</br>

> <h2 id="15"> 5. Exception Handling </h2>

```python

try:
  # mycode
# explicitely mention possibly occuring error instead using Exception as e 
except ImportError:     
  #  handling
except Exception:
  #  final handle for rare exception happened

```
</br>
</br>

<center> <h1 id="16">Auto Formatting Tools </h1></center>

Linters are Auto Formatting programs that provide feedback on the quality of code by displaying warnings and errors. They can detect Python code errors, invalid code patterns, and elements that do not adhere to your conventions. Python linters have several advantages, including:

<ul> 
<li>  Bug prevention in a project.   </li>
<li>  Making Python code readable for any programmer.   </li>
<li>  Detecting and removing unnecessary code.   </li>
<li>   Making code more readable and less complex.  </li>
</ul>

Of course, every approach has drawbacks:
<ul> 
<li>  Linters can produce false positive results.   </li>
<li>  This procedure can take some time.   </li>
<li> Some mistakes may go unnoticed.  </li>

</ul>


</br>
List Of some Available Auto-formatters in Python :
</br>
</br>

> <h2 id="17">  1. Black  </h2>

Black is the uncompromising Python code formatter. You give up control of the finer points of hand-formatting by employing it. You receive speed, determinism, and independence from pycodestyle's pestering about formatting in exchange for Black.

```cmd
pip install black
```
</br>

><h2 id="18">  2. autopep8 </h2>
autopep8 would auto-format your python script. not only the code indentation but also other coding spacing styles. It makes your python script to conform the PEP8 Style Guide.

```cmd
pip install autopep8
```
</br>

><h2 id="19">  3. yapf </h2>
Most of the current formatters for Python --- e.g., autopep8, and pep8ify --- are made to remove lint errors from code. This has some obvious limitations. For instance, code that conforms to the PEP 8 guidelines may not be reformatted. But it doesn't mean that the code looks good.

YAPF takes a different approach. It's based off of 'clang-format', developed by Daniel Jasper. In essence, the algorithm takes the code and reformats it to the best formatting that conforms to the style guide, even if the original code didn't violate the style guide. The idea is also similar to the 'gofmt' tool for the Go programming language: end all holy wars about formatting - if the whole codebase of a project is simply piped through YAPF whenever modifications are made, the style remains consistent throughout the project and there's no point arguing about style in every code review.

```cmd
pip install yapf
```
</br></br></br>
Wrapping Up , </br>
Reading and writing code are much more effective and efficient thanks to the PEP 8 style standard. A guide is a helpful tool that we can use to improve our code reading and writing processes even though it might not always be applicable to our line of work. There is still a lot to learn about PEP 8, which we only touched on briefly in this article.

Enjoy Learning :smile::open_book::computer:


