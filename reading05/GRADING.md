Reading 05 - Grading
====================

**Score**: 4 / 4

Deductions
----------

Comments
--------

2. hello.sh
You could also do:

for argument in $@; do
    echo Hello, $argument!
done

3. mascot.sh
You can also use a case statement like this:
#!/bin/sh

case $(uname) in 
    Linux)
    echo Tux
    ;;
    Darwin)
    echo Hexley
    ;;
    *BSD)
    echo Beastie
    ;;
    *)
    echo Uh... yeah...
    ;;
esac

4. resolve_links.sh
Get all arguments with:
for path in $@; do
   for file_path in $path/*; do
...
   done
done
