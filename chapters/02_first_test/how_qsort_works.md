# How does the qsort function work?
In the first few samples, we're using a sorting function called "qsort".

Although it's not important to understand how it works for the purposes of learning property-based testing, some readers are interested so I'm writing the description here.

# High level

*(if you're familiar with sorting algorithms - `qsort` is a quicksort variation that always uses the first element as the pivot)*
 

**`qsort` a recursive sorting function**.

## Recursion stop condition
If len(list) < 2: Return the input list 

Reason: Any list shorter than 2 is already sorted, because it’s either empty or one number.

## Recursion step
*Note: we're only here if the list has more than on element*

Break the list into 2 parts:
1. The number in index 0 (`first_item`).
2. The rest of the list (`rest_of_list`).

Now Go over `rest_of_list` and divide it into two lists: 
1. `smaller_than_first`: all the numbers that are smaller-equal than first_item, and 
2. `larger_than_first`: all the numbers that are larger than first_item.

Because we need to return, a sorted list, all numbers in `smaller_than_first` must appear before `first_item` and all the items in `larger_than_first` must appear after `first_item`.

But this is not enough: `smaller_than_first` and `larger_than_first` are not sorted internally.

So we’ll recursively call `qsort` and sort them, and then concatenate the results. So the return value will be:
`qsort(smaller_than_first) + [first_item] + qsort(larger_than_first)`


# So again, in short:

1. Take the 1st number and the rest of the list.
2. Put all the numbers smaller than that number before it and all the numbers larger than that number after it.
3. Internally sort the smaller numbers and the larger numbers by recursively calling the function.
