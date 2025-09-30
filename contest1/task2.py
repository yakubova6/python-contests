from math import ceil

human_oxygen_per_day = 0.5

oak_oxygen_per_year = 20
poplar_oxygen_per_year = 32

days_in_year = 365

human_oxygen_per_year = human_oxygen_per_day * days_in_year
poplars_needed = ceil(human_oxygen_per_year / poplar_oxygen_per_year)
oaks_needed = ceil(human_oxygen_per_year / oak_oxygen_per_year)

print(f"{human_oxygen_per_year} {poplars_needed} {oaks_needed}")