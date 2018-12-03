from PIL import Image, ImageDraw, ImageFont
background_color = (147,253,160)
img = Image.new('RGB', (280,280), color = background_color)
d = ImageDraw.Draw(img)
number = "6"
color = (120,120,210)
font = ImageFont.truetype("TTF/ClearSans-Medium.ttf", 120)
d.text((40,45), number, fill=color, font=font, align = "right")
d.text((105,35), "x", fill=color, font=font, align = "right")
d.text((165,45), number, fill=color, font=font, align = "right")
img.save('6x6.png')
