Homework 03 - Grading
=====================

**Score**: 1.5 / 15

Deductions
----------
Activity 1 Task 1
-0.5	Doesn’t use variables in rules
-0.75 	Don't have the right dependencies for some rules
Rules should look like this:
libgcd.a:       gcd.o
        $(AR) $(ARFLAGS) $@ $<

libgcd.so:      gcd.o
        $(LD) $(CFLAGS) -shared -o $@ $<

gcd-dynamic:    main.o libgcd.so
        $(LD) $(LDFLAGS) -o $@ -L. $< -lgcd

gcd-static:     main.o libgcd.a
        $(LD) $(LDFLAGS) -static -o $@ -L. $< -lgcd
-2 pt for missing all parts for Activity 1 except makefile

-10 pt missing all parts for Activities 2 and 3


Comments
--------
Please see the TA's or Prof. Bui if the grading is a mistake and you forgot to push. Seems like alot is missing



