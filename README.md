# Karatsuba

This is an implementation of Karatsubas method in python.
While quite a few other people have madeversions of this algorithm in various languages, including python, i was unable to find many people using base 2 instead of 10
( Possible in some of the implementations offered by some people ). On top of that, i was unable to find anyone who didn't use the **, // and % operators.


### Why does this matter ?

The cost of the algorithm has been calculated by assuming that only seven operations have a cost :

- The three multiplications
- The four additions

In those versions, assuming they followed what was done in this [exemple](https://github.com/stanislavkozlovski/Algorithms/blob/master/Coursera/algorithms_stanford/Karatsuba%20Multiplication/python/karatsuba.py)
( There might have been older versions than this one, but i used that one as an exemple and the goal is just to help understand what i mean ).

The cost is drastically changed to ( counting multiplications and powers together ) :

- Six additional multiplications to handle the powers of 10 
- Three divions
- Two modulo operations

### But those aren't included in the cost of the algorithm, despite it doing the same thing ?

Indeed, that is because it is assumed that these operations are 'free' : 
Imagine splitting 1833 into a * 10^n + b, you can nearly instantly  see the number as 18 * 10^2 + 33 as the number can be split into 1800 + 33 with ease.
The same principle applies to machines, except it is in base 2 instead of 10. To translate the action done above, bitwise operators can come in, which is exactly what my implementation uses.

Just to avoid some confusion when reading the code, i'll just add the 'translations' here :

a is equal to x // 2\**n, going back to base 10 it is simply a = x // 10\**n, not much of a change there.
Using 2 as a base though, allows us to translate the floored division by 2 by a bitshift to the right : x >> n

b is equal to x % 2\**n. Again, as we're always calculating the modulo of a power of 2 we can 'cheat' and use the bit operator '&' : b = x & (n - 1)
To explain why the -1 i would recommend searching about it as understanding it is quite important.
To obtain the result of 2**n we can also express it as a bitwise operator : 1 << n

c follows the same principle of a, and d follows the same as b.

For the final operation before the return, powers of 10 ( 2 here ) and a multiplication by 2 occurs, as they have already been covered by a or b, i won't elaborate ( The code also has a comment 'translating' them )


### To understand how the algorithm works

I recommend checking the wikipedia for that, or one of the many articles out there for it, but as a quick explanation :


We want to multiply x and y together

Both x and y can be expressed using the following 'template' : a * 10\**n + b
Multiplying x and y using this definition gives us : 
  (a * 10\**n + b)(c * 10\**n + d)
  
 Where c and d represent the unique integers for y.
 
 If we develop all of this, we get :
 
  ac * 10\**2n + (ad + bc) * 10\**n + bd
  
  So far, no magic.
  
  Now, let us see what we can do with, say, (a + b)(c + d) ( variants do exist using (a - b)(c - d) but they'll give negative numbers, which isn't good for signed numbers on which we do bit operations, although python handles that just fine).
  
  They give : ac + ad + bc + bd
  
  Now let's change (a+b)(c+d) to (a+b)(c+d) - ac - bd :
  
  It is now equal to ad + bc, except since we know a, b, c and d, we now just want to multiply ac and bd, which we already know, removing one multiplication.
  
  With that knowledge, we now have : 
  
  ac * 10\**2n + ((a + b)(c + d) - ac - bd) * 10**n + bd
  
