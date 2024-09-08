Python
------
Survey of Python 3 features and external modules.

Development
-----------
>Install a MacOS Python development environment.
1. Install [Homebrew](https://brew.sh/)
2. brew install python@3.12
3. brew install mypy
4. Install [VSCode](https://code.visualstudio.com/)
5. Install VSCode Python Microsoft Extensions: Python, Python Debugger, Pylance, MyPy Type Checker

Virtual Env
-----------
>Setup virtual environment. See [VE Setup](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
1. python3.12 -m venv venv
2. source venv/bin/activate
3. pip3 list
4. pip3 install --upgrade pip ( optional )
5. pip3 freeze > requirements.txt ( optional )

Dependencies
------------
>Install all dependencies listed in requirements.txt.
1. pip3 install -r requirements.txt

MyPy
----
>Type check all source files.
1. mypy ./src

Run
---
>Replace *.py with source file name.
1. python3.12 ./src/*.py

Releases
--------
1. Initial Release [2024.8.7]
2. Explored Expression Library [2024.8.8]
3. Enhanced Project ( files.dirs, exceptions, http.requests ) [2024.8.16]

Resources
---------
* [Python Org](https://www.python.org/)
* [W3C Python Tutorial](https://www.w3schools.com/python/)
* [Real Python](https://realpython.com/)
* [Python FP](https://www.kite.com/blog/python/functional-programming/)
* [Practial FP](https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming)
* [FP in Python](https://stackabuse.com/functional-programming-in-python/)
* [Expression Github](https://github.com/dbrattli/Expression)
* [Expression Tutorial](https://expression.readthedocs.io/en/latest/tutorial/introduction.html)
