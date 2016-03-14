Homework04 - Grading
====================

**Score**: 10.25 / 15

Deductions
----------

-1.0 #1 Fails test
-0.5 #1 Need to use parameter expansion to define variables

-1.0  #2 Fails test
-0.25 #2 Does not print usage if no arguments given
-0.25 #2 Does not use -h flag for du and sort
-0.25 #2 Didn't redirect stderr to /dev/null
-0.25 #2 -a flag not handled correctly

-0.25 #3 Uses one long sleep instead of a series of smaller sleeps

Comments
--------

- #2 No need to store output in temp file and cat it, just let output go to
  stdout

- #2 There is no need to create a temp directory

- #3 the `function` prefix is a BASHism

- #3 There is no need to create a temp directory

- #3 Using labels such as INT for the signals is better than numbers

- While using Google is great, if you get stuck you could ask questions or seek
  guidance from a TA or the instructor.

  Most shell scripts are actually written in Bourne shell since that is the
  most portable language across all Unix systems.
