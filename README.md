Intuition of how the algorith works:

Ants are traveling from a starting location to the final, visiting all cities. We can imagine they return using the same paths, and deposit pheromone on the way back. They deposit more pheromone on shorter distances, then long ones, and only on the path they travelled. An individual ant makes decisions on what city to go to based on level of pheromone on the path and the distance to the nearest city.

In more detail:

1) We select N number of ants.
2) We initialize matrix of pheromone depostits, its the same shape as the distance matrix. And coorinates respond to the same cities. If `distances[2,5] = 35` the distance from 2 to 5 is 35, and if `pheromone[2,5] = 0.8` the level of pheromone deposited on path between 2 and 5 is 0.8. The pheromone matrix is initialize with small variables all of the same value.
3) First generation makes decision using this:

```
city_to_city_score = pheromone ** alpha * (1.0 / distance) ** beta
```

alpha and beta act as weight on pheromone and distnace respecively. 

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

An ant keeps going from city to city according to the above chosing rule unil he visits all cities.

If we chose 20 ants to start with we will have 20 path at the end of this group of ants travelling generation.

Since in the initial step the pheromone levels are the same, the choices are made on distances + some noise. Randomized Greedy if you like. But we want to keep track of the successful routes, so ants deposit pheromene.

4) On the way back all ants or selected number of best ants deposit pheromone on the paths they travelled.

They deposit:

```
 1 / (distance between two cities)
```

For example:
an ant travelled a path: [ (0 -> 3) (distance: 8), (3 -> 5) (distnace: 2)]

0.125 units of pheromone would be deposited on ```pheromone[0,3] += 0.125``` and ```pheromone[3,5] += 0.5```

This is done to encourage ants to give more priority to shorter routes between cities.

5) The final peice, is that we have to let pheromone decay, so old pheormone does not confuse next generations of ants.
We just multiply the pheromone matrix by decay rate. Right after we deposit. Therefore pheromone that has been sitting for a while has been subject to many many decays and should be small.

6) Keep doing steps 3) 4) and 5) for n iterations. The second generation, will also take pheromone into account!








