summary.

1. simpy is module that help users to make simulate random situation.
2. It is specialized to deal with non synchronous situations like real world that car parking to empty space or employee checking.
3. In this simulation, time scale is env.now, if want to set maximum time, it can be done with env.run(until=150)
4. In simpy environment, only 1 process can be executed at 1 time.
   if one process is ended and want to execute other process
   1. set process using env.process
   2. and end process using yield env.timeout( time )
                       or   yield


Code other data in example code.

1. set numbers in each checkers
2. record which checkers deal with how many shoppers in global variable
3. print out end of the code.


