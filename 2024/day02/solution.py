#!/usr/bin/python3

def parse_input(path:str) -> list[tuple[int]]:
    with open(path) as file:
        data = file.read().splitlines()

    reports = [tuple(int(i) for i in line.split()) for line in data]

    return reports

positive = lambda n: True if n > 0 else False

def count_safe(reports: list[tuple[int]]) -> int:
    safe = 0

    for report in reports:
        prev = report[0]
        sign = None

        for pos in report[1:]:
            dif = pos-prev

            if abs(dif) > 3:
                break
            elif dif == 0:
                break
            elif positive(dif) != sign and sign is not None:
                break

            prev = pos
            sign = positive(dif)
        else:
            safe += 1

    return safe

def count_safe_tolerate(reports: list[tuple[int]]) -> int:
    safe = 0

    for report in reports:
        prev = report[0]
        sign = None
        levels = 0

        for pos in report[1:]:
            dif = pos-prev

            if abs(dif) > 3:
                levels += 1
            elif dif == 0:
                levels += 1
            elif positive(dif) != sign and sign is not None:
                levels += 1
            else:
                prev = pos
                sign = positive(dif)

            if levels > 1:
                break
        else:
            safe += 1

    return safe

if __name__ == '__main__':
    # reports = parse_input('test-input')
    reports = parse_input('input')

    # Part 1
    safe = count_safe(reports)
    print(f"{safe} reports are safe")

    # Part 2
    safe = count_safe_tolerate(reports)
    print(f"{safe} reports are actually safe")
