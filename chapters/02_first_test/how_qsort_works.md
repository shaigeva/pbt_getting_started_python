# How does the qsort function work?
In the first few samples, we're using a sorting function called "qsort".

Although it's not important to understand how it works for the purposes of learning property-based testing, some readers are interested so I'm writing the description here.

# High level
(if you're interested and know sorting algorithms - `qsort` is a quicksort variation that always uses the first element as the pivot)
 

`qsort` a recursive sorting function.

The stop condition is that if the list is shorter than 2 – qsort returns the input list (any list shorter than 2 is already sorted, of course – it’s either empty or one number).

If there’s more than one element, qsort breaks the list into 2 parts:

The number in index 0 (`first_item`).
The rest of the list (`rest_of_list`).
Now qsort goes over `rest_of_list` and divides it into two lists: all the numbers that are smaller-equal than first_item and all the numbers that are larger than first_item.

The result will be a sorted list, so all numbers in smaller_than_first must appear before first_item and all the items in larger_than_first must appear after first_item.

but `smaller_than_first` and `larger_than_first` are not sorted internally.

So we’ll recursively call `qsort` and sort them, and then concatenate the results:

`qsort(smaller_than_first) + [first_item] + qsort(larger_than_first)`
So again:

1. Take the 1st number and the rest of the list.
2. Put all the numbers smaller than that number before it and all the numbers larger than that number after it.
3. Internally sort the smaller numbers and the larger numbers by recursively calling the function.
