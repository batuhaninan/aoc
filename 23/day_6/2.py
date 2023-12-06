def main():
    with open("data.txt", "r") as f:
        lines = f.read().split("\n")

    result = 1

    time = int("".join([time for time in lines[0].split("Time: ")[-1].split(" ") if time]))
    distance = int("".join([distance for distance in lines[1].split("Distance: ")[-1].split(" ") if distance]))

    time_to_hold = set()

    for i in range(1, time+1):
        ms = ((time - i) * i)
        if ms > distance:
            time_to_hold.add(i)

    result *= len(time_to_hold)

    return result


print(main())
