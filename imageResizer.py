import cv2 as bv

path= input("Enter the path of the image: ")
img= bv.imread(path)
print("The image is of size: ", img.shape)
reduce= int(input("Enter the percentage by which you want to reduce the image size: "))
new= input("Enter the new file name: ")

new_height=int(img.shape[0]* reduce/100)
new_width=int(img.shape[1] * reduce / 100)

op= bv.resize(img, (new_width,new_height))
bv.imwrite(new, op)
bv.imread(new)
bv.imshow("tittle", img)
bv.waitKey(0)