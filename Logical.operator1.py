#logical operators = evalue multiple conditions (or, and, not)
#                    or = at least one condition must be True


temp = 31
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")