def main():
    with open("data.txt", "r") as f:
        data = f.read()

    result = 0
    for line in data.split():
        numbers = [c for c in line if c.isdigit()]
        result += int(numbers[0] + numbers[-1])
    return result


print(main())
