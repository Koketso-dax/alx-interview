#### Interview Challenge: Lockboxes problem

Problem breakdown:

<p> We are required to write a function that will take as input a list of lists, each of these lists is to be treated like a box. A single element in the list is equivalent to a key for a box corresponding to its index location. For this specific case we assume the first box ([0]) is always open. The function must then determine if the input list of list has a key for every element and return `True` if so and `False` otherwise. Key duplicates are possible and the boxes can have a variety of sizes. e.g </p>

<code>
[ [1], [2], [3], [4], [] ]
</code>

<p> In this case the output should be `True` because each list (box), a key (number) exists for each list from 0 to (n-1) with n = 5 in this case. The final box does not have a key so this list of lists can be traversed in a linear pattern however this will not always be the case. Another example: </p>

<code> [ [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6] ] </code>

<p> This case should also return `True` because if we evaluate for each key from indeces 0 to (n - 1), we have a series of paths that eventually allow all the boxes to be opened. N.B: we will ignore keys we have already encountered:
    - [0] is open.
    - [0] has keys for [1], [4] and [6]
    - [1] has a key for [2]
    - [4] has a key for [3]
    - [3] has a key for [5] 
</p>

<p> With this all the boxes have been opened. Some boxes we pointless to explore because at the point of execution where they were encountered, the keys they contained were already acquired. Now for the case were not all the boxes are open: </p>

<code> [ [1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6] ] </code>

<p> In this case the function should return `False` because we only have keys for 0 to 2 and 4. 4 is empty and most of the keys repeat values we have already explored. Furthermore there is no way to reach nodes 3, 5 and 6:
    - [0] is open.
    - [0] has keys for [1] and [4]
    - [1] has a key for [2]
    - [4] is empty    
</p>

Solution:

<p> We will perform the same followed in the above examples with some additional checks:
    - Check if `boxes` is not None and is of type list.
    - Initialize a list of `unlocked_boxes` with [0] as the only value.
    - For each unlocked box, append keys to `unlocked_boxes` if it the key is not already in the list and `0 < key < (n - 1)`
    - After iterating through all the available (reachable) boxes, check if `unlocked_boxes`.count() == len(boxes).
    - Return True if so and False otherwise.
</p>
