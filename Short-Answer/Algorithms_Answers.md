#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Answer: O(n^3)

b)
Answer : O(n^2)

c)
Answer: O(n)


## Exercise II

English:
Drop the egg from each story starting with the first story
if the egg does not break, continue up to the next story,
if the egg breaks, stop
f is the story below the story where the egg broke

pseudo code-ish:
for story in building:
    if egg breaks:
        stop
        f = story - 1
    elif egg doesn't break
        continue through loop

Runtime:
O(n^3)