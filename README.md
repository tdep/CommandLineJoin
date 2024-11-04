# Command Line Join

A command line program used to join two `.csv` files on a shared key. 

## Details

This program is an assignment for a Database course I am taking as part of my MS in Computer Science. The task is to 
write a command line program which joins two `.csv` files, taking inspiration from the `$join` command in Linux.

## Inputs

There are 4 accepted inputs:
1. `type`
   - The type of join to use.
   - Accepted inputs: 
       - `inner`: Also known as *"Nested Loop Join"*, for every row in the outer table (`A`), read the entirety of the inner 
     table (`B`) matching on the filter value (such as `a.id`). If the two values match, add the combination to the result set.
       - `merge`: Also known as *"Sort-Merge"*, sort both tables on a given key (such as `user_id`), and once sorted, merge the
     matching rows and add to the result set.
     - `hash`: Completed in two stages:
       - **Stage 1 - Build**: For the rows in the first table, generate a hash table using the given key (such as `user_id`), 
       and map all rows of the first table to the key.
       - **Stage 2 - Probe**: For the rows in the second table, find the corresponding key in the hash table and for each 
       row of that key from, combine the matching rows from the first table and add the combination to the result set.
2. `file1`
   - The first file to join.
   - Must be a `.csv` file.
3. `file2`
   - The second file to join.
   - Must also be a `.csv` file.
4. `option`
   - Additional options to manage how the data is handled.
   - Accepted inputs: 
     - `-e EMPTY`: Replace missing input fields with `EMPTY`

## Join Key

It is assumed that the first column of each file serves as the join key and therefore must match.

An alternative is to use the index of each row (`row_number`) to join two arbitrary sets of data.

## Considerations
Each type of join has advantages and disadvantages:
- **Nested Loop Join** - Simple but costly to implement regarding time complexity, O(N<sup>2</sup>), due to the use of
a nested loop. Good for small datasets.
- **Sort-Merge** - More advanced than the Nested Loop, has the advantage of sorting the data for in each table thus having
a better time complexity result of O(<em><b>N <sub>log</sub>N</b></em> ) since after the sort, we only traverse the tables once.
- **Hash Map Join** - The most complex of the three, can be the most efficient provided that the hashing is balanced.
Has the disadvantage of requiring more memory as a separate hash table is generated, but overall efficient for large 
datasets with a best-case time complexity of O(<b><em>N</em></b> ).