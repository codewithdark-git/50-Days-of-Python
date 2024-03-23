# Import the OpenCV library
import cv2

# Read the input image
image1 = cv2.imread("input image path")

# Create a window for displaying the original image
window_name = 'Original Image'
# cv2.imshow(window_name , image1)

# Convert the image to grayscale
gray_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert = cv2.bitwise_not(gray_img)

# Apply Gaussian blur to the inverted image
blur = cv2.GaussianBlur(invert, (21, 21), 0)

# Invert the blurred image
invertedblur = cv2.bitwise_not(blur)

# Create a pencil sketch by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray_img, invertedblur, scale=256.0)

# Save the sketch as an image
cv2.imwrite("Where is sketch image save", sketch)

# Read the saved sketch image
image = cv2.imread("Where is sketch image save")

# Create a window for displaying the sketch image
window_name = 'Sketch Image'
# cv2.imshow(window_name, image)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
