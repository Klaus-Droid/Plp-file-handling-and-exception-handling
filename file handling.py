"""
File Manager: Read, Modify & Write
---------------------------------
This script demonstrates safe file handling in Python.
It reads a file, modifies its content, and writes the result
to a new file while handling errors gracefully.

Author: Emmanuel Chege
"""

def modify_content(content: str) -> str:
    """
    Modify the content of the file.
    Example: Convert text to uppercase and add line numbers.
    """
    lines = content.splitlines()
    modified_lines = [f"{idx+1}: {line.upper()}" for idx, line in enumerate(lines)]
    return "\n".join(modified_lines)


def process_file(input_file: str, output_file: str):
    """
    Reads from input_file, modifies its content,
    and writes it to output_file.
    Handles errors gracefully.
    """
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            content = infile.read()

        modified = modify_content(content)

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(modified)

        print(f"✅ File processed successfully! Output saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied for '{input_file}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    filename = input("📂 Enter the filename to read: ").strip()
    process_file(filename, "output.txt")
