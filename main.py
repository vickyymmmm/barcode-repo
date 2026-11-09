from barcode_generator import generate_barcode
from barcode_verifier import verify_barcode


def main() -> None:
    # Use synthetic test data only.
    test_data = "TEST|asset-123|status-active"

    image_path = generate_barcode(test_data)
    verify_barcode(image_path, test_data)


if __name__ == "__main__":
    main()