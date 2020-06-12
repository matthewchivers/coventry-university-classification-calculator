# Classification Calculator

## Coventry University

### Classifications

At the time of writing, there are three methods of classification:
1) The average mark of the 100 credits worth of modules with the highest mark at level 6 or above
2) The average mark of the 220 credits worth of modules with the highest mark at level 5 and above (to include a maximum of 120 credits at Level 5)
3) The average mark of the 300 credits worth of modules with the highest mark at levels 4 and above (to include a maximum of 120 credits at each of Levels 4 and 5)

This calculator assumes a three year degree. Roughly corresponding with:

* Year One = Level 4
* Year Two = Level 5
* Placement Year = Level 5
* Year Three = Level 6

## Instructions

Insert your grade information into the code directly. The program takes no input at runtime.

There is a section similar to:
``` python
if __name__ == "__main__":

    ##################################
    # INSERT GRADE INFORMATION BELOW #
    ################################## 
```
Grade information should go under this comment, as indicated using template variables.

Template is pre-populated for Computer Science Students Graduating in 2020 who took a placement year).

Once the grades (Modules) are populated, run the script! Something like:
``` bash
$ python calculator.py
```

The third classification algorithm can take a second or two to calculate, as the code employs backtracking to generate all possible permutations. No efficiency has been considered - just wanted to quickly create a tool for the job. Recommendations welcome.
