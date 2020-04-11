""" Taxi """
import re


def calculate(distance, minutes=0):
    """calculate fee with distance and waiting minutes"""
    fee = 6
    if distance > 2:
        if distance <= 8:
            fee = fee + (distance - 2) * 0.8
        else:
            fee = fee + 6 * 0.8 + (distance - 8) * 1.2
    if minutes > 0:
        fee = fee + minutes * 0.25
    return round(fee)


def format_output(fee):
    return "收费%s元" % fee


def parse_line(line):
    m = re.match(r"(?P<distance>\d+)公里,等待(?P<minutes>\d+)", line)
    return int(m.group("distance")), int(m.group("minutes"))


def process_line(line):
    distance, minutes = parse_line(line)
    fee = calculate(distance, minutes)
    return format_output(fee)


def process_file(path):
    result = []
    with open(path, "r") as file:
        line = file.readline()
        while line:
            result.append(process_line(line))
            line = file.readline()
    return "\n".join(result)
