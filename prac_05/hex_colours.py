colour_to_hex = {"DarkSlateGray": "#2f4f4f", "DarkViolet": "#9400d3", "CornflowerBlue": "#6495ed",
                 "BlueViolet": "#8a2be2", "AliceBlue": "#f0f8ff", "BlanchedAlmond": "#ffebcd",
                 "CadetBlue": "#5f9ea0", "DarkGreen": "#006400", "DarkOrange": "#ff8c00",
                 "DarkOrchid": "#9932cc"}


colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in colour_to_hex:
        print("{} is {}".format(colour_name, colour_to_hex[colour_name]))
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")