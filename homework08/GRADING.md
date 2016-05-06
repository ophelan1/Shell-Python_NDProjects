Homework 08 - Grading
=====================

**Score**: 12.75 / 15

Deductions
----------

-0.25	One test in timeout test failed
-2	Four tests in rorschach test failed


Comments
--------

 timeout.py -h does not contain usage
/afs/nd.edu/user9/cmaheu/unix/grading/assignments/homework08/cmaheu/testto.sh: line 27: 30346 Terminated              ./timeout.py -t 1 sleep $i
/afs/nd.edu/user9/cmaheu/unix/grading/assignments/homework08/cmaheu/testto.sh: line 27: 30349 Terminated              ./timeout.py -t 1 sleep $i
/afs/nd.edu/user9/cmaheu/unix/grading/assignments/homework08/cmaheu/testto.sh: line 27: 30351 Terminated              ./timeout.py -t 1 sleep $i
/afs/nd.edu/user9/cmaheu/unix/grading/assignments/homework08/cmaheu/testto.sh: line 27: 30353 Terminated              ./timeout.py -t 1 sleep $i
timeout.py tests 1 failures

 Traceback (most recent call last):
  File "./rorschach.py", line 112, in <module>
    itDirs()
  File "./rorschach.py", line 62, in itDirs
    itFiles(path)
  File "./rorschach.py", line 57, in itFiles
    itRules(address)
  File "./rorschach.py", line 38, in itRules
    Action = shlex.split(dictItem['action'].format(path = filename, name = os.path.basename(filename)))
TypeError: string indices must be integers, not str
testr.sh: line 55: kill: (30372) - No such process
rorschach.py tests 4 failures


