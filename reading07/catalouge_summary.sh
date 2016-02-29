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
        FS    = "\n\n"
        count = 0
    	}
    	{
    		print ARGC
    	}
'
