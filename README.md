# Classification Calculator

## Coventry University

### Pre-amble
This calculator has not been officially verified as accurate against Coventry University's internal systems. However, it does follow the algorithms correctly (to the best of our knowledge). 

The calculator did make correct calculations for the cohort graduating in Summer 2020 (for those students kind enough to test it, anyway).

### Classifications

At the time of writing, there are three methods of classification:
1) The average mark of the 100 credits worth of modules with the highest mark at level 6 or above
2) The average mark of the 220 credits worth of modules with the highest mark at level 5 and above (to include a maximum of 120 credits at Level 5)
3) The average mark of the 300 credits worth of modules with the highest mark at levels 4 and above (to include a maximum of 120 credits at each of Levels 4 and 5)

This calculator currently assumes a classic three year degree plus industrial placement. Roughly corresponding with:

* Year One = Level 4
* Year Two = Level 5
* Industrial Placement Year = Level 5
* Year Three = Level 6

## Instructions

> #### Note
> The input functionality ideally needs changing to be more robust. Either to take (CLI) input at runtime or else from a (CSV/JSON) file. Hard-coding inputs should be avoided, but this was hashed together alongside final-year deadlines and revision.

#### Insert grade information into the code directly:

There is a code-block similar to:
``` python
if __name__ == "__main__":

    ##################################
    # INSERT GRADE INFORMATION BELOW #
    ################################## 
```

The modules displayed under this comment block should be fairly self-explanatory. Use them as a template for your own grades/modules.

> The current information is pre-populated for Computer Science Students Graduating in 2020, including a placement year.

Once the grades (modules) are populated, run the script! Something like:
``` bash
$ python calculator.py
```
The output will inform you of the classification you should be awarded, and lists the calculations from all algorithms for information purposes.

The calculations employ backtracking to gain all grade/module permutations. For this reason, the third classification algorithm can take a considerable amount of time to calculate (though it has never taken longer than a few seconds in my own tests).
