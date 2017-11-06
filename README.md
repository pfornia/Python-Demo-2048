# 2048

A simple python implementation of a console-based version of 2048, a popular video game created by Gabriele Cirulli: 

https://itunes.apple.com/us/app/2048/id840919914?mt=8 

https://play.google.com/store/apps/details?id=com.digiplex.game&hl=en

## Getting Started

Download the repository. Navigate to the repo. Run the line:

```
python 2048.py
```

The game is played on a 4-by-4 grid:

_        _        _        _

_        _        _        4

_        2        _        _

_        _        _        8

A underscore indicates a blank space. A number indicates a non-blank space. The W-A-S-D keys are used as arrow keys. A directional move will shift all existing numbers as far as possible in that direction. Two identical numbers that collide will merge into a single space with a value equal to their sum. After each move, a new number (2 or 4) will populate in one of the blank spaces randomly. An attempted move that does not move any pieces does not count, and does nothing.

The player loses if all blank spaces fill without winning.

The player wins if any space holds the value 2048.

The Q-key will exit at any point.

### Prerequisites

Python 3

## Authors

* [**Paul Fornia**](https://github.com/pfornia)

<!--
## License

TBD

-->