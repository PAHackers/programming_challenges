# Challenge

Improve the performance of your code from [challenge #1](../challenge_1/README.md)

If you have not participated in round 1, you can earn 5 points for any
submission that posts better times than the last place submission from round 1.
You can earn an additional 5 points if you include a time complexity analysis
of your algorithm using Big-O notation.

## Scoring Points


### Performance Improvements
10 points for cutting your worst run time in half

15 points for improving your worst run time by 1 order of magnitude

5 points for every additional order of magnitude

10 bonus points for getting within 5% of thunderhorse's round 1 times

~~15 bonus points for getting within 5% of thunderhorse's round 2 times (that's
right, I improved my times, too!)~~ Unfortunately, I found some serious issues
with my round 2 solution and won't have time to resolve them, so I'm withdrawing
this bonus.

### Analysis
If you have not submited a time complexity analysis as part of round 1, you
can earn 5 points by submitting it during round 2.

Additional 5 points for a time complexity analysis of your round 2 code.
Include an explaination of how you were able to optimize the performance.

## Submission and Due Date
PM your code to @ThunderHorse on the PA Hackers by 11:59PM on Sunday, ~~October 11, 2020~~ January 3, 2021.

## Tips

1. Python is an interpreted language. You can usually assume that interpreted == slow.
   Built-in functions will tend to be faster than whatever you write. This is
   because the built-in functions are implemented in C and optimized for
   performance. For example, using index() to find the index of an element in
   a list will likely be faster than using a loop that iterates over every
   value of the list.

2. Relying on built-in functions can make the things you do faster. The only thing
   better than improving the speed of what you're doing is finding a way not to
   do it at all, or at least do less of it. Look for ways to do less work.

3. Look for ways to short-circuit your algorithm. Quitting early is a great way
   to reduce the total amount of work the computer has to do.

4. Break your algorithm up into chunks with different purposes (e.g. read data
   from file, search for number, etc.) Figure out which thing takes the longest
   and find a way to do it faster and/or do less of it.

5. Generate a larger data set to see how your algorithm scales. 1000 lines isn't
   big enough to get a sense for whether or not the changes you're making are
   actually improvements. Form a hypothesis about what would make your algorithm
   faster. If it doesn't behave how you would expect, investigate why. I'm happy
   to answer questions :)

6. Get an understanding of how each operation on your data structures scales.
   This page can be very helpful: https://wiki.python.org/moin/TimeComplexity
   It may give you wholly new ideas about how you might approach solving this.

