#!/usr/bin/env python3
"""
Simple Image Renamer
A simplified version for quick batch renaming of images.
"""

import os
import sys
from pathlib import Path

def rename_images_in_folder(folder_path):
    """
    Rename all image files in a folder to 0001, 0002, etc.
    
    Args:
        folder_path: Path to the folder containing images
    """
    # Common image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist!")
        return
    
    # Get all image files
    image_files = []
    for file in folder.iterdir():
        if file.is_file() and file.suffix.lower() in image_extensions:
            image_files.append(file)
    
    # Sort files by name
    image_files.sort()
    
    if not image_files:
        print(f"No image files found in '{folder_path}'")
        return
    
    print(f"Found {len(image_files)} image files")
    print("Renaming files...")
    
    # Rename files
    for i, file_path in enumerate(image_files, 1):
        # Create new filename: 0001.jpg, 0002.png, etc.
        new_name = f"{i:04d}{file_path.suffix.lower()}"
        new_path = folder / new_name
        
        # Skip if already correctly named
        if file_path.name == new_name:
            continue
            
        # Rename the file
        try:
            file_path.rename(new_path)
            print(f"  {file_path.name} -> {new_name}")
        except Exception as e:
            print(f"  Error renaming {file_path.name}: {e}")
    
    print("Done!")

if __name__ == "__main__":
    # Check if folder path is provided as command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 simple_rename.py <folder_path>")
        print("Example: python3 simple_rename.py /path/to/photos")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    rename_images_in_folder(folder_path)