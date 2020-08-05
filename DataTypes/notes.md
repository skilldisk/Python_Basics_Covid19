# Defnition, Data Types and Operators

Follow me on     <a target="_blank" href="https://www.facebook.com/skilldisk"><img style="max-width: 30px;"
            src="https://img.icons8.com/fluent/96/facebook-new.png" alt="facebook"></a>
    <a target="_blank" href="https://twitter.com/skilldisk"><img style="max-width: 30px;"
            src="https://img.icons8.com/fluent/96/twitter.png" alt="Twitter"></a>
    <a target="_blank" href="https://t.me/skilldisk/"><img style="max-width: 30px;"
            src="https://img.icons8.com/color/2x/telegram-app.png" alt="Telegram"></a>
    <a target="_blank" href="https://github.com/skilldisk"><img style="max-width: 30px;"
            src="https://img.icons8.com/fluent/96/github.png" alt="GitHub"></a>
    <a target="_blank" href="https://www.youtube.com/channel/UC41IWICHdLr7uCeeOCPFnpQ"><img style="max-width: 30px;"
            src="https://img.icons8.com/office/2x/youtube.png" alt="Youtube"></a>

----
## Abbreviations
> REPL : Read Evaluate Print Loop

> IDE : Integrated Development Editor


----
# Definitions.

#### Identifiers
> An Identifier is a name given to entities like class, functions, variables etc.


#### Variable
> A variable is a named area of the computers’ memory that can be used to hold data.

> * A variable name can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, and _ )
> * Variable should not start with a number.
> * Python Keywords are not allowed as variable names. 
> * Variable names are case-sensitive.

#### Dynamic Typing
> The type of the data held by a variable can Dynamically change as the program executes.
> Many programming languages such as Java, C and C# where variables are Statically Typed.

#### Keywords
> Keywords are a list of reserved words that have predefned meaning. Keywords are special vocabulary and cannot be used by programmers as identifers for variables, functions, constants or with any identifer name.

> There are 35 Keywords in python3.8. This number can vary slightly over the time.

``` Python
    >>> help('keywords')
        
    Here is a list of the Python keywords.

    False               class               from                or
    None                continue            global              pass
    True                def                 if                  raise
    and                 del                 import              return
    as                  elif                in                  try
    assert              else                is                  while
    async               except              lambda              with
    await               finally             nonlocal            yield
    break               for                 not
```
----
# Data Types

1. Numbers
2. String
3. Boolean
4. None

### Numbers
        Python has three type of numbers.
  1. **Integer**
        Integers can be of any length; it is only limited by the memory available.
        ``` python
        
        >>> a = 2
        >>> type(a)
        <class 'int'>

        ```
  2. **Float**
        It can store number with a fractional part.
        ``` python
        
        >>> f = 3.14
        >>> type(f)
        <class 'float'>
        
        ```
  3. **Complex**
        Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part. 
        ``` python
        
        >>> c = 2 + 3j
        >>> type(c)
        <class 'complex'>
        >>>
        >>>
        >>> m = 25 - 3.14j
        >>> type(m)
        <class 'complex'>
        
        ```

### String
        A string consists of a sequence of one or more characters, which can include letters, numbers, and other types of characters. A string can also contain spaces.+

``` python
        >>> name = "Skill Disk"
        >>> type(name)
        <class 'str'>
        >>>
        >>>place = 'Bangalore'
        >>> type(place)
        <class 'str'>
        >>>
        >>> # can use Single quotes or Double quotes to represent strings.
        >>>
        >>> # MULTILINE STRING
        >>> address = ''' 
        ... #333, 2nd Floor,
        ... Dr Rajkumar Road, 
        ... Rajajinagar, 6th block,
        ... Bangalore - 560010
        ... '''
        >>> # Multiline strings can be denoted using triple quotes, ''' or """.               

```

### Boolean
        A condition is really just a yes-or-no question, the answer to that question is a Boolean value, either True or False. The Boolean values, True and False are treated as reserved words.
``` python
        
        >>> condition = True
        >>> type(condition)
        <class 'bool'>
        >>> # Boolean type has only two values. True False
        
```


### None
        None is another special data type in Python. None is frequently used to represent the absence of a value.
        
``` python
        
        >>> x = None
        >>> type(x)
        <class 'NoneType'>
        
```

---
# Operators
        These are special symbols which help the user to carry out operations like addition, subtraction, etc.
* Arthmetic operators.
* Assignment operators.
* Logical operators.
* Comparison operators.
* Bitwise Operators.

### Arthmetic Operators
| Operator | Operator Name | Example |
| :---: | --- | --: |
| + | Addition operator |  |
| - | Subtraction operator  |  |
| * | Multiplication operator |  |
| / | Division operator |  |
| % | Modulus operator |  |
| ** | Exponent operator |  |
| // | Floor division operator |  |


### Assignment Operators
| Operator | Operator Name | Example |
| :---: | --- | ---: |
| = | Assignment |  |
| += | Addition Assignment |  |
| −= | Subtraction Assignment |  |
| *= | Multiplication Assignment |  |
| /= | Division Assignment  |  |
| **= | Exponentiation Assignment |  |
| //= | Floor division Assignment |  |
| %= | Remainder Assignment |  |


### Logical Operators
| Operator | Operator Name | Example |
| :---: | --- | ---: |
| and | Logical AND |  |
| or | Logical OR |  |
| not | Logical NOT |  |


### Comparision Operators
| Operator | Operator Name | Example |
| :---: | --- | ---: |
| == | Equal to |  |
| != | Not Equal to  |  |
| > | Greater than |  |
| < | Lesser than |  |
| >= | Greater than or equal to  |  |
| <= | Lesser than or equal to |  |


### Bitwise Operators
| Operator | Operator Name | Example |
| :---: | --- | ---: |
| & | Binary AND  |  |
| \| | Binary OR  |  |
| ^ | Binary XOR |  |
| ~ | Binary Ones Complement |  |
| << | Binary Left Shift  |  |
| >> | Binary Right Shift |  |

----
# Comments
        A comment is a text that describes what the program or a particular part of the program is trying to do and is ignored by the Python interpreter.

#### Single line Comment
        In Python, use the hash (#) symbol to start writing a comment. 

``` Python
        >>> # This is Single line comment
```
#### Multiline Comment
        Use the hash (#) symbol at the beginning of each line.
        OR
        Use Triple quotes, ( ''' or  """ ) 

``` Python
        >>> # This is Single line comment
        >>> # Adding hash (#) again to the next line makes it Multiline comment. 
        >>>
        >>>
        >>> ''' Multiline comment can 
        ... also be represented by using thriple quotes.
        ... Usually this type of commenting is used 
        ... to represent DOC Strings in Python'''
        >>> 
```
---


Connect with us on <a target="_blank" href="https://t.me/skilldisk/"><img style="max-width: 30px;" src="https://img.icons8.com/color/2x/telegram-app.png" alt="Telegram"></a>
<a target="_blank" href="https://www.youtube.com/channel/UC41IWICHdLr7uCeeOCPFnpQ"><img style="max-width: 30px;" src="https://img.icons8.com/office/2x/youtube.png" alt="Youtube"></a>
<a target="_blank" href="https://www.facebook.com/skilldisk"><img style="max-width: 30px;" src="https://img.icons8.com/fluent/96/facebook-new.png" alt="facebook"></a>
<a target="_blank" href="https://twitter.com/skilldisk"><img style="max-width: 30px;"
src="https://img.icons8.com/fluent/96/twitter.png" alt="Twitter"></a>  
<a target="_blank" href="https://github.com/skilldisk"><img style="max-width: 30px;"
src="https://img.icons8.com/fluent/96/github.png" alt="GitHub"></a>
