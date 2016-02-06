CC=             gcc
CFLAGS=         # TODO
LD=             gcc
LDFLAGS= -c
AR=             ar
ARFLAGS=        # TODO
TARGETS=        libgcd.a libgcd.so gcd-static

all: gcd-dynamic gcd-static

gcd-dynamic: main.c libgcd.so
        gcc -o gcd-dynamic -L. main.c -lgcd

gcd-static: libgcd.a main.c
        gcc -static -o gcd-static -L. main.c -lgcd

libgcd.a: gcd.o
        ar -rcs libgcd.a  gcd.o

libgcd.so: gcd.c
        gcc -fPIC -c -o libgcd.o $^
        gcc -shared -o libgcd.so libgcd.o

%.o: %.c
        gcc -c -o $@ $^


clean:
      	rm -f $(TARGETS) *.o
