# Step 1: Read a file and print its contents
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n📂 File Content:\n", content)
except FileNotFoundError:
    print("❌ Error: File not found.")


# Step 2: Handle more errors
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n📂 File Content:\n", content)
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: Permission denied when trying to open the file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")

