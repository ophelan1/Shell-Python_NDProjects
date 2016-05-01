CC=             gcc
CFLAGS=         
LD=             gcc
LDFLAGS= 		 
AR=             ar
ARFLAGS=        -rc
TARGETS=        libgcd.a libgcd.so gcd-static gcd-dynamic

all: $(TARGETS)

libgcd.a: gcd.o
		$(AR) $(ARFLAGS) $@ $<

libgcd.so: gcd.o
		$(LD) $(CFLAGS) -shared -o $@ $<

gcd-dynamic: main.o libgcd.so
		$(LD) $(LDFLAGS) -o $@ -L. $< -lgcd

gcd-static: main.o libgcd.a
		$(LD) $(LDFLAGS) -static -o $@ -L. $< -lgcd

%.o: %.c
		$(CC) -c -o $@ $^

clean:
		rm -f $(TARGETS) *.o




