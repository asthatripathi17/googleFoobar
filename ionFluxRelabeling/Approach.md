# Problem Statement
Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

```
     7
   /   \
  3     6
 / \   / \
1   2 4   5
```

## Test Cases:
Inputs:
(int) h = 3, (int list) q = [7, 3, 5, 1]
</br>Output: (int list) [-1, 7, 6, 3]

Inputs:
(int) h = 5, (int list) q = [19, 14, 28]
</br>Output: (int list) [21, 15, 29]

## Approach:

1. **Understanding the Problem**:
   - The problem describes a scenario where we have a perfect binary tree of converters, represented by a tree structure with nodes labeled with distinct positive integers.
   - We are given the height of the tree and a list of positive integers representing different flux converters in the tree.
   - The task is to find the converter sitting on top of each converter in the given list, or return -1 if there is no such converter.

2. **Initial Observation**:
   - The problem involves traversing a perfect binary tree to find the parent node of each given converter node in the list.
   - For a perfect binary tree of height 'h', each node (except the root) has a parent node, making it possible to determine the parent node for any given converter.

3. **Thought Process**:
   - We start by constructing the perfect binary tree based on the given height.
   - We then iterate through the list of converters.
   - For each converter, we traverse the tree to find its parent node.
   - If a parent node exists, we add its label to the result list; otherwise, we add -1.

4. **Solution Approach**:
   - We can approach this problem using tree traversal techniques, such as depth-first search (DFS).
   - We first construct the perfect binary tree of converters using a recursive function.
   - Then, for each converter in the given list:
     - We traverse the tree recursively to find its parent node.
     - Since the perfect binary tree is constructed in a left-to-right manner, we start the traversal from the root node and prioritize the right subtree.
     - This approach ensures that we always explore the right subtree first, allowing us to efficiently find the parent node of the given converter.
     - If a parent node exists, we add its label to the result list; otherwise, we add -1.
   - Finally, we return the result list containing the labels of the parent converters.

5. **Implementation**:
   - We can implement this solution in Python using a class-based approach to represent the tree nodes and recursive functions for tree construction and traversal.
   - The key is to accurately traverse the tree and find the parent node for each given converter node.

6. **Complexity Analysis**:
   - The time complexity of the solution depends on the height of the perfect binary tree and the number of converters in the given list.
   - Since we traverse the tree for each converter, the overall time complexity can be considered linear or slightly superlinear.
   - The space complexity is also linear, as we need to store the result list containing the labels of the parent converters.
