from PIL import Image, ImageDraw, ImageFont
from number_dict import number_dict
import boto3
from io import BytesIO

destination_bucket = '2048gameyash'
s3 = boto3.resource('s3')

def curved_square(d, coordinated = (0,0), number = "0", temp = 3):
	width = 16-temp
	test_number = temp - 3
	d.ellipse((coordinated[0]*(float(dimention - width)/temp) + 4*width/5, coordinated[1]*(float(dimention - width)/temp) + 4*width/5, coordinated[0]*(float(dimention - width)/temp) + 4*width/5 + 10, coordinated[1]*(float(dimention - width)/temp) + 4*width/5 + 10), fill=number_dict[number]["backgroud_color"])
	d.ellipse(((coordinated[0] + 1)*(float(dimention - width)/temp) + 1*width/5 - 10, coordinated[1]*(float(dimention - width)/temp) + 4*width/5, (coordinated[0] + 1)*(float(dimention - width)/temp) + 1*width/5, coordinated[1]*(float(dimention - width)/temp) + 4*width/5 + 10), fill=number_dict[number]["backgroud_color"])
	d.ellipse((coordinated[0]*(float(dimention - width)/temp) + 4*width/5, (coordinated[1] + 1)*(float(dimention - width)/temp) + 1*width/5 - 10, coordinated[0]*(float(dimention - width)/temp) + 4*width/5 + 10, (coordinated[1] + 1)*(float(dimention - width)/temp) + 1*width/5), fill=number_dict[number]["backgroud_color"])
	d.ellipse(((coordinated[0] + 1)*(float(dimention - width)/temp) + 1*width/5 - 10, (coordinated[1] + 1)*(float(dimention - width)/temp) + 1*width/5 - 10, (coordinated[0] + 1)*(float(dimention - width)/temp) + 1*width/5, (coordinated[1] + 1)*(float(dimention - width)/temp) + 1*width/5), fill=number_dict[number]["backgroud_color"])
	d.rectangle((coordinated[0]*(float(dimention - width)/temp) + 4*width/5, coordinated[1]*(float(dimention - width)/temp) + 4*width/5 + 5, (coordinated[0] + 1)*(float(dimention - width)/temp) + 1*width/5, (coordinated[1] + 1)*(float(dimention - width)/temp) + 1*width/5 - 5), fill=number_dict[number]["backgroud_color"])
	d.rectangle((coordinated[0]*(float(dimention - width)/temp) + 4*width/5 + 5, coordinated[1]*(float(dimention - width)/temp) + 4*width/5, (coordinated[0] + 1)*(float(dimention - width)/temp) + 1*width/5 - 5, (coordinated[1] + 1)*(float(dimention - width)/temp) + 1*width/5), fill=number_dict[number]["backgroud_color"])
	if number != "0":
		font = ImageFont.truetype("TTF/ClearSans-Medium.ttf", number_dict[number]["font_size"][test_number])
		# print number_dict[number]["coordinate"][0]
		d.text((coordinated[0]*(float(dimention - width)/temp) + number_dict[number]["coordinate"][test_number][0],coordinated[1]*(float(dimention - width)/temp) + number_dict[number]["coordinate"][test_number][1]), number, fill=number_dict[number]["color"], font=font, align = "right")

def make_image(array, userid):
	img = Image.new('RGB', (dimention, dimention), color = (205,193,180))
	d = ImageDraw.Draw(img)
	temp = len(array)
	width = 16-temp
	for i in range(temp+1):
		#horizontal lines
		d.line((0,i*(float(dimention - width)/temp) + width/2 - 1, dimention,i*(float(dimention - width)/temp) + width/2 - 1), fill=(187,173,160), width=width)
		#vertical lines
		d.line((i*(float(dimention - width)/temp) + width/2 - 1,0, i*(float(dimention - width)/temp) + width/2 - 1,dimention), fill=(187,173,160), width=width)

	#add_a_box
	for i in range(temp):
		for j in range(temp):
			curved_square(d, coordinated = (j,i), number = str(array[i][j]), temp = temp)
	# curved_square(d, coordinated = coordinate_temp, number = number_temp)
	object_key = userid + '.png'
	extension = path.splitext(object_key)[1].lower()
	if extension in ['.jpeg', '.jpg']:
        format = 'JPEG'
    if extension in ['.png']:
        format = 'PNG'
    buffer = BytesIO()
    img.save(buffer, format)
    buffer.seek(0)
    obj = s3.Object(
        bucket_name=destination_bucket,
        key=object_key
    )
    obj.put(Body=buffer)
	# img.save('left.png')
	return "https://s3-eu-west-1.amazonaws.com/2048gameyash/" + object_key