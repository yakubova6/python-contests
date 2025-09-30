data = input().split()

weight_in_kg = float(data[0])
height_in_m = float(data[1])

body_mass_index = weight_in_kg / (height_in_m ** 2)

print(body_mass_index)