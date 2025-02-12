Python
------
>Survey of Python 3 features and libraries, with a strong focus on using type hints.

>Highlights include Expression, fastapi, pydantic, requests and sqlite3.

Warning
-------
>Using pydantic and fastapi is problematic. Installs work. Yet imports don't always work. Yet scripts work!

>Mypy and Pylance might be part of the problem. Because pip3 install and upgrade of dependencies works!

>So I uninstalled MyPy. Yet, as expected, Pylance still does not recognize fastapi and pydantic imports.

>Yet, a day ago, I experienced no fastapi or pydantic import errors. Rebuilding the venv has not helped.

>Clearly, Python ***desperately*** needs a proper build-package-typer management tool!

Python Repository
-----------------
* [PyPi](https://pypi.org/)

Development
-----------
>Install a MacOS Python development environment.
1. Install [Homebrew](https://brew.sh/)
2. brew install python@3.13
3. Install [VSCode](https://code.visualstudio.com/)
4. Install VSCode Python Microsoft Extensions: Python, Python Debugger, Pylance

Virtual Env
-----------
>Setup virtual environment. See [VE Setup](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
1. python3.13 -m venv venv
2. source venv/bin/activate
3. pip3 install --upgrade pip
4. pip3 install Expression pydantic requests
5. pip3 install "fastapi[standard]"
6. pip3 list
7. pip3 freeze > **requirements.txt**

Install Dependencies
--------------------
>To install dependencies in **requirements.txt**:
1. pip3 install -r requirements.txt

Upgrade Dependencies
--------------------
>To upgrade dependencies in **requirements.txt**:
1. pip3 install --upgrade -r requirements.txt

Run
---
>To run a script, replace *.py with a source file name:
1. python3.13 ./src/*.py

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
9. [2025.1.21] Added insertion sort.
10. [2025.1.21] Added queue and stack.
11. [2025.1.26] Added pydantic validation.
12. [2025.1.26] Enhanced pydantic validation.
13. [2025.1.27] Added fastapi.
14. [2025.1.28] Added sqlite3.
15. [2025.1.28] Added unittest.

Big O
-----
1. O(1)     - constant time
2. O(log N) - logarithmic time
3. O(N)     - linear time
4. O(N2)    - quadratic time
5. O(2^n)   - exponential time
6. O(n!)    - factorial time

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