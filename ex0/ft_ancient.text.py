import sys
import typing
import io


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient.text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file: '{sys.argv[1]}'")
    try:
        file: typing.TextIO = io.open(sys.argv[1], "r")
        content = file.read()
        print("---\n")
        print(content)
        file.close()
        print(f"\n---\nFile '{sys.argv[1]}' closed")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return


if __name__ == "__main__":
    main()
