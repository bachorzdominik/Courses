# https://hyperskill.org/learn/step/6347
import math

r = math.radians(int(input()))
cos = math.cos(r)
sin = math.sin(r)

print(round((cos / sin), 10))
