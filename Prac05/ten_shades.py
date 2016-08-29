COLOUR_HEXES = {"grey1": "#030303", "grey5": "#0d0d0d", "grey10": "#1a1a1a", "grey15": "#262626", "grey20": "#333333",
                "grey25": "#404040", "grey30": "4d4d4d", "grey35": "#595959", "grey40": "#666666", "grey45": "#737373",
                "grey50": "#7f7f7f"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_HEXES:
        print(colour, "is", COLOUR_HEXES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")
