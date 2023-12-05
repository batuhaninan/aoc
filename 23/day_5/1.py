def main():
    with open("data.txt", "r") as f:
        lines = f.read().split("\n")

    maps = dict(
        seed_to_soil=list(),
        soil_to_fertilizer=list(),
        fertilizer_to_water=list(),
        water_to_light=list(),
        light_to_temperature=list(),
        temperature_to_humidity=list(),
        humidity_to_location=list()
    )

    seeds = [int(number) for number in lines[0].split("seeds: ")[1:][0].split(" ")]

    last_map = ""

    for line in lines[2:]:
        if " map:" in line:
            last_map = line.split(" map:")[0]
            continue

        if not line:
            last_map = ""
            continue

        dest, src, rnge = [int(number) for number in line.split(" ") if line]
        map_name = last_map.replace("-", "_")
        maps[map_name].append((dest, src, rnge))

    min_score = 99999999
    print(maps)
    for seed in seeds:
        last_value = seed

        for _, values in maps.items():
            for dest, src, rnge in values:
                if src <= last_value <= src + rnge:
                    last_value = dest + (last_value - src)
                    break

        min_score = min(min_score, last_value)

    return min_score


print(main())
