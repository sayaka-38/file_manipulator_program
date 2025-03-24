# file_manipulator_program

## Overview

This is a Python script for learning file manipulation.  
It takes a file path as an argument and can perform 4 types of file operations.  
It was created with built-in as much as possible while interacting with AI.  

## How to Use
### 1. reverse
Takes a file from `inputpath` and creates a new file in `outputpath` with the contents of `inputpath` reversed.  
```command
reverse inputpath outputpath
```
  

### 2. copy
Creates a copy of the file at `inputpath` and saves it as `outputpath`.  
```command
copy inputpath outputpath
```
  

### 3. duplicate-contents
Duplicates the contents of the file at `inputpath` and appends the duplicated contents `n` times in the file at `inputpath`.
```command
duplicate-contents inputpath n
``` 
  
### 4. replace-string
Searches for the string `oldstring` in the contents of the file at `inputpath` and replaces all occurrences of `oldstring` with `newstring`.
```command
replace-string inputpath oldstring newstring  
``` 