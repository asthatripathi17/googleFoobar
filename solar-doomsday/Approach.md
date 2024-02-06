# Problem Statement
Write a function solution(area) that takes as its input a single unit of measure representing the total area of solar panels you have (between 1 and 1000000 inclusive) and returns a list of the areas of the largest squares you could make out of those panels, starting with the largest squares first. So, following the example above, solution(12) would return [9, 1, 1, 1].

## Test Cases:
Your code should pass the following test cases.Note that it may also be run against hidden test cases not shown here.

Input: 12</br>Output: 9,1,1,1

Input: 15324</br>Output: 15129,169,25,1

## Approach:

1. **Understanding the Problem**:
   - The problem statement describes a scenario where we are given an integer representing the area of a solar square. We need to decompose this area into the sum of the largest possible square numbers.
   - The goal is to find the largest possible square numbers whose sum equals the given area.

2. **Initial Observation**:
   - Since we are looking for the largest square numbers, it's intuitive to start with the largest possible square and subtract it from the area. We repeat this process until the area becomes zero.

3. **Thought Process**:
   - We start with the given area.
   - At each step, we find the largest square number less than or equal to the remaining area.
   - We subtract this square number from the remaining area and add it to our result list.
   - We continue this process until the remaining area becomes zero.

4. **Solution Approach**:
   - We can approach this problem using a loop:
     - While the remaining area is greater than 0:
       - Find the largest square number less than or equal to the remaining area.
       - Subtract this square number from the remaining area and add it to the result list.
   - Return the result list containing the largest square numbers.

5. **Edge Cases**:
   - We need to handle the case when the remaining area becomes 1. In this case, we simply add 1 to the result list.

6. **Implementation**:
   - We can implement this solution in multiple languages like C++, Java, or Python, using appropriate data structures and looping constructs.
   - The key is to accurately determine the largest square number less than or equal to a given area, which can be achieved through iterative calculation or mathematical manipulation.

7. **Complexity Analysis**:
   - The time complexity of the solution depends on the approach used to find the largest square number at each step. In general, it can be considered linear or slightly superlinear due to the iterative nature of the solution.
   - The space complexity is also linear, as we need to store the result list containing the largest square numbers.

