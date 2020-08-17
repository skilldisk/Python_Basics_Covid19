# FILES

    A file is a common storage unit in a computer, and all programs and data are written into a file and read from a file.


### Directories
    The folders, often referred to as directories, are used to organize files on computer.
    Directories store files and other directories while files stores the data

## Types of Files

1. Text file
2. Binary file

Files stores data in the form of binary, the bits in the text file represents characters, while the bits in the binary files represents custom data.

Eg:
| Text files | Binary files |
| :---: | :---: |
|html, css, svg, c, py, txt, md, csv, tsv, json | jpg, png, gif, mp3, mkv, avi, ppt, zip, mdb, exe, iso |
---
### Working with files

To open a file in python code, use
``` python
    file_handler = open('file', 'mode')
    
    # file ==> fileName.fileExtension
    # mode ==> Check below table
```

To Close a file opened by the python code
``` python
    file_handler.close()
```
If an exception occurs while performing some operation on the fle, then the code exits without closing the fle. In order to overcome this problem. File can be handled with try-except-finally block or using with statement.
``` python
    with open('file','mode') as f:
        # Statements here
        pass

```
##### Access modes fo files
| Mode | Description |
| :--: | -- |
| 'x' | * Creates a new file and perform write operation. <br> * If file already exists, the operation fails. |
| 'r' | * Read only mode. <br> * This is the default mode. |
| 'w' | * Write only Mode. <br> * If file doesn't exist it creates a new file. <br> * If file already exist it will overwrite the data. |
| 'a' | * Appending data at the end of file. <br> * If file doesn't exist it creates a new file. |
| 'r+' | Reading and Writing Mode |
| 'w+' | * Write and Read Mode.<br> * If file doesn't exist it creates a new file. <br> * If file already exist it will overwrite the data.|
| 'a+' | * Open file for reading and appending |
| 'rb' | * Opens the binary fle in read-only mode. |
| 'wb' | * Opens the fle for writing the data in binary format.|
| 'rb+' | * Opens the fle for both reading and writing in binary format. |

