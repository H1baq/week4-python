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


# Step 3: Ask user how they want to modify content
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as infile:
        content = infile.read()
        print("\n📂 Original File Content:\n", content)

    # Let user choose modification
    print("\nHow would you like to modify the content?")
    print("1 - Uppercase")
    print("2 - Lowercase")
    print("3 - Reverse text")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        modified_content = content.upper()
    elif choice == "2":
        modified_content = content.lower()
    elif choice == "3":
        modified_content = content[::-1]
    else:
        print("Invalid choice. Keeping content unchanged.")
        modified_content = content

    print("\n✏️ Modified Content Preview:\n", modified_content[:200], "...\n")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: Permission denied when trying to open the file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")

# Step 4: Save modified content into a new file
filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as infile:
        content = infile.read()
        print("\n📂 Original File Content:\n", content)

    # Modification choice
    print("\nHow would you like to modify the content?")
    print("1 - Uppercase")
    print("2 - Lowercase")
    print("3 - Reverse text")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        modified_content = content.upper()
    elif choice == "2":
        modified_content = content.lower()
    elif choice == "3":
        modified_content = content[::-1]
    else:
        print("Invalid choice. Keeping content unchanged.")
        modified_content = content

    # Save into a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"\n✅ Modified content written to {new_filename}")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: Permission denied when trying to open the file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")



