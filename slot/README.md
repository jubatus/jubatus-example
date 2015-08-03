Slot Machine Simulation
=======================

This is an example of jubabandit.
This example optimizes the cumulative reward of a sequence of slot machine plays by multi-armed bandit algorithm.
You can try various simulation settings by modifying config file(config/slot.conf).

## Preparation

- Install Jubatus 0.7.0 or later
- Install Jubatus Python Client
    - python 3.x is needed

## How to try

### Launch jubabandit server

```
jubabandit -f config/epsilon.json &
```

### Execute simulation

```
cd python
python slot.py
```

## Config file
### [common]
Set the basical settings of a simulation.
- iteration
    - The number of iteration of a simulation.

### [slots]
Set the slot machine information
These slot machines generate a reward from normal distribution with the probability of hit rate.
You can add as many slots as you like.
The formats are below:

```
slot_name = hit_rate,average,standard_deviation
ex.)
a = 0.1,50,10
```

