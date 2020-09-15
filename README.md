# DotPruner [![DotPruner Python package Status](https://github.com/ansonmiu0214/DotPruner/workflows/tests/badge.svg)](https://github.com/ansonmiu0214/DotPruner/actions)
Pruning redundant nodes from DOT graphs

> Go from...
> ![DOT graph before pruning](assets/before.png)
> 
> ...to...
> ![DOT graph after pruning](assets/after.png)

## Getting Started

Prerequisites:
* `python3.x`
* `python3-venv`

```bash
# Create virtual environment
$ python3 -m venv venv

# Enter virtual environment
$ source venv/bin/activate

# Install dependencies
(venv) ... $ pip install -r requirements.txt
```

## Usage

### CLI

Prune graph "in-place":
```bash
python3 -m dotpruner path/to/original/graph.dot
```

Use `--dest` or `-d` to specify destination for new graph:
```bash
python3 -m dotpruner path/to/original/graph.dot --dest path/to/new/graph.dot
```

Use `--overwrite` or `-o` to overwrite existing file in destination:
```bash
python3 -m dotpruner path/to/original/graph.dot -d path/to/new/graph.dot --overwrite
```

### API
```python

```


## Tests
```bash
python3 -m unittest discover dotpruner.tests --verbose
```
