import re


def main():
    with open("data.txt", "r") as f:
        data = f.read()

    result = 0
    pattern = re.compile(r'(Game\s*(\d*):)')
    for line in data.split("\n"):
        rgb = dict(red=12, green=13, blue=14)

        game = int(re.match(pattern, line).group(2))
        cubes = re.sub(pattern, '', line)

        flag = True
        for _set in cubes.split(";"):
            for color_set in _set.split(", "):
                count, color = color_set.split()
                if int(count) > rgb[color]:
                    flag = False

        if flag:
            result += game

    return result


print(main())
