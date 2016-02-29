#usr/bin/sh 

####### Main Script #######
if [ $# = 1 ]; then
	urlSTR=${1}
else
	urlStr="http://catalog.cse.nd.edu:9097/query.text"
fi
# A better reddit.sh
curl -s $urlStr | \
awk 'BEGIN     {
        FS= "\n\n"
        count = 0
 	}
 	{
 	   	/type/ {
   			types[$2]++
   			count++
   		}
	}
	END {
       for (i = 0; i < count; i++) {
            if (i in Titles) {
                printf "%2d. %s\n", c, Titles[i]
                printf "    %s\n\n", URLs[i]
                c++                                                                                                    
            }
        }
    }	
}
'
