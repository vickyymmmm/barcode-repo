from pathlib import Path

from PIL import Image
from pdf417decoder import PDF417Decoder


def verify_barcode(image_path: str | Path, expected_data: str) -> bool:
    """Decode a PDF417 image and compare it with the expected test data."""
    with Image.open(image_path) as image:
        decoder = PDF417Decoder(image)

        if decoder.decode() <= 0:
            raise RuntimeError("No PDF417 barcode could be decoded.")

        decoded_data = decoder.barcode_data_index_to_string(0)

    if isinstance(decoded_data, bytes):
        decoded_data = decoded_data.decode("utf-8")

    if decoded_data != expected_data:
        raise ValueError("Decoded barcode data does not match the input.")

    print(f"Barcode verified: {image_path}")
    return True