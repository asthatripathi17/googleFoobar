# Problem Statement
To trick the system, you'll need to write a program to return the same security checksum that the bunny trainers would have after they would have checked all the workers through. Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the trainers at the checkpoint have found ways to quicken the pass-through rate. Instead of checking each and every worker coming through, the bunny trainers instead go over everyone in line while noting their worker IDs, then allow the line to fill back up. Once they've done that they go over the line again, this time leaving off the last worker. They continue doing this, leaving off one more worker from the line each time but recording the worker IDs of those they do check, until they skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and then take off for lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical order without any gaps.

For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:

``0 1 2 /``</br>
``3 4 / 5``</br>
``6 / 7 8``</br>

where the trainers' XOR (^) checksum is 0^1^2^3^4^6 == 2.
Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:

``17 18 19 20 /``</br>
``21 22 23 / 24``</br>
``25 26 / 27 28``</br>
``29 / 30 31 32``</br>

which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.

All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at least 1 worker long.
Write a function solution(start, length) that will cover for the missing security checkpoint by outputting the same checksum the trainers would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the line (length) before the automatic review occurs, so your program must generate the proper checksum with just those two values.

## Test Cases:
Input: (0, 3)</br>
Output: 2

Input: (17, 4)</br>
Output: 14

## Approach:

The goal is to compute the XOR checksum for a given range of worker IDs.

**Step 1**: Define a function xor_seq(start, end) to calculate the XOR sequence for a given range of IDs. This function will determine the XOR value of the IDs within the specified range.

**Step 2**: Define the main function solution(start, length) to compute the XOR checksum for the entire line of workers. This function iterates over each segment of the line, calculates the XOR sequence for each segment, and updates the checksum accordingly.

**Step 3**: Within the main function, iterate over each segment of the line:
- Calculate the XOR sequence for the current segment using the xor_seq function.
- Update the checksum by XORing it with the XOR sequence of the current segment.

**Step 4**: Return the final checksum computed after processing all segments of the line.

This approach efficiently calculates the XOR checksum by considering the XOR sequence for each segment of the line. By breaking down the line into smaller segments, the solution avoids the need to iterate over each individual worker ID, reducing the time complexity of the algorithm. This approach is suitable for solving the problem within the given constraints and efficiently computes the required checksum.

