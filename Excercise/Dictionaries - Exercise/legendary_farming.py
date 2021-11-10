items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
not_obtained = True

while not_obtained:
    data = input().split()

    for index in range(0, len(data), 2):
        quantity = int(data[index])
        material = data[int(index) + 1].lower()

        if material in key_materials:
            key_materials[material] += quantity

            if key_materials[material] >= 250 and not_obtained:
                key_materials[material] -= 250
                print(f"{items[material]} obtained!")
                not_obtained = False
                break

        elif material not in junk_materials:
            junk_materials[material] = quantity

        else:
            junk_materials[material] += quantity

sorted_key_materials = (sorted(key_materials.items(), key=lambda data: (-data[1], data[0])))
sorted_junk_materials = (sorted(junk_materials.items()))

for material, quantity in sorted_key_materials:
    print(f"{material}: {quantity}")

for material, quantity in sorted_junk_materials:
    print(f"{material}: {quantity}")