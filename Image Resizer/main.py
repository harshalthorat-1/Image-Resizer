import cv2 as cv


img = "bat_man.jpeg"
newImg = f'3New_{img}'
scale_percent = 50


# Load Img
src = cv.imread(img, cv.IMREAD_UNCHANGED)

# Check if image was loaded
if src is None:
    print("Image not found. Check the file path.")
else:
    # output = cv.resize(src, (899, 1599)) #coutimizeable

    new_widht = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)

    #resize

    output =cv.resize(src,(new_widht,new_height),interpolation=cv.INTER_AREA)
    cv.imwrite(newImg,output)
    cv.imshow("BatMan" , output)
    cv.waitKey(0)

