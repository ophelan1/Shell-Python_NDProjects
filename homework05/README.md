Homework 05
===========

caesar.sh
---------
1. The source set [SET1] would be all upper and lower case letters. That is, it will be all the letters from A-Z and from a-z. So, SET1=[A-Za-z]. 
2. [SET2] shifts those letters according to the shift letter (or amount). So, instead of being a pattern of letters rannging from A-Z, we have a range of letters from ("shift letter")-("letter before the shift letter"). But bourne cannot handle this implicitly, so we have to specific [shiftletter-ZA-(shiftletter-1)] So, if SET1=[A-Z], and the shift letter is the letter "L", SET2=[L-ZA-K]. Set 2 was constucted using printf and octal substitution to convert the integer values to characters. (i.e. 1 = A, shiftLetter="The Letter 'N' after A"). Once we have the set for [A-Z] to [L-ZA-K], it is easy to also include lower case letters, (i.e. [A-Za-z]=[L-ZA-Kl-za-k] )
3. Once the two sets are set up, encryption is easy. We simply take [input % 26] so that any shift request greater than from A-Z is reduced to a form that makes sense. We then convert that integer to the ASCII values that correspond to the UpperShiftChar and LowerShiftChar. Once we have these ascii values, we need the script to understand them as char, so we can substitute them into our sets. This is done using printf and %03o. The shell interprets this octal as a character. This means that we can now substitue into our 'tr' equation, and the shell will be able to understand it.

reddit.sh
---------
1. The command ( grep -F '"url":') grabs all the lines with the string ("url":) in them. The -F flag forces grep to grab entire lines. Once the lines which contain the sought after string around found, the ouput is piped to sed. Sed replaces input patterns with output patterns. In theory, my sed works like this:
	1. sed 's/			#REPLACE THE PATTERN BELOW
	2. [The Leading Blanks] & [String ( "url": )] & [The Actual URL] & [String ( ", )]
	3. /				#REPLACE ABOVE PATTERN WITH
	4. [The Actual URL from #2] 
	5. /g'				#DO THIS FOR ALL INCOMING DATA, NOT JUST ONCE 
2. I managed ordering using a pipeline. The input is grabbed by grep, maniuplated by sed, and then piped through $SORT and $SHUFFLE. Finally, it is piped into head and displayed. If a shuffled output is requested, $SORT="cat" && $SHUFFLE="shuf". Thus, it will be piped into $SORT, which will call cat (do nothing) and pipe the same input into $SHUFFLE. $SHUFFLE causes the input to be piped into the 'shuf' command, shuffling it, and then pipes the output to head. If a sorted output is requested, the same technique is used but this time $SORT="sort" && $SHUFFLE="cat".
3. I'm sure this is not the OFFICAL way to do this, but it was the most convenient and got the job done. I simply created variable strings which corresponded to whether or not a flag has been called. If the flag arguments signal that the output should be piped through a command (i.e. "-s" means output should be sorted) then these variable string are set equal to the requested commands (i.e., sortString="sort"). If the commands in question should NOT be called, then the string values are set to "cat". THIS WAY, if I want to pipe input to output through several commands, there does not need to be any "if then" statements present in the pipeline. If a command is supposed to be run, input is piped into its value (aka input is piped into the commands that it's string value represents), manipulated, then piped out. If a command is not supposed to run, it's string value will be "cat", so it will simply pass the input to the next section of the pipe. It is easy to see how each specific flag affects the string values by looking at the case statement. 

broify.sh
---------
1. My piping method was the same as with reddit.sh. To remove comments, I simply set a variable equal to the DELIM as specified by the flag (set to '#' if no flag given). I then set a string variable equal to the commands necesary to remove these comments (a sed command used with a regex). When the input is sent through the pipe, it is piped through the string value of this variable, and so is piped through the correct comment deletion commands. It took me a while to deal with doing this to special characters such as '//' fron the example
2. This was tricky because "grep" and "cat" pass their input one line at a time. If I were to use "sed REPLACE" I would need to find the pattern "\n\n" in the text (New line at the end of a string followed by another new line indicates a blank line of text). The means that I would need to consider multiple lines at once. It is much easier to use "sed DELETE". That way I can delete any line of text which is blank, and remove it from the stream entirely, instead of finding "\n\n" and replacing it with "\n".
3. Much like reddit.sh, the command line arguments simply change the values of the stringVariable commands. 
