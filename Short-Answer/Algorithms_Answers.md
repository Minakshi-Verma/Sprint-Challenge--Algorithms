#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
I think, the overall runtime complexity for the 1st problem is O(n). There is only one loop involved in this snippet and the runtime will change linearly with n.

b)
My guess is, the runtime complexity would be O(n^n) for the problem-2 since this snippet has nested loops('while' and 'for' loop).


c)
In the third problem, L25-L27 are O(1) but L29 is O(n) since it a function call. So the runtime complexity for this code block would be O(n).

## Exercise II
Building can be considered as a sorted array as the 2nd floor would be on the top of first, third floor would be on the top of 2nd and so on. So I would use sorting as we do in binary search tree.

# go to mid floor of the building(n/2) and drop the egg
-if egg is broken, we are at floor f or higher.means we need to move to lower floor to find the right floor. Consider this midfloor as a "temp top floor" for now.
# move 1 floor down, and go to mid floor again(consider (temp top floor-1) as a top floor for this search) 
-if egg is broken again, we will will go 1 floor down the mtemp mid floor and continue to search for right floor.Repeat the process.
- if egg is not broken, we will consider this floor as  "temp bottom floor" for our next search. now we will go half way up to check if egg gets broken from that floor. We will reapeat till we find the right floor.






