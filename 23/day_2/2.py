import re


def main():
    with open("data.txt", "r") as f:
        data = f.read()

    result = 0
    pattern = re.compile(r'(Game\s*(\d*):)')
    for line in data.split("\n"):
        rgb = dict(red=0, green=0, blue=0)

        cubes = re.sub(pattern, '', line)

        for _set in cubes.split(";"):
            for color_set in _set.split(", "):
                count, color = color_set.split()
                rgb[color] = max(rgb[color], int(count))

        result += rgb.get("red", 1) * rgb.get("green", 1) * rgb.get("blue", 1)

    return result


print(main())
