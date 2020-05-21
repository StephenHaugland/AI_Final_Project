# AI_Final_Project

This is a repository containing an artificial intelligence final project.  It is a genetic algorithms project written in Python. The algorithm is loosely based on the principles of natural selection and evolution.  The goal was to create artificial bots that would navigate a maze, reproduce, and learn to improve navigation of the maze in successive generations. The key application of genetic algorithms to the field of AI is the ability of the algorithm to search a space of potential solutions to find optimal solutions to a given problem.  Given the right problem, a genetic algorithm can compute a predominant solution much quicker and with much more efficiency than a human.

## The maze

We used a 2 dimensional array to construct a grid of 0's and 1's.  The 1's on the grid represent maze obstacles and the 0's represent open space.  We utilize the Python Pygame library to draw the maze onto a popup screen.  The bots enter the maze on the far left side of the screen and the goal is to navigate through the maze obstacles to the exit on the far right hand side of the screen.

![Maze Screenshot](https://github.com/shaners1106/AI_Final_Project/blob/master/Images/Maze.PNG)

## Encoding

We initialize a seed population with an initial DNA consisting of completely random navigational directives.  We hold the "genes" in a 1 dimensional array.  Once the population size is predetermined a seed population of agents is initialized each given an initial random DNA sequence of instructions ('L', 'R', or 'F').

## Fitness Score

An agent's performance is evaluated based on a fitness score.  We used a simple distance formula so that agents who made it closer to the maze exit would receive a higher score.  We also rewarded agents who reached the exit in the least amount of instructions.

## Selection

A generation of agents expires when each agent has completed its full array of genetic instructions.  We use a roulette style selection process based off of probabilities.  Every agent of a given population has a statistical chance to enter the reproductive process, with agents with higher fitness scores having a higher probability of getting selected.  We order the agents by fitness score and delegate each agent a float value between 0 and 1 in ascending order with larger float values correlating to higher fitness scores.  We then randomly generate float values between 0 and 1 which correlate to the agents that we are going to select for reproduction.  This selection strategy favors higher fitness scores, but also doesn't completely eliminate lower fitness scores, which allows for more genetic variety being perpetuated throughout successive generations. We select half of the population to enter the crossover process. 

## Crossover

At this point the population enters the reproductive process. Because an agent's fitness score is tied to the order of an its movements, we desire to preserve this order in successive generations.  Therefore, we use a method of crossover reproduction called ordered crossover.  According to this strategy, we pull a random length strand of DNA from parent 1 from a random array starting index, we place this strand in the new_child DNA structure at the exact same starting index.  We then fill in the remaining DNA indices with the corresponding genes from parent 2.  The resulting child DNA array is an ordered mix of parent 1 and parent 2.

## Mutation

Mutation is critical for persistent genetic variety which helps your algorithm avoid local maxima.  Within the crossover process, we subject every new child to the possibility of mutation according to a random number generator that is tied to probabilities.  For the first 10 generations of agents, every new baby bot has a 15% chance of getting mutated.  For generations 11-20 every new baby bot has a 10% chance of getting mutated.  And every generation thereafter the baby bots have a 5% chance of mutation.  Our method of mutation is to pull a strand of DNA that is 10% of the total DNA sequence from a random location within the sequence and randomly generate completely new DNA instructions. 

### Authors

Shane Snediker: https://www.github.com/shaners1106

Stephen Haugland: https://www.github.com/StephenHaugland

 
