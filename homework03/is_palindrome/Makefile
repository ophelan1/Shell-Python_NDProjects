CC=             gcc
CCFLAGS=        -g -O0
TARGETS=        is_palindrome

all: $(TARGETS)

is_palindrome: is_palindrome.c
		$(CC) $(CCFLAGS) -o $@ $<

test: is_palindrome is_palindrome.input is_palindrome.output
		cat is_palindrome.input | ./is_palindrome > is_palindrome.test
		diff is_palindrome.test is_palindrome.output
		rm is_palindrome.test

clean:
		rm -fR ./is_palindrome ./is_palindrome.dSYM ./is_palindrome.test *.o