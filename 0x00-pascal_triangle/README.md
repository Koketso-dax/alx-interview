#### Python algorithm for pascal triangle

## Solution:

    [1.] If n is less than or equal to 0, return an empty list.
    [2.] Initialize a variable triangle as a list containing a single list [1].
    [3.] For i in the range from 1 to n (exclusive):
        * a. Initialize a variable row as a list containing a single element 1.
        * b. For j in the range from 1 to i (exclusive):i. Append the sum of the elements at indices j-1 and j of the previous row (triangle[i-1]) to row.
        * c. Append a 1 to row.
        * d. Append row to triangle.
    [4.] Return the triangle list.
