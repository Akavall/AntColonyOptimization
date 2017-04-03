Intuition of how the algorithm works:

Ants are traveling from a starting location to the final, visiting all cities. We can imagine they return using the same paths, and deposit pheromone on the way back. They deposit more pheromone on shorter distances, then long ones, and only on the path they traveled. An individual ant makes decisions on what city to go to based on level of pheromone on the path and the distance to the nearest city.

In more detail:

1) We select N number of ants.
2) We initialize matrix of pheromone deposits, it is the same shape as the distance matrix. And coordinates respond to the same cities. If `distances[2,5] = 35` the distance from 2 to 5 is 35, and if `pheromone[2,5] = 0.8` the level of pheromone deposited on path between 2 and 5 is 0.8. The pheromone matrix is initialize with small variables all of the same value.
3) Explore some paths:

Ant makes a decision on what city to go to using this:

```
city_to_city_score = pheromone ** alpha * (1.0 / distance) ** beta
```

alpha and beta act as weight on pheromone and distance respectively. 

We calculate ```city_to_city_score``` for all the available cities (we are ignoring cities we already visited, because we can't go back to them).

The probability of going to the next city is:

```
prob_of_going_to_city(i) = city_to_city_score(i) / sum_of_all_available_city_to_city_scores
```

For example, if an ant is at city 2, and available cities are 4,7,8. We computed the scores for those cities as:

```
{4: 0.2, 7: 0.4, 8: 0.8}
```

The probability of going to 4 is ```0.2 / (0.2 + 0.4 + 0.8) = 0.142857``` and so on.

An ant keeps going from city to city according to the above choosing rule until he visits all cities.

If we chose 20 ants to start with, we will have 20 paths at the end of this group of ants traveling generation.

Since in the initial step the pheromone levels are the same, the choices are made on distances + some noise. Randomized Greedy if you like. But we want to keep track of the successful routes, so ants deposit pheromone.

4) On the way back all ants or selected number of best ants deposit pheromone on the paths they traveled.

They deposit:

```
 1 / (distance between two cities)
```

For example:
an ant traveled a path: [ (0 -> 3) (distance: 8), (3 -> 5) (distance: 2)]

0.125 units of pheromone would be deposited on ```pheromone[0,3] += 0.125``` and ```pheromone[3,5] += 0.5```

This is done to encourage ants to give more priority to shorter routes between cities.

5) The final piece, is that we have to let pheromone decay, so old pheromone does not confuse next generations of ants.
We just multiply the pheromone matrix by decay rate. Right after we deposit. Therefore pheromone that has been sitting for a while has been subject to many many decays and should be small.

6) Keep doing steps 3) 4) and 5) for n iterations. 







