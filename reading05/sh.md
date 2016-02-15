TLDR - sh
==========

Overview
--------

.sh files contain Shell Scripts, which are a list of commands that would otherwise 
have to be entered individually onto the command line.

Examples
--------

-Variables in Shell scripting-
	
	variable=value
	variable=$EnviornmentalVariable

-IF Statements-
	
	if [ STATEMENT ];then
   		//Command
	elif [ STATEMENT ];then
   		//Command
	elif [ STATEMENT ] || [ STATEMENT ] || [ STATEMENT ];then
		//Command
	fi

-CASE Statements-

	case word in
  		pattern1)
     		Statement(s) to be executed if pattern1 matches
     	;;
  		pattern2)
    		Statement(s) to be executed if pattern2 matches
     	;;
  		pattern3)
     		Statement(s) to be executed if pattern3 matches
     	;;
	esac

-FOR loop-
	
	for VARIABLE in N;do
		//Command
		//Command
	done

-WHILE loop-

	while COMMAND; do
		//Statements
	done

-FUNCTIONS-

	Hello () {
		echo "Hello World"
	}

-TRAP-

	kill -2 FILENAME

