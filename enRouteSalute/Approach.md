# Problem Statement
Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example: "--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function answer(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.

## Test Cases:
Input: ">----<"
</br>Output: 2

Input: "<<>><"
</br>Output: 4

Input: "--->-><-><-->-"
</br>Output: 5

## Approach:
This solution works by observing the interaction between employees walking in opposite directions. Whenever an employee walking to the left encounters an employee walking to the right, they exchange salutes. The problem can be solved by iterating through the string and keeping track of the number of salutes that occur when employees walking in opposite directions meet each other. By counting the number of such encounters and doubling it, we can determine the total number of salutes exchanged during the walk along the hallway. 

1. **Iteration through the string**: Since we need to examine each character in the hallway string to determine when salutes occur, iterating through the string is a natural approach.

2. **Tracking the movement of employees**: By using a variable rightWalker to track the number of employees walking to the right encountered so far, we can determine the number of salutes that occur when an employee walking to the left encounters employees walking to the right.

3. **Counting salutes**: Whenever an employee walking to the left encounters employees walking to the right, salutes occur. We can count the number of such salutes and multiply by 2 to account for both employees saluting each other.

This approach efficiently solves the problem by considering the interactions between employees walking in opposite directions and counting the number of salutes that occur.
