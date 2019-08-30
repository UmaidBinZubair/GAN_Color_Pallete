import json
import cv2
import numpy as np


f=open("colors_data.txt", "r")
contents = f.readlines()
l = len(contents)
con_1 = contents[0:int(l*0.2)]
con_2 = contents[int(l*0.2):int(l*0.6)]
con_3 = contents[int(l*0.6):]

con = [con_1,con_2,con_3]
for miss,content in enumerate(con):
	for list in content:
		content = json.loads(list)
		image = np.zeros((150,1000,3),np.uint8)
		num = np.random.choice(5,4-miss,replace = False)
		print(num)
		i=0
		for col_num,color in enumerate(content['result']):
			for i in num:
				if i == col_num:
					image[:,i*200:((i+1)*200)-1,:] = color
			i+=1

		cv2.imshow('Colors', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(0) & 0xff == ord('q'):
			break


