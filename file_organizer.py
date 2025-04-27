import os

# Directory Path
desktop_path = os.path.expanduser("~/Desktop")

main_dir = os.path.join(desktop_path, "MyFiles")

# Print the current directory
print("Working directory:", os.getcwd())

if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print(f"Directory '{main_dir}' created.")
else:
    print(f"Directory '{main_dir}' already exists.")

# List of subdirectory names
subdirs = ["Docs", "Images", "Videos"]

# Create subdirectory inside 'MyFiles'
for subdir in subdirs:
    path = os.path.join(main_dir, subdir)
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Subdirectory '{subdir}' created in '{main_dir}'.")
    else:
        print(f"Subdirectory '{subdir}' already exists in '{main_dir}'.")
