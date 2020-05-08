# Elementary Cellular Automaton

Elementary cellular automata have two possible values for each cell (0 or 1), and rules that depend only on nearest neighbor values. for more info:

https://mathworld.wolfram.com/ElementaryCellularAutomaton.html

It has been created with Pygame: https://www.pygame.org/

# Instalation:

The use of a virtual environment is recommended:

```
pip install requirements.txt
```

## How to use it:

Launch the code with a random rule:

```
python wolfram_automata.py
```

Pressing ```ENTER``` you can stop or run the simulation.

Optional flag ```-g``` creates one gif image.  

```
python wolfram_automata.py -g
```

With the optional flag ```-r XX``` where XX is a integer between 0 and 255, you can run a certain rule:

```
python wolfram_automata.py -r 30
```


## Examples:

Here you can seen some examples created with this code:

### Rule 30:

Rule 30 is described here:
https://mathworld.wolfram.com/Rule30.html

![](rule30.gif)

### Rule 90:

Rule 90 is described here:
https://mathworld.wolfram.com/Rule90.html

![](rule90.gif)

### Rule 94:

Rule 94 is described here:
https://mathworld.wolfram.com/Rule94.html

![](rule94.gif)
