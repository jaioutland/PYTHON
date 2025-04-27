"""
Jai Outland
Github:
"""

import os

# Get the Desktop path (for macOS)
desktop_path = os.path.expanduser("~/Desktop")

# Define the full path to 'MyFiles' on Desktop
main_dir = os.path.join(desktop_path, "MyFiles")

# Print the current working directory
print("Working directory:", os.getcwd())

# Create main directory on Desktop if it doesn't exist
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    print(f"Directory '{main_dir}' created.")
else:
    print(f"Directory '{main_dir}' already exists.")

# List of subdirectory names
subdirs = ["Docs", "Images", "Videos"]

# Create each subdirectory inside 'MyFiles'
for subdir in subdirs:
    path = os.path.join(main_dir, subdir)
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Subdirectory '{subdir}' created in '{main_dir}'.")
    else:
        print(f"Subdirectory '{subdir}' already exists in '{main_dir}'.")
