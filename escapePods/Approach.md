# Problem Statement
Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function solution(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step. There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:</br>


entrances = [0, 1]</br>
exits = [4, 5]</br>
path = [ </br>
[0, 0, 4, 6, 0, 0], # Room 0: Bunnies</br>
[0, 0, 5, 2, 0, 0], # Room 1: Bunnies</br>
[0, 0, 0, 0, 4, 4], # Room 2: Intermediate room</br>
[0, 0, 0, 0, 6, 6], # Room 3: Intermediate room</br>
[0, 0, 0, 0, 0, 0], # Room 4: Escape pods</br>
[0, 0, 0, 0, 0, 0], # Room 5: Escape pods</br>
]

Then in each time step, the following might happen:</br>
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3</br>
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3</br>
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5</br>
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5</br>

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step. (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final solution remains the same.)

## Test Cases:

Input: [0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]</br>
Output: 6 </br>

![unnamed (1)](https://github.com/asthatripathi17/googleFoobar/assets/121253696/b44486f7-4b7e-408c-afee-6b78023d7d9a)

Input: [0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]</br>
Output: 16</br>

![unnamed](https://github.com/asthatripathi17/googleFoobar/assets/121253696/91bb3283-d53b-44da-9b6e-fc48de5e96b6)


## Approach:
### Concept Used: A Variation of the Max-Flow Problem

This problem can be viewed as a variation of the max-flow problem because it involves finding the maximum amount of flow that can be sent from a set of sources (entrances) to a set of sinks (exits) through a network with capacities on its edges (corridors).

- Sources (Entrances) - The starting room numbers of the groups of bunnies serve as sources from which the flow of bunnies originates.

- Sinks (Exits) - The room numbers of the escape pods represent the sinks or destinations where the flow of bunnies needs to reach.

- Flow Network - The rooms and corridors together form a flow network, where each room corresponds to a vertex and each corridor corresponds to an edge with a capacity representing the maximum number of bunnies that can pass through it.

- Maximum Flow - The goal is to find the maximum flow of bunnies from the entrances to the exits, respecting the capacities of the corridors. This maximum flow represents the maximum number of bunnies that can safely make it to the escape pods at each time step.

By framing the problem in this way, we can apply algorithms designed to solve the max-flow problem to efficiently find the solution. These algorithms determine how much flow can be sent through the network while satisfying the capacity constraints and ensuring that no more bunnies are sent than can be accommodated by the corridors.


### Solution Approach:

This problem is a variation of the max-flow problem, where the goal is to find the maximum flow of bunnies from the entrances to the exits through the corridors. We can solve it using the Ford-Fulkerson algorithm or any other maximum flow algorithm.

1. **Build the Flow Network** - Convert the given input into a flow network representation. Each room represents a vertex, and each corridor represents an edge with a capacity representing the maximum number of bunnies that can pass through.

2. **Find the Maximum Flow** - Use an algorithm like Ford-Fulkerson to find the maximum flow from the entrances to the exits in the flow network. This algorithm iteratively augments paths from the source (entrances) to the sink (exits) until no more augmenting paths exist.

3. **Calculate the Total Flow** - Once the maximum flow is found, sum up the flow leaving the entrances (source) to determine the total number of bunnies that can reach the escape pods.

4. **Return the Result** - Return the total flow as the solution.

This approach ensures that we maximize the number of bunnies reaching the escape pods while respecting the capacities of the corridors.

### Ford-Fulkerson Algorithm Implementation

- **Breadth-First Search (BFS):**

  The `searching_algo_BFS` function performs a BFS traversal on the residual graph (graph with remaining capacities) to find a path from the source to the sink.
  - It updates the `parent` array to keep track of the paths discovered during the BFS traversal.
  - If a path from the source to the sink is found, it returns True along with the path.

- **Ford-Fulkerson Algorithm:**

  The `ford_fulkerson` function repeatedly applies BFS to find augmenting paths and updates the flow along those paths until no more augmenting paths can be found.
  - It calculates the maximum flow by summing up the flow along all augmenting paths.
  - For each augmenting path found, it updates the residual capacities of the edges in the flow graph.

- **Main Solution Function (`solution`):**

  - Constructs the flow graph based on the input corridors (`path`), entrances, and exits.
  - Sets infinite capacities for edges from the source to entrances and from exits to the sink to ensure that all bunnies can flow through these points.
  - Calls the `ford_fulkerson` function to find the maximum flow from the source to the sink.
  - Returns the maximum flow, which represents the maximum number of bunnies that can escape.

Overall, my solution efficiently solves the problem by transforming it into a max-flow problem and applying the Ford-Fulkerson algorithm to find the maximum flow through the flow network. This approach ensures that the maximum number of bunnies can safely make it to the escape pods.
