
COLOUR_CODES = {"black": "#000000", "blackcoffee": "#3b2f2f", "blackolive": "#3b3c36", "blackshadows": "#bfafb2",
                "blanchedalmond": "#ffebcd", "bronze": "#cd7f32", "blond": "#faf0be", "blue": "#0018a8",
                "bluebell": "#a2a2d0", "bluegreen": "#0d98ba"}


colour_name = input("Enter colour name: ")
while colour_name != "":
    print(f"The hexadecimal code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter colour name: ")



