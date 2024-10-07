#### Interview Challenge: Lockboxes problem

Problem breakdown:

<p> We are required to write a function that will take as input a list of lists, each of these lists is to be treated like a box. A single element in the list is equivalent to a key for a box corresponding to its index location. For this specific case we assume the first box ([0]) is always open. The function must then determine if the input list of list has a key for every element and return `True` if so and `False` otherwise. Key duplicates are possible and the boxes can have a variety of sizes. e.g </p>

<code>
[ [1], [2], [3], [4], [] ]
</code>

<p> In this case the output should be `True` because each list (box), a key (number) exists for each list from 0 to (n-1) with n = 5 in this case. The final box does not have a key so this list of lists can be traversed in a linear pattern however this will not always be the case. Another example: </p>

<code> [ [1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6] ] </code>

<p> This case should also return `True` because if we evaluate for each key from indeces 0 to (n - 1), we have a series of paths that eventually allow all the boxes to be opened:
    - [0] is open.
    - [0] has the connections ` [0] -> [1] `, ` [0] -> [4] `, 
</p>
