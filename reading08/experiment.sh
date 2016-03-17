ROLLS=1000
SIDES=6					
while getopts "r:s:h" option; do		
case $option in				
	r) ROLLS=$OPTARG ;;				
 	s) SIDES=$OPTARG ;;
 	h) echo "usage: $(basename $0) [ -r ROLLS -s SIDES]";
	   echo "    -r ROLLS        Number of rolls of die (default: 10)";
 	   echo "    -s SIDES        Number of sides on die (default: 6)"; exit 1 ;;
 	esac
done

(
j=0
while [ $j -lt $ROLLS ]; do
	(
	i=0
	while [ $i -lt $SIDES ]; do
		i=$((i+1))
		echo $i
	done
	) | shuf | head -n 1
	j=$((j+1))
done
) | awk '{count[$1]++}END{for(q in count) print q,"\t"count[q]}' | sort | > results.dat