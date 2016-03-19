awk -F "," '{print $1,$2}' demographics.csv | awk '{count[$1]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $1,$2}' demographics.csv | awk '{count[$2]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $3,$4}' demographics.csv | awk '{count[$1]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $3,$4}' demographics.csv | awk '{count[$2]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $5,$6}' demographics.csv | awk '{count[$1]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $5,$6}' demographics.csv | awk '{count[$2]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $7,$8}' demographics.csv | awk '{count[$1]++}END{for(q in count) print q, "\t"count[q]}' | sort
awk -F "," '{print $7,$8}' demographics.csv | awk '{count[$2]++}END{for(q in count) print q, "\t"count[q]}' | sort