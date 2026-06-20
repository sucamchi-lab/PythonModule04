import sys
import typing
import io


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_stream_management.py <file>")
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

        lines: list[str] = content.splitlines()
        transformed_lines: list[str] = [line + "#" for line in lines]
        transformed: str = "\n".join(transformed_lines)
        print("Transform data:")
        print("---")
        print(transformed)
        print("---")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_name: str = sys.stdin.readline().strip()
        if new_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            try:
                new_file: typing.TextIO = io.open(new_name, "w")
                new_file.write(transformed + "\n")
                new_file.close()
                print(f"Data saved in file '{new_name}'.")
            except OSError as e:
                print(f"[STDERR] Error opening file '{new_name}': {e}",
                      file=sys.stderr,)
                print("Data not saved.")
    except OSError as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}",
              file=sys.stderr,)
        return


if __name__ == "__main__":
    main()
