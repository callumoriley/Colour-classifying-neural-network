import random

# created by ChatGPT
def identify_color(rgb):
    red, green, blue = rgb

    red *= 256
    green *= 256
    blue *= 256

    if red > 200 and green < 100 and blue < 100:
        return "red"
    elif red > 200 and green > 100 and blue < 100:
        return "orange"
    elif red > 200 and green > 200 and blue < 100:
        return "yellow"
    elif red < 100 and green > 200 and blue < 100:
        return "green"
    elif red < 100 and green < 100 and blue > 200:
        return "blue"
    elif red > 200 and green < 100 and blue > 200:
        return "purple"
    elif red < 100 and green < 100 and blue < 100:
        return "black"
    elif red > 200 and green > 200 and blue > 200:
        return "white"
    else:
        return "Unknown"
    
NUM_COLOURS = 10000
OUTPUT_FILE_NAME = "generated_colours.txt"
output_list = []

for i in range(0, NUM_COLOURS):
    rgb = tuple([random.random() for _ in range(0,3)])
    colour = identify_color(rgb)
    if colour != "Unknown":
        output_list.append(f"{rgb[0]} {rgb[1]} {rgb[2]} {colour}")

with open(OUTPUT_FILE_NAME, "w") as f:
    for line in output_list:
        f.write(line+"\n")