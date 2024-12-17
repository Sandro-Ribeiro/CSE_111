
import os
import subprocess
from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS

# Path to the folder containing images
image_folder = "/home/sandro/Imagens/Photos"
output_file = "/home/sandro/Imagens/metadata.txt"

# Function to extract EXIF metadata from an image
def extract_exif(image_path):
    try:
        # Opens the image file
        image = Image.open(image_path)

        # Retrieves EXIF metadata
        exif_data = image._getexif()

        # verifies if exif_data exist
        if exif_data:
            # Converts EXIF tags from numeric keys to names
            return {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
        else:
            # returns None if exif_data doesn't exist
            return None
    
    # Handle invalid or corrupted image files   
    except UnidentifiedImageError:
        print(f"Error: {image_path} is not a valid image or is corrupted.")
        return None

    except Exception as e:
        print(f"Unknown error processing {image_path}: {e}")
        return None
    
def get_interpreted_makernote(image_path):
    try:
        # Run the exiftool comand to get MakeNote
        result = subprocess.run(
            ["/usr/bin/exiftool", "-MakerNotes", image_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running exiftool on {image_path}: {e}")
        return "MakerNote: Failed to interpret"

def main():
    n = 0
    # Open in append mode
    with open(output_file, "a") as file:
        # Walk through the folder structure
        for root, dirs, files in os.walk(image_folder):
            for filename in files:
                #check for supported image file extensions
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                    #get the Full path to the image
                    image_path = os.path.join(root, filename)
                    print(f"Processing: {image_path}")
                    exif_data = extract_exif(image_path)

                    # wirtes the EXIF metadata to the output file
                    n += 1
                    file.write(f"{n} - Metadata for {image_path}:\n")
                    if exif_data:
                        for tag, value in exif_data.items():
                            # Replace MakerNote with interpreted data
                            if tag == "MakerNote":
                                value = get_interpreted_makernote(image_path)
                            file.write(f"{tag}: {value}\n")
                    else:
                        file.write(f"No EXIF metadata found\n")
                    file.write("\n")

    print(f"EXIF metadata saved to {output_file}")

if __name__ == "__main__":
    main()
    
