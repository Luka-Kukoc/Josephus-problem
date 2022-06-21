# Josephus-problem

Josephus problem explanation:

https://en.wikipedia.org/wiki/Josephus_problem

https://www.youtube.com/watch?v=uCsD3ZGzMgE&ab_channel=Numberphile

I watched a video about the Josephus problem and decided to try to solve it.

When I managed to figure out the solution, I wanted to try it out in python using this formula (the step, in this case, is 2, so every second person gets killed):

w = 1 + 2(n-i)

n - number of people

i - the greatest number that is to the power of 2 and is lesser than n (if n is 17 then b is 16, or if n is 77 then b is 64)

w - the place where Josephus should be.

I figured, when n (the number of people) is a number with a base of 2, the answer (solution) is 1, hence the first if statement.
The rest calculates the place where Josephus should be using the formula that I came up with.

 
