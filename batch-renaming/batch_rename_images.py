#!/usr/bin/env python3
"""
Batch Image Renamer
Renames all image files in a folder sequentially starting from 0001.
"""

import os
import sys
from pathlib import Path
from typing import List, Set

# Supported image file extensions
IMAGE_EXTENSIONS: Set[str] = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
    '.webp', '.svg', '.ico', '.raw', '.cr2', '.nef', '.arw'
}

def get_image_files(folder_path: Path) -> List[Path]:
    """
    Get all image files from the specified folder.
    
    Args:
        folder_path: Path to the folder containing images
        
    Returns:
        List of image file paths sorted by name
    """
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")
    
    image_files = []
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in IMAGE_EXTENSIONS:
            image_files.append(file_path)
    
    # Sort files by name to ensure consistent ordering
    return sorted(image_files)

def rename_images(folder_path: str, start_number: int = 1, dry_run: bool = False) -> None:
    """
    Rename all image files in a folder sequentially.
    
    Args:
        folder_path: Path to the folder containing images
        start_number: Starting number for renaming (default: 1)
        dry_run: If True, only show what would be renamed without actually renaming
    """
    folder = Path(folder_path).resolve()
    
    try:
        image_files = get_image_files(folder)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
        return
    
    if not image_files:
        print(f"No image files found in {folder}")
        return
    
    print(f"Found {len(image_files)} image files in {folder}")
    
    if dry_run:
        print("\nDry run - showing what would be renamed:")
    else:
        print("\nRenaming files:")
    
    renamed_count = 0
    
    for i, file_path in enumerate(image_files, start=start_number):
        # Generate new filename with 4-digit zero-padded number
        new_name = f"{i:04d}{file_path.suffix.lower()}"
        new_path = folder / new_name
        
        # Skip if the file already has the target name
        if file_path.name == new_name:
            print(f"  Skipping {file_path.name} (already correctly named)")
            continue
        
        # Check if target filename already exists
        if new_path.exists() and new_path != file_path:
            print(f"  Warning: Target file {new_name} already exists, skipping {file_path.name}")
            continue
        
        if dry_run:
            print(f"  {file_path.name} -> {new_name}")
        else:
            try:
                file_path.rename(new_path)
                print(f"  {file_path.name} -> {new_name}")
                renamed_count += 1
            except OSError as e:
                print(f"  Error renaming {file_path.name}: {e}")
    
    if not dry_run:
        print(f"\nSuccessfully renamed {renamed_count} files")
    else:
        print(f"\nWould rename {len([f for f in image_files if f.name != f'{image_files.index(f)+start_number:04d}{f.suffix.lower()}'])} files")

def main():
    """Main function to handle command-line interface."""
    if len(sys.argv) < 2:
        print("Usage: python3 batch_rename_images.py <folder_path> [--dry-run] [--start-number N]")
        print("\nOptions:")
        print("  --dry-run        Show what would be renamed without actually renaming")
        print("  --start-number N Start numbering from N (default: 1)")
        print("\nExample:")
        print("  python3 batch_rename_images.py /path/to/photos")
        print("  python3 batch_rename_images.py /path/to/photos --dry-run")
        print("  python3 batch_rename_images.py /path/to/photos --start-number 100")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    start_number = 1
    
    # Parse start number if provided
    if '--start-number' in sys.argv:
        try:
            start_idx = sys.argv.index('--start-number')
            if start_idx + 1 < len(sys.argv):
                start_number = int(sys.argv[start_idx + 1])
            else:
                print("Error: --start-number requires a number")
                sys.exit(1)
        except (ValueError, IndexError):
            print("Error: Invalid start number")
            sys.exit(1)
    
    print(f"Batch Image Renamer")
    print(f"Folder: {folder_path}")
    print(f"Starting number: {start_number}")
    print(f"Supported formats: {', '.join(sorted(IMAGE_EXTENSIONS))}")
    print("-" * 50)
    
    rename_images(folder_path, start_number, dry_run)

if __name__ == "__main__":
    main()