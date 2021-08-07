from rgbmatrix import RGBMatrix, RGBMatrixOptions
from dateutil import parser
from PIL import Image, ImageDraw, ImageFont
import os

class MatrixDisplay:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rgbMatrixOptions = RGBMatrixOptions()
        self.init_rgb_matrix()

        self.matrix = RGBMatrix(options = self.rgbMatrixOptions) # rows, chain length
        self.font = ImageFont.load(os.path.dirname(os.path.realpath(__file__))+ '/helvR08.pil')
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

    def draw_horizontal_divder(self):
        self.draw.rectangle((0, 16, 64, 16), fill=(64, 64, 64))

    def draw_vertical_divider(self):
        self.draw.rectangle((16, 0, 16, 32), fill=(64, 64, 64))

    def draw_route_sign(self, anchor_x, anchor_y, width, height, route_string, fill_color, text_color):
        w, h = self.draw.textsize(route_string, font= self.font)
        h += int(h*0.15)
        w += int(w*0.09)
        self.draw.rounded_rectangle([anchor_x, anchor_y, anchor_x + width, anchor_y + height], fill=fill_color, radius=5)
        self.draw.text((((width-w)/2) + anchor_x, ((height-h)/2) + anchor_y), route_string, fill=text_color, font= self.font)

    def draw_text(self, anchor_x, anchor_y, text):
        self.draw.text((anchor_x, anchor_y), text, fill="#4d4d4d", font= self.font)

    def draw_arrival(self, anchor_x, anchor_y, text):
        splits = text.split('&')
        self.draw_text(anchor_x, anchor_y, splits[0])
        self.draw_text(anchor_x - 2, anchor_y + 7, splits[1])

    def draw_estimate(self, anchor_x, anchor_y, date_time_string):
        date_time = parser.parse(date_time_string)
        self.draw_text(anchor_x, anchor_y, date_time.strftime('%a %I:%M %p'))
    
    def clear_screen(self):
        self.matrix.Clear()

    def paint_black(self):
        # Clear background
        self.draw.rectangle((0, 0, self.width, self.height), fill=(0, 0, 0))
        self.matrix.SetImage(self.image.convert('RGB'))
    
    def setImage(self):
        self.matrix.SetImage(self.image.convert('RGB'))
