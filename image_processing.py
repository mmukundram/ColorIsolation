import cv2
import math
image = cv2.imread("iDbWF.png")
colors = {}
vibgyor = [[148,0,211],[75,0,130],[0,0,255],[0,255,0],[255,255,0],[255,127,0],[255,0,0]]

def new_file_name(count):
	return str(count) + '.jpg'

count=0

def quantize(colors, my_color):
	distance = 500
	for i in range(0,len(colors)):
		color = colors[i]
		new_distance = math.sqrt((color[0]-my_color[0])**2 + (color[1]-my_color[1])**2 + (color[2]-my_color[2])**2)
		if new_distance < distance:
			quantized_color = color;
	print str(my_color) + ' quantized to ' + str(quantized_color)
	return quantized_color

for i in range(0,len(image)):
	for j in range(0,len(image[i])):
		key = ''
		if image[i,j][0] is not 255 and image[i,j][1] is not 255 and image[i,j][2] is not 255: 
			my_quantize = quantize(vibgyor,image[i,j])
			print(my_quantize)
			for item in my_quantize:
				key = key + str(item) + ',' 
			colors[key] = new_file_name(count)
			count = count + 1

print len(colors)



