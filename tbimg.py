from PIL import Image, ImageDraw

def build_image(background_buff, tb_buff):
    background_img = Image.open(background_buff)
    tb_logo = Image.open(tb_buff)

    width, height = background_img.size
    # creates opaque rectangle
    rect = Image.new('RGBA', (width, 65))
    rdraw = ImageDraw.Draw(rect);
    rdraw.rectangle(((-1, -1), (width + 1, 66)), fill=(255,255,255,127), outline=(255,255,255,255))
    rect.paste(tb_logo, (20, 20), mask=tb_logo)
    background_img.paste(rect, (0, 0), mask=rect)

    return background_img
