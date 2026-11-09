from pathlib import Path

from pdf417gen import encode, render_image


def generate_barcode(
    data: str,
    output_filename: str = "test_barcode.png",
) -> Path:
    """Create a PDF417 barcode image and return its path."""
    path = Path(output_filename)
    if path.suffix.lower() != ".png":
        path = path.with_suffix(".png")

    codes = encode(data, columns=6, security_level=3)
    image = render_image(codes, scale=4, ratio=3, padding=20)
    image.save(path)

    print(f"Barcode saved to: {path}")
    return path