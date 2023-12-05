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

    maps_reversed = list(maps.items())[::-1]

    def get_seed_from_location(i):
        for _, values in maps_reversed:
            for dest, src, rnge in values:
                if dest <= i < dest + rnge:
                    i = src + (i - dest)
                    break
        return i

    for i in range(100_000_000_000):
        seed = get_seed_from_location(i)
        for seed_range in range(0, len(seeds), 2):
            _seeds = seeds[seed_range:seed_range + 2]
            if _seeds[0] <= seed < sum(_seeds):
                return i, seed



print(main())
