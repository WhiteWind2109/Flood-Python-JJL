# CUED Part IA Flood Warning System

_by Qiaochu Jiang, Junteng Li, and Dongcheng Jiang_

This is the Part IA Lent Term computing activity  at the Department of
Engineering, University of Cambridge.

The activity is documented at [http://cued-partia-flood-warning.readthedocs.io/](http://cued-partia-flood-warning.readthedocs.io/)

---

## Demonstration Guide

First of all, clone this repository and enter the repository directory in command line:

```sh
git clone https://github.com/JasonLiJT/Flood-Python-JJL.git
cd Flood-Python-JJL/
```

To run the demonstration codes, type:

```sh
python Task**.py
```

If you are working on a computer that has Python 2 and Python 3 installed, depending on your configuration you may need to use:

```sh
python3 Task**.py
```

## Test Guide

### The pytest module

To run tests, you need [pytest](http://docs.pytest.org/). If you have installed Anaconda, pytest comes with it. If you hate Anaconda, use the following command to install pytest:

```sh
pip install pytest
```

If you are working on a computer that has Python 2 and Python 3 installed, depending on your configuration you may need to use:

```sh
pip3 install pytest
```

### Run tests

To run all tests in all test_*.py files in this directory, use:

```sh
py.test .
```

To run all test in the file test_data.py:

```sh
py.test test_data.py
```

pytest will print a summary of the number of tests run, with the number that pass and the number that fail.

If you are working on a computer that has Python 2 and Python 3 installed, depending on your configuration you may need to use:

```sh
python3 -m pytest test_data.py
```

to run the tests.