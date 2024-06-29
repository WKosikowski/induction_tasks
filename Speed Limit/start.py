#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from RoadSection import *


date1 = datetime.datetime(2024, 7, 23, 3, 20, 0)
date2 = datetime.datetime(2024, 7, 23, 3, 22, 0)
date3 = datetime.datetime(2024, 7, 23, 3, 25, 0)
date4 = datetime.datetime(2024, 7, 23, 3, 28, 0)


road = RoadSection(50, 2)
print(road.isOverLimit(date1, date2))
print(road.isOverLimit(date3, date4))