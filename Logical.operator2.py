#logical operators = evalue multiple conditions (or, and, not)
#              and = both conditions must be True


temp = -24
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")