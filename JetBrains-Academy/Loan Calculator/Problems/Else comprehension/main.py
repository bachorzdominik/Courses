# https://hyperskill.org/learn/daily/9887
# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]
print([1 if num > 0 else 0 for num in old_list])
