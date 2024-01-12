
class Band:

    def __init__(self, name=""):
        """Initialize the band"""
        self.name = name
        self.members = []

    def __str__(self):
        """Return a string representation of a band."""
        bands_str = []
        for member in self.members:
            bands_str.append((str(member)))
        return f"{self.name} ({', '.join(bands_str)})"

    def add(self, member):
        """Add a member to the band."""
        self.members.append(member)

    def play(self):
        """Play bands."""
        output = ""
        for musician in self.members:
            if musician.instruments:
                output = output + musician.play() + "\n"
            else:
                output = output + musician.name + " needs an instrument!\n"
        return output



