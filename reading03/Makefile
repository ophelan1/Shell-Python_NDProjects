all: hello-debug hello-dynamic hello-profile hello-static

hello-debug: hello.c
	gcc -g hello.c -o hello-debug

hello-dynamic: hello.c
	gcc hello.c -o hello-dynamic

hello-profile:
	gcc -pg hello.c -o hello-profile

hello-static:
	gcc -static hello.c -o hello-static

clean: 
	rm -rf hello-*
