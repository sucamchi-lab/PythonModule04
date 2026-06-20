def secure_archive(filename: str, action: str = "r", content: str = "",
                   ) -> tuple[bool, str]:
    try:
        if action == "w":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)
    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt"))
    print("Using 'secure_archive' to write previous content to a new file:")
    success, data = secure_archive("ancient_fragment.txt")
    if success:
        print(secure_archive("ancient_fragment_copy.txt", "w", data))
    else:
        print((success, data))


if __name__ == "__main__":
    main()
