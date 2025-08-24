# Week 4 Python Assignment: File Handling + Error Handling

filename = input("Enter the filename to read: ")

try:
    # Open and read the file
    with open(filename, "r") as infile:
        content = infile.read()
        print("\n📂 Original File Content:\n", content)

    # Ask how to modify content
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

    # Save modified content into a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"\n✅ Modified content written to {new_filename}")
    print("\n🎉 Program completed successfully! Thanks for using Flower Facts File Modifier 🌸")

except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: Permission denied when trying to open the file.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
