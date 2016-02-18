#!/bin/sh
#Shell Script "bake.sh"
set -e

pngs=`find . -iname "*$SUFFIXES"`

if [ "$VERBOSE" == "1" ]; then
	set -v
fi

for file in $pngs; do
        $CC $CFLAGS $file -o ${file%.*} || echo "ERROR: Compilation Failed for ${file}" && exit
done
