# Step 1: Read a file and print its contents
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n📂 File Content:\n", content)
except FileNotFoundError:
    print("❌ Error: File not found.")
