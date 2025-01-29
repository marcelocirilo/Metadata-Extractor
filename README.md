# EXIF Metadata Extractor

A Python-based tool for extracting and displaying EXIF metadata from image files. This project leverages the Pillow library to parse and display image metadata in a user-friendly way.

## Features
- Extract EXIF metadata from images.
- Display information such as:
  - Camera make and model.
  - Date and time the photo was taken.
  - GPS location (if available).
- Handle images without EXIF data gracefully.
- Validate the existence of image files before processing.

## Prerequisites
- Python 3.6+
- Pillow

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/exif-metadata-extractor.git
cd exif-metadata-extractor
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the script:
```bash
python main.py
```
2. Enter the path to the image when prompted:
```bash
Path of the image: /path/to/your/image.jpg
```
3. View the extracted EXIF metadata in the terminal.

## Project Structure
```bash
exif-metadata-extractor/
├── main.py              # Entry point for the program
├── extractor/           # Module containing the extractor logic
│   ├── __init__.py      # Contains the Extractor class
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

## Example Output
### Image with EXIF Data
```bash
Path of the image: example.jpg
Make: Canon
Model: Canon EOS 80D
DateTime: 2023:12:25 10:30:45
FNumber: 2.8
ExposureTime: 1/250
ISO: 100
```

### Image without EXIF Data
```bash
Path of the image: example.jpg
No EXIF data found.
```

### Invalid File Path
```bash
Path of the image: nonexistent.jpg
File not found. Please provide a valid path.
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Pillow Library for image handling.
EXIF metadata format documentation from Exif.org.
