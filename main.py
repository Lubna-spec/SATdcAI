import cv2
import numpy as np

def detect_changes(image1_path, image2_path, threshold=25):
    """Detects changes between two images.

    Args:
        image1_path: Path to the first image.
        image2_path: Path to the second image.
        threshold: Pixel intensity difference threshold for change detection.

    Returns:
        A difference image highlighting the changed areas.
    """

    # Read the images
    image1 = cv2.imread("C:\\Users\\lubna\\OneDrive\\Desktop\\lubna\\ai\\gk\\b.jpg")
    image2 = cv2.imread("C:\\Users\\lubna\\OneDrive\\Desktop\\lubna\\ai\\gk\\c.jpg")

    # Convert to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Compute absolute difference
    diff = cv2.absdiff(gray1, gray2)

    # Apply threshold to create binary mask
    _, mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    return mask

if _name_ == '_main_':
    image1_path = "image1.jpg"
    image2_path = "image2.jpg"

    change_mask = detect_changes(image1_path, image2_path)

    # Display the result
    cv2.imshow("Change Mask", change_mask)
    cv2.waitKey(0)
