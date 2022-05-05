# CS 412 Algorithms & Analysis

You are given n eggs and a building with k floors. Dropping an egg from a floor higher than the threshold floor will break the egg. A drop from a floor equal to or lower than the threshold floor conserves the egg. Given that an unbroken egg can be dropped from any floor, what is the minimum number of egg drops D needed in order to find the threshold floor in the worst case? 

## Constraints:
An egg that survives a fall can be used again <br>
A broken egg must be discarded <br>
The effect of a fall is the same for all eggs
If an egg breaks when dropped, then it would break if dropped from a higher floor. <br>
If an egg survives a fall then it would survive a shorter fall <br>

### Three approaches to solve this problem:
Recursive<br>
Dynamic Programming<br>
Binomial Coefficients With Binary Search<br>

## Applications
Minimizing cache misses when retrieving data from the cache<br>
Performing a large number of queries on a database<br>
Avoiding a call to the HDD which is slower<br>
