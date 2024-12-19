import os
from PIL import Image


def create_image_with_metadata(output_dir, file_name, metadata=None):
    """
    Creates a blank image and adds custom EXIF metadata using ExifTool.
    :param output_dir: Directory where the image will be saved.
    :param file_name: Name of the image file.
    :param metadata: Dictionary containing EXIF metadata (optional).
    :return: Path to the created file.
    """
    image_path = os.path.join(output_dir, file_name)

    # Create a blank 100x100 pixel image
    image = Image.new("RGB", (100, 100), color="white")
    image.save(image_path, "JPEG")

    # Add EXIF metadata if provided
    if metadata:
        exiftool_command = f'exiftool {" ".join([f"-{key}={repr(value)}" for key, value in metadata.items()])} {repr(image_path)}'
        os.system(exiftool_command)
        # Remove the `_original` file created by ExifTool
        os.remove(image_path + "_original")

    return image_path


def create_non_image_file(output_dir, file_name):
    """
    Creates a non-image file for testing purposes.
    :param output_dir: Directory where the file will be saved.
    :param file_name: Name of the file.
    :return: Path to the created file.
    """
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w") as file:
        file.write("This is not an image file.")
    return file_path
