

COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

filename = "wimbledon.csv"


def main():
    """Extract data from a file and print results about champions and countries that won Wimbledon """
    records = get_record()
    champions_to_count, countries = process_data(records)
    display_result(champions_to_count, countries)


def display_result(champions_to_count, countries):
    """Display the result of champions and countries """
    print("Wimbledon Champions: ")
    for name, frequency in champions_to_count.items():
        print(name, frequency)
    print(f"\nThese {len(countries)} have won Wimbledon: ")
    print(','.join(country for country in sorted(countries)))


def process_data(records):
    """Process the data of champions and countries """
    champions_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champions_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champions_to_count[record[CHAMPION_INDEX]] = 1
    return champions_to_count, countries


def get_record():
    """Get the record from a file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


main()
