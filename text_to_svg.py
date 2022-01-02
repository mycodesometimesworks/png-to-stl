from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class TextToSVG:
    def __init__(self, fontname, fontsize, text_color, text_outline_color, background_color, image_border_size=4, text_border_size=3):
        self.fontname = fontname
        self.fontsize = fontsize
        self.text_color = text_color
        self.text_outline_color = text_outline_color
        self.background_color = background_color
        self.image_border_size = image_border_size
        self.text_border_size = text_border_size

    def estimate_text_size(self, txt, font):
        testImg = Image.new('RGB', (1, 1))
        testDraw = ImageDraw.Draw(testImg)
        return testDraw.textsize(txt, font)

    def image_draw_text(self, text_input, output_filename):
        font = ImageFont.truetype(self.fontname, self.fontsize)
        image_width, image_height = self.estimate_text_size(text_input, font)
        img = Image.new('RGB', (image_width + self.image_border_size, image_height + self.image_border_size), self.background_color)
        drawing = ImageDraw.Draw(img)
        drawing.text((2, 2), text_input, fill=self.text_color, font=font)
        if self.text_outline_color:
            drawing.rectangle((0, 0, width + self.text_border_size, height + self.text_border_size), outline=self.text_outline_color)
        img.save(output_filename)


if __name__ == "__main__":
    text_input = 'hello world'
    text_color = "black"
    output_filename = "intake/test_text.png"

    fontname = "ArundinaSans.ttf"
    fontsize = 40
    background_color = "white"
    text_outline_color = ""

    TextToSVGInstance = TextToSVG(fontname, fontsize, text_color, text_outline_color, background_color)
    TextToSVGInstance.image_draw_text(text_input, output_filename)
