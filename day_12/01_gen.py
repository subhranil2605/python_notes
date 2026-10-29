lines_read = 0


def cleaned_data(input_obj):
    global lines_read
    for line in input_obj:
        lines_read += 1
        yield line.strip()


def parse_line(clean_lines):
    for line in clean_lines:
        result = line.split(" ", 2)
        timestamp = result[0]
        level = result[1]
        message = result[2]
        record_data = {"timestamp": timestamp, "level": level, "message": message}
        yield record_data


def filter_error(records):
    for record in records:
        if record["level"] == "ERROR":
            yield record


def main():
    with open("data.log", "r") as f_object:
        result = filter_error(parse_line(cleaned_data(f_object)))
        print(next(result))
        print(next(result))


main()
print(lines_read)
