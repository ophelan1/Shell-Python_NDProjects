TLDR - grep
==========

Overview
--------

Grep  searches the named input FILEs (or standard input if no files are
       named, or the file name - is given) for lines containing a match to the
       given PATTERN.  By default, grep prints the matching lines.

Examples
--------

-Search For A Given String In A File-
	grep "literal_string" filename

-Case Insensative Search-
	grep -i "literal_string" filename

-Match Regular Expressions-
	grep "REGEX" filename

-Seach for a given WORD, not just string fragment-
	grep -iw "literal_string" filename
