#usr/bin/sh 

####### Main Script #######
if [ $# = 1 ]; then
	urlSTR=${1}
else
	urlStr="http://catalog.cse.nd.edu:9097/query.text"
fi
# A better reddit.sh
curl -s $urlStr | \
awk 'BEGIN {
		printf "# Begin Section:\n"
		counter=0
		totalMachines=0
 	}
 	/type/ {
		types[$2]++
   	}
   	/name/ {
   		if ( $2 in names ){
   			names[$2]=1
   		}
   		else {
   			totalMachines++
   		}
   		counter++
   	}
   	{
   		counter++
   	}
	END {
		printf "# End Section:\n"
		i=0
		max=0
    	for (i in types) {
    		if ( types[i] > max ){
    			max=i
    		}
        }
        printf "Total Numer of Machines:    %d\n", totalMachines
        printf "Most Prolific Type:   		%s\n", max
        printf "Total Number of CPUs :		%d \n ", counter

    }'
