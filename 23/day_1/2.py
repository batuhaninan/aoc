def main():
    with open("data.txt", "r") as f:
        data = f.read()

    numbers_spelled = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
   }

    result = 0
    for line in data.split():
        _line = line
        for number in numbers_spelled.keys():
            if numbers_spelled[number] in _line:
                _line = _line.replace(number, number[0] + numbers_spelled[number] + number[-1])
        numbers = [c for c in _line if c.isdigit()]
        result += int(numbers[0] + numbers[-1])
    return result


print(main())
