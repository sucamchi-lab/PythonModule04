import sys
import typing
import io


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file: typing.TextIO = io.open(sys.argv[1], "r")
        content = file.read()
        file.close()
        print("---\n")
        print(content)
        print("---\n")
        print(f"File '{sys.argv[1]}' closed.")

        lines = content.splitlines()
        transformed_lines = [line + "#" for line in lines]
        transformed = "\n".join(transformed_lines)
        print("Transform data:")
        print("---")
        print(transformed)
        print("---")

        new_name: str = input("Enter new file name (or empty): ")
        if new_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            new_file: typing.TextIO = io.open(new_name, "w")
            new_file.write(transformed + "\n")
            new_file.close()
            print(f"Data saved in file '{new_name}'.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return


if __name__ == "__main__":
    main()
