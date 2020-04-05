# Google Code Jam

## Develop

### Pre-requisites

- Python 3
- `pip`

### Setup

```console
pip install --upgrade pipenv
pipenv shell
pipenv install --dev
```

### Test

```console
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.7.7, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
rootdir: ${HOME}/google-code-jam
collected 7 items

tests/cj2019/foregone_solution_test.py .                                 [ 14%]
tests/cj2020/qualif/incidium_test.py ...                                 [ 57%]
tests/cj2020/qualif/nesting_depth_test.py .                              [ 71%]
tests/cj2020/qualif/parenting_partnering_returns_test.py .               [ 85%]
tests/cj2020/qualif/vestigium_test.py .                                  [100%]

============================== 7 passed in 0.07s ===============================
```

### Run

```console
$ python cj2020/qualif/incidium.py < tests/cj2020/qualif/incidium.txt
Case #1: POSSIBLE
1 3 2
3 2 1
2 1 3
Case #2: IMPOSSIBLE
```

## 2020

- [Leaderboard](https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27)
- Qualification Round: #2151 / 40697
