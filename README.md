# Fall guys simulator
This python script creates histogram diagrams (as .png) for the probability of advancing in a round in the playstation game "fall guys". It is only applicable for the coop game mode.
The following can be variied in main:
- number of teams
- number of advancing teams
- how many simulations of the round (aka tries). More = more accurate probabilities
- round number for the diagram title

The images provided by the script help in estimating how likely it is to get qualified if you are behind the finish line and waiting for the round to end. This way, you can decide if it is worth to wait or not.

### Example
Here is a diagram for a common round 1 in fall guys coop mode:
![Histogram showcasing the probability of advancing based on the no of team points](histograms_round_1_10000000_tries.png)
In this example there is a total of 20 teams of which 14 advance. Looking at the graph one can deduce that you need 34 points to advance with an 80 % likelihood.