import numpy as np

from ant_colony import AntColony

distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])

ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print "shorted_path: {}".format(shortest_path)

# ([(0, 2), (2, 3), (3, 4), (4, 1), (1, 0)], 16.0)
