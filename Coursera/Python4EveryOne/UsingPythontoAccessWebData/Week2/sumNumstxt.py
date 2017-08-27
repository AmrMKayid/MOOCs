import re

file = open("regex_sum_23971.txt", "r")
print(sum([int(i) for i in re.findall('[0-9]+', file.read())]))