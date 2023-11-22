# SHELPY

Flexible functional-style shell pipelines in Python.

## Setup
```shell
    pip install .
```

## Examples
```shell
    shelpy-hi
```
```text
Hello world from shelpy!
```

```shell
range 1 10 | map 'x -> int(x) * 10' | filter 'x -> int(x) >= 50'
```

```text
50
60
70
80
90
```