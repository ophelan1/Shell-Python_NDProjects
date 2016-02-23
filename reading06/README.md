Reading 06
==========
1. tr '[:lower:]' '[:upper:]'
2. grep root:/bin/ | awk '/bin/{print $NF}'
3. sed 's/monkey/gorillaz/g'
4. sed 's/\/bin\/[bash|tcsh/csh].*$/\/usr\/bin\/python/g'
5. sed -e 's/^[ \t]*//'
6. grep "4[0-9]\{2,\}:[0-9]\{2,\}7"
7. tail -f log_name.log
8. grep -F -f file1.txt file2.txt

