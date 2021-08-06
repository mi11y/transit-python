import atexit
from PIL import Image, ImageDraw, ImageFont
import math
import os
import time
from dateutil import parser
from rgbmatrix import RGBMatrix, RGBMatrixOptions

height = 32
width = 64
options = RGBMatrixOptions()
options.rows = height
options.cols = width
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
matrix         = RGBMatrix(options = options) # rows, chain length

font           = ImageFont.load(os.path.dirname(os.path.realpath(__file__))
                   + '/helvR08.pil')
fontYoffset    = -2  # Scoot up a couple lines so descenders aren't cropped

image       = Image.new('RGB', (width, height))
draw        = ImageDraw.Draw(image)

def clearOnExit():
    matrix.Clear()

atexit.register(clearOnExit)

def draw_horizontal_divder():
    draw.rectangle((0, 16, 64, 16), fill=(64, 64, 64))

def draw_vertical_divider():
    draw.rectangle((16, 0, 16, 32), fill=(64, 64, 64))


def draw_route_sign(anchor_x, anchor_y, width, height, route_string, fill_color, text_color):
    w, h = draw.textsize(route_string, font=font)
    h += int(h*0.15)
    w += int(w*0.09)
    draw.rounded_rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill=fill_color, radius=5)
    draw.text((((width-w)/2) + anchor_x, ((height-h)/2) + anchor_y), route_string, fill=text_color, font=font)

def draw_text(anchor_x, anchor_y, text):
    draw.text((anchor_x, anchor_y), text, fill="#4d4d4d", font=font)

def draw_arrival(anchor_x, anchor_y, text):
    splits = text.split('&')
    draw_text(anchor_x, anchor_y, splits[0])
    draw_text(anchor_x - 2, anchor_y + 7, splits[1])

def draw_estimate(anchor_x, anchor_y, date_time_string):
    date_time = parser.parse(date_time_string)
    draw_text(anchor_x, anchor_y, date_time.strftime('%a %I:%M %p'))

swap_current_time = time.time()
next_route_current_time = time.time()
swap_prev_time = time.time()
next_route_prev_time = time.time()
show_estimates = False
while True:


    draw_horizontal_divder()

    matrix.SetImage(image.convert('RGB'))
    
    draw_route_sign(2, 2, 12, 12, "8", "#042340", "#000")
    draw_route_sign(2, 18, 12, 12, "12", "#042340", "#000")

    swap_current_time = time.time()
    estimates_swap_time_delta = (swap_current_time - swap_prev_time)
    if(estimates_swap_time_delta > 5):
        print("Swap!")
        show_estimates = not show_estimates
        print("show estimates? ")
        print(show_estimates)
        swap_prev_time = swap_current_time

        # Clear background
        draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
        matrix.SetImage(image.convert('RGB'))


    if(show_estimates):
        draw_estimate(14, -1, "2021-08-06T06:25:00+00:00")
        draw_estimate(14, 15, "2021-08-06T06:46:00+00:00")
    else:
        draw_arrival(14, -1, "SW 5th & Morrison")
        draw_arrival(14, 15, "SW 6th & Yamhill")

    next_route_current_time = time.time()
    next_route_time_delta = (next_route_current_time - next_route_prev_time)
    if(next_route_time_delta > 30):
        print("Next route!")
        next_route_prev_time = next_route_current_time
        swap_prev_time = next_route_current_time
        next_route_prev_time = next_route_current_time

