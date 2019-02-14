from timeit import default_timer
from math   import gcd

# ===========================================================
# PROBLEM 5 -- Smallest multiple
# ===========================================================
#
# 2520 is the smallest number that can be divided by each of
# the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible
# by all the numbers from 1 to 20
#
# ===========================================================
# lcm(a,b) = a*b/gcd(a,b)
# can start from given lcm of 1-10
def problem_5( ):
    # Print the Problem Context
    print( "Project Euler Problem 5 -- Smallest Multiple" )

    # Set Up Variables
    start_time  =  default_timer( )
    lcm         =  2520

    # Primary Loop, compute the LCM of the current and the next integer in the range
    for n in range( 11 , 21 ):
        lcm  *=  n // gcd( lcm , n )

    # Compute Execution Time
    end_time        =  default_timer( )
    execution_time  =  ( end_time - start_time ) * 1000

    # Display Results
    print( "   Smallest Positive numbers evenly divisible by all numbers from 1 to 20:   %d"      % lcm )
    print( "   Computation Time:                                                         %.3fms"  % execution_time )
    return

if __name__ == '__main__':
    problem_5( )
