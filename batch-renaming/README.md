# Batch Image Renaming Scripts

Two Python scripts for batch renaming image files in a folder with sequential numbering starting from 0001.

## Scripts

### 1. `batch_rename_images.py` (Full-featured)

A comprehensive script with advanced features and command-line interface.

**Features:**
- Supports many image formats (jpg, jpeg, png, gif, bmp, tiff, webp, svg, ico, raw, cr2, nef, arw)
- Command-line interface with options
- Dry-run mode to preview changes
- Custom starting number
- Error handling and validation
- Skips files that are already correctly named

**Usage:**
```bash
# Basic usage
python3 batch_rename_images.py /path/to/your/photos

# Preview changes without renaming (dry-run)
python3 batch_rename_images.py /path/to/your/photos --dry-run

# Start numbering from a different number
python3 batch_rename_images.py /path/to/your/photos --start-number 100

# Combine options
python3 batch_rename_images.py /path/to/your/photos --dry-run --start-number 50
```

### 2. `simple_rename.py` (Easy to use)

A simplified script for quick and easy batch renaming.

**Features:**
- Command-line argument for folder path
- Supports common image formats (jpg, jpeg, png, gif, bmp, tiff, webp)
- Automatic sequential numbering from 0001
- Simple error handling

**Usage:**
```bash
python3 simple_rename.py /path/to/your/photos
```

## Example

Before:
```
IMG_20231201_143022.jpg
DSC_0891.jpg
photo.png
image (1).jpg
```

After:
```
0001.jpg
0002.jpg
0003.png
0004.jpg
```

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Notes

- Both scripts preserve the original file extensions
- Files are sorted alphabetically before renaming
- The scripts will skip files that are already correctly named
- Both scripts convert extensions to lowercase for consistency