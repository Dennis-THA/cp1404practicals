
CURRENT_YEAR = 2023
VINTAGE_YEAR = 50


class Guitar:
    """Class for storing data and determining old guitar or not"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a guitar"""
        return f"{self.name} ({self.year} : ${self.cost:,.2f} )"

    def get_age(self):
        """Get the age pf the guitar based on the current year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine whether the guitar is vintage or not """
        return self.get_age() >= VINTAGE_YEAR
