from rgbmatrix import RGBMatrix, RGBMatrixOptions
from dateutil import parser
from PIL import Image, ImageDraw, ImageFont
import os
import math

class MatrixDisplay:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rgbMatrixOptions = RGBMatrixOptions()
        self.init_rgb_matrix()

        self.matrix = RGBMatrix(options = self.rgbMatrixOptions) # rows, chain length
        self.font = ImageFont.load(os.path.dirname(os.path.realpath(__file__))+ '/Resources/helvR08.pil')
        self.init_image_draw()

    def init_image_draw(self):
        self.image = Image.new('RGB', (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)
    
    def init_rgb_matrix(self):
        self.rgbMatrixOptions.rows = self.height
        self.rgbMatrixOptions.cols = self.width
        self.rgbMatrixOptions.chain_length = 1
        self.rgbMatrixOptions.parallel = 1
        self.rgbMatrixOptions.hardware_mapping = 'adafruit-hat'
    
    def loadImage(self, path = 'Utils/Resources/Biketown_logo.png'):
        self.im1 = Image.open(path)
    
    def pasteOnto(self, coords=(0,0)):
        self.image.paste(self.im1, coords)

    def draw_horizontal_divder(self):
        self.draw.rectangle((0, 16, 64, 16), fill="#b5b5b5")

    def draw_vertical_divider(self):
        self.draw.rectangle((16, 0, 16, 32), fill="#b5b5b5")

    def draw_route_sign(self, anchor_x, anchor_y, width, height, route_string, fill_color, text_color):
        w, h = self.draw.textsize(route_string, font= self.font)
        h += int(h*0.15)
        w += int(w*0.09)
        self.draw.rounded_rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill=fill_color, radius=3)
        self.draw.text((((width-w)/2) + anchor_x, ((height-h)/2) + anchor_y), route_string, fill=text_color, font= self.font)

    def draw_interstate_highway_sign(self, anchor_x, anchor_y, width, height, route_string):
        w, h = self.draw.textsize(route_string, font= self.font)
        h += int(h*0.01)
        w += int(w*0.09)
        self.draw.rounded_rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill=(11, 62, 132), radius=3)
        self.draw.rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + 2], fill=(174, 42, 49))
        self.draw.text((((width-w)/2) + anchor_x, ((height-h)/2) + anchor_y), route_string, fill="#b5b5b5", font= self.font)

    def draw_oregon_highway_sign(self, anchor_x, anchor_y, width, height, route_string):
        w, h = self.draw.textsize(route_string, font= self.font)
        h += int(h*0.01)
        w += int(w*0.09)
        self.draw.rounded_rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill="#2e2e2e", radius=3)
        self.draw.text((((width-w)/2) + anchor_x, ((height-h)/2) + anchor_y), route_string, fill="#b5b5b5", font= self.font)

    def draw_state_route_sign(self, anchor_x, anchor_y, width, height, route_string):
        w, h = self.draw.textsize(route_string, font= self.font)
        h += int(h*0.01)
        w += int(w*0.09)
        self.draw.rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill="#112b19")
        self.draw.text((((width-w)/2) + anchor_x, ((height-h)/2) + anchor_y), route_string, fill="#b5b5b5", font= self.font)

    def drawRectangle(self, anchor_x, anchor_y, width, height, fill):
        self.draw.rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill=fill)

    def draw_text(self, anchor_x, anchor_y, text, color="#b5b5b5"):
        self.draw.text((anchor_x, anchor_y), text, fill=color, font= self.font)

    def draw_arrival(self, anchor_x, anchor_y, text):
        splits = text.split()
        splitAt = math.floor(len(splits)/2)
        topText = splits[0:splitAt]
        bottomText = splits[splitAt:len(splits)]
        self.draw_text(anchor_x, anchor_y, ' '.join(topText))
        self.draw_text(anchor_x + 1, anchor_y + 7, ' '.join(bottomText))

    def draw_route_border(self, anchor_x, anchor_y, width, height, border_color):
        self.draw.rectangle((anchor_x, anchor_y, anchor_x+width, anchor_y), fill=border_color)
        self.draw.rectangle((anchor_x, anchor_y+height, anchor_x+width, anchor_y+height), fill=border_color)
        self.draw.rectangle((anchor_x, anchor_y, anchor_x, anchor_y+height), fill=border_color)
        self.draw.rectangle((anchor_x+width, anchor_y, anchor_x+width, anchor_y+height), fill=border_color)


    def draw_estimate(self, anchor_x, anchor_y, date_time_string):
        date_time = parser.parse(date_time_string)
        self.draw_text(anchor_x, anchor_y, date_time.strftime('%a %H:%M'))

    def clear_screen(self):
        self.matrix.Clear()

    def paint_black(self):
        # Clear background
        self.draw.rectangle((0, 0, self.width, self.height), fill=(0, 0, 0))
        self.matrix.SetImage(self.image.convert('RGB'))

    def paint_solid_color_background(self, fill=(0,0,0)):
        self.draw.rectangle((0, 0, self.width, self.height), fill=fill)

    def setImage(self):
        print("Draw!")
        self.matrix.SetImage(self.image.convert('RGB'))
