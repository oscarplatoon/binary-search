## Binary Search

**The goal of binary search is to find the index of a passed in value compared to an array of strings or integers.**

Let's say that our set of values is shaped a little differently from our previous linear search challenge. Use this code to generate it:

```ruby
values = (1..10000).to_a.sample(1000).sort
```

We now have a total of 1000 unique values between 1 and 10,000 and, most importantly, they're sorted.

Your challenge is to write a binary search. Here's the basic premise of the algorithm:

1. Say you're searching for a value `t` in a search set of `values`
2. Find the middle value in `values` we'll call `m`
3. If `t` is equal to `m` then your target is found
4. If `t` is less than `m`, your new search set is the half of `values` before `m`
5. If `t` is greater than `m`, your new search set is the half of `values` after `m`
6. If your search set is now empty, the `t` is not found
7. If your search set is not empty, return to step 2 with that new set

When you think you have it working, make sure to try out some tricky cases like these:

* Search for the value that is right on the dividing line of a set
* Search for a value that is not found
* Search for a value that is the only value in a set

Let's do some analysis of the algorithm. But, fair warning, this will be much tougher than the first algorithm.
Continue with the idea that comparing two numbers is the only instruction that is "expensive" in this algorithm.

1. How many comparisons would run in the best-case scenario for that algorithm?
2. How many comparisons would run in the worse-case scenario for that algorithm?
3. How many comparisons would run in an average case?
4. How would the worst-case scenario grow in proportion to the number of elements in the set?
