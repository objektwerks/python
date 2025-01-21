Python
------
Survey of Python 3 features and libraries, with a strong focus on using type hints.

Development
-----------
>Install a MacOS Python development environment.
1. Install [Homebrew](https://brew.sh/)
2. brew install python@3.13
3. brew install mypy
4. Install [VSCode](https://code.visualstudio.com/)
5. Install VSCode Python Microsoft Extensions: Python, Python Debugger, Pylance, MyPy Type Checker

Virtual Env
-----------
>Setup virtual environment. See [VE Setup](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
1. python3.13 -m venv venv
2. source venv/bin/activate
3. pip3 list
4. pip3 install --upgrade pip ( optional )
5. pip3 freeze > requirements.txt ( optional )

Python Repository
-----------------
* [PyPi](https://pypi.org/)

Install Dependencies
--------------------
>To install dependencies in requirements.txt.
1. pip3 install -r requirements.txt

Upgrade Dependencies
--------------------
>To upgrade dependencies in requirements.txt:
1. pip3 install --upgrade -r requirements.txt

MyPy
----
>To type check all source files:
1. mypy ./src

Run
---
>Replace *.py with a source file name.
1. python3.13 ./src/*.py

Big O
-----
1. O(1) - constant time
2. O(log N) - logarithmic time
3. O(N) - linear time
4. O(N2) - quadratic time
5. O(2^n) - exponential time

Releases
--------
1. [2024.8.7] Initial Release
2. [2024.8.8] Explored Expression Library
3. [2024.8.16] Enhanced Project ( files.dirs, exceptions, http.requests )
4. [2025.1.17] Added binary search, merge sort, quick sort, recursion and selection sort.
5. [2025.1.18] Added breadth first search.
6. [2025.1.19] Added depth first search.
7. [2025.1.20] Added Dijstra's algo.
8. [2025.1.21] Added bubble sort.

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