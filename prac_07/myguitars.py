from prac_07.guitar import Guitar
in_file = "guitars.csv"


def main():
    guitars = []
    with open(in_file, 'r') as infile:
        for line in infile:
            name, year, cost = line.strip().split(',')
            year = int(year)
            cost = float(cost)
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    sorted_guitars = sorted(guitars)
    for guitar in sorted_guitars:
        print(guitar)


main()
