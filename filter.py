#import the graphic library
from graphics import*

#import the sys library to use the exit function
import sys

#Implementation of the grayscaleFilter function
def grayscaleFilter(ImageN):
    
    #construct an image object to manipulate the photo
    img = Image(Point(100,100),ImageN)

    #get the width and the height of the image
    width = img.getWidth()
    height = img.getHeight()

    #loop through each pixel 
    for x in range(width):
        for y in range(height):
            
            # get the rgb value of each pixel and find their average
            red,green,blue = img.getPixel(x,y)
            average = round((red+green+blue)/3)

            #replace the pixel color by using the previous average as rgb values
            img.setPixel(x,y,color_rgb(average,average,average))
    #save the image on wihich the grayscale filter has been applied
    img.save("gray.gif")

#implementation of the sierraFilter function 
def sierraFilter(ImageN):
    
    #construct an image object to manipulate the photo
    img = Image(Point(100,100),ImageN)

    #get the width and the height of the image
    width = img.getWidth()
    height = img.getHeight()

    #loop through each pixel
    for x in range(width):
        for y in range(height):

            #get the rgb values of each pixel and apply the formula below to find the new rgb values
            red,green,blue = img.getPixel(x,y)
            sepiaR = round((0.393 * red) + (0.769 * green) + (0.189 * blue))
            sepiaG = round((0.349 * red) + (0.686 * green) + (0.168 * blue))
            sepiaB = round((0.272 * red) + (0.534 * green) + (0.131 * blue))

            #replace the pixel color using the new rgb values
            img.setPixel(x,y,color_rgb(sepiaR,sepiaG,sepiaB))
            
    #save the image on wihich the sierra filter has been applied
    img.save("sierra.gif")
    
#Implement the main function of our program        
def main():
    
    #print a welcome message to the user
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Welcome to Image Filter")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    #prompt the user for the image name and check whether they collaborated
    imageName = input("Enter the image name here.Please enter .gif image(e.g photo.gif): ")

    #if the user did not collaborate, print an error message and exit the program
    if imageName[len(imageName)-4:] != ".gif":
        print("you did not input a .gif photo .Please TRY AGAIN")
        sys.exit(0)
        
    #if the user inputted a correct name, prompt them for the filter the would like to apply(grayscale or sierra)
    filterName = input("Input the filter name in lowercase or uppercase(g, grayscale, s, or sierra): ")

    #create a list of possible filters
    filterList = ["g","grayscale","s","sierra"]

    #if the user did not inputted the right filter, print an error message
    if filterName.lower() not in filterList:
        print("The fiter you have inputted is not availible.")
        
    #if the user collaborated, call the grayscale or the sierra function to apply a filter on the image
    else:
        if filterName.lower() =="g" or filterName.lower()=="grayscale":
            grayscaleFilter(imageName)
        else:
            sierraFilter(imageName)
main()
