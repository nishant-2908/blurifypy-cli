# blurify-cli
Python CLI Script to blur the edges of an image
### Project: Blur Photo
- Prints the file in the working directory
- Let the user input a serial number
- Get the file properties
- Blurring the photo using Image library in Python
- Takes input for filename (current directory) and blur radius
- Crops the original image to the twice of the radius from the original width and height
- Blurs the original image to the radius with the Gaussian Blur filter
- Rotates the image to suit the best needs
- Paste the cropped image over the blurred image centrally
- Save the image

### Libraries used used: Image (from PIL), ImageFilter (from PIL)
### Only supports .jpg, .jpeg, .png