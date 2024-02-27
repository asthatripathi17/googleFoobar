# Problem Statement
Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k. The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

## Test Cases:
Input: (int list) l = [1, 1, 1]
</br>Output: (int) 1

Input: (int list) l = [1, 2, 3, 4, 5, 6]
</br>Output: (int) 3

## Approach:

1. **Observation:** We need to count the number of "lucky triples" in the given list. A lucky triple is a triplet (lst[i], lst[j], lst[k]) where i < j < k and lst[k] is divisible by lst[j], which in turn is divisible by lst[i]. 

2. **Iterative Approach:** To find lucky triples efficiently, we need to iterate through the list and check for each element lst[i], whether there exist elements lst[j] and lst[k] such that lst[j] divides lst[k] and lst[i] divides lst[j].

3. **Nested Loop:** We utilize nested loops to iterate through all possible combinations of lst[i], lst[j], and lst[k]. 

4. **Counting Lucky Triples:** For each lst[i], we count the number of elements lst[j] before it such that lst[i] divides lst[j]. Then, for each lst[i], we count the number of elements lst[k] after it such that lst[k] is divisible by lst[i]. The total count of lucky triples involving lst[i] is the product of these two counts.

5. **Incremental Counting:** We incrementally add the count of lucky triples found for each lst[i] to a cumulative count.

6. **Returning Result:** Finally, we return the total count of lucky triples found in the list.

This approach systematically checks each element of the list and identifies lucky triples by counting the number of suitable divisors before and after each element. By iterating through the list only once and employing efficient counting techniques, we can accurately determine the count of lucky triples without redundant computations.
