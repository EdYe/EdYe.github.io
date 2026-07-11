#!/usr/bin/env python3
"""Convert PNG image(s) to JPEG format.

Usage:
    python3 convert_png_to_jpeg.py <input.png> [output.jpg]
    python3 convert_png_to_jpeg.py <directory> [--recursive]
"""

import argparse
import sys
from pathlib import Path

from PIL import Image


def convert_png_to_jpeg(input_path: Path, output_path: Path | None = None, quality: int = 90) -> Path:
    if output_path is None:
        output_path = input_path.with_suffix(".jpeg")

    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=quality)

    return output_path


def find_png_files(directory: Path, recursive: bool) -> list[Path]:
    pattern = "**/*.png" if recursive else "*.png"
    return sorted(directory.glob(pattern))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PNG image(s) to JPEG format.")
    parser.add_argument("input", type=Path, help="Path to a PNG file or a directory containing PNG files")
    parser.add_argument("output", type=Path, nargs="?", default=None, help="Output file path (only valid for single-file input)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into subdirectories when input is a directory")
    parser.add_argument("-q", "--quality", type=int, default=90, help="JPEG quality, 1-100 (default: 90)")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: {args.input} does not exist", file=sys.stderr)
        sys.exit(1)

    if args.input.is_dir():
        if args.output is not None:
            print("Error: output path is not supported when input is a directory", file=sys.stderr)
            sys.exit(1)

        png_files = find_png_files(args.input, args.recursive)
        if not png_files:
            print(f"No PNG files found in {args.input}")
            return

        for png_file in png_files:
            out = convert_png_to_jpeg(png_file, quality=args.quality)
            print(f"Converted: {png_file} -> {out}")
    else:
        out = convert_png_to_jpeg(args.input, args.output, quality=args.quality)
        print(f"Converted: {args.input} -> {out}")


if __name__ == "__main__":
    main()
