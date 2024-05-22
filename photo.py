# Importing the necessary libraries
import os
from prettytable import PrettyTable
from PIL import Image, ImageFilter

# Supported extensions
extensions = [".jpg", ".png", ".jpeg"]

# These 3 are the columns of the tables
t = PrettyTable(["Sr. No.", "Image", "File Size"])

# Adding the title to the table
t.title = f"Files at {os.getcwd()}"

# To insert rows
for i, file in enumerate(os.listdir(os.getcwd())):
    file_size = os.path.getsize(file)
    t.add_row([i + 1, file, file_size])

# Printing the table
print(t)

while True:
    try:
        # Getting the Serial Number
        sr_no = input("Sr. No.: ")

        if int(sr_no) > 0:
            # If the serial number is a valid number

            file_name: str = os.listdir(os.getcwd())[int(sr_no) - 1]

            # Get the file extension
            extension = os.path.splitext(file_name)[1]

            # If the file extension is a valid extension
            if extension in extensions:

                # Open the image
                image = Image.open(file_name)

                blur_radius = input("Enter the blur radius: ")
                try:

                    # If the blur radius is a valid integer
                    if int(blur_radius) > 0:

                        # Getting the width and the height of the image
                        width = image.width
                        height = image.height

                        radius = int(blur_radius)

                        # Applying the Gaussian Blur filter
                        blurred_image = image.filter(ImageFilter.GaussianBlur(radius))

                        # Cropping the original image
                        cropped_image = image.crop(
                            (radius, radius, int(width - radius), int(height - radius))
                        )

                        # Pastin the cropped image over the blurred image
                        blurred_image.paste(
                            cropped_image,
                            (
                                int((blurred_image.width - cropped_image.width) / 2),
                                int((blurred_image.height - cropped_image.height) / 2),
                            ),
                        )

                        # Rotating the image to suit the best needs
                        transposed_image = blurred_image.transpose(Image.ROTATE_270)

                        # Saving the file
                        transposed_image.save(
                            f"{os.path.splitext(file_name)[0]}_blurred{extension}"
                        )

                        break

                # In case of a ValueError ask for the input again

                except ValueError:
                    blur_radius = input("Enter the blur radius: ")

            else:

                # If the file does not end with a valid extension
                print("File does not end with a valid extension")

    except ValueError:

        # If the serial number is not a valid integer
        sr_no = input("Sr. No.: ")

    except IndexError:

        # If the serial number is not in the list of the files
        print("File not found")

    except KeyboardInterrupt:
        print("You exited")
        break
