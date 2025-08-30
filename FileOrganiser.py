import os
import shutil

# File extensions
image_extension = (".jpg", ".jpeg", ".png", ".gif", ".webp")
video_extension = (".webm", ".mov", ".mp4", ".m4p", ".m4v")
document_extension = (".doc", ".docx", ".pdf", ".txt", ".key")
code_extension = (".py", ".java", ".html", ".css", ".js", ".sql", ".cpp", ".c")

# Automatically detect Downloads folder on Windows
ddir = os.path.join(os.path.expanduser("~"), "Downloads")

# Create subdirectories if they don't exist
subdirectories = ["images", "videos", "documents", "code", "other"]
for subdir in subdirectories:
    path = os.path.join(ddir, subdir)
    if not os.path.exists(path):
        os.makedirs(path)

# Helper functions (case-insensitive)
def get_image(file):
    return os.path.splitext(file)[1].lower() in image_extension

def get_video(file):
    return os.path.splitext(file)[1].lower() in video_extension

def get_document(file):
    return os.path.splitext(file)[1].lower() in document_extension

def get_code(file):
    return os.path.splitext(file)[1].lower() in code_extension

# Move files
for file in os.listdir(ddir):
    filepath = os.path.join(ddir, file)

    if os.path.isdir(filepath):
        continue  # skip folders

    # Decide destination folder
    if get_image(file):
        dest = os.path.join(ddir, "images", file)
    elif get_video(file):
        dest = os.path.join(ddir, "videos", file)
    elif get_document(file):
        dest = os.path.join(ddir, "documents", file)
    elif get_code(file):
        dest = os.path.join(ddir, "code", file)
    else:
        dest = os.path.join(ddir, "other", file)

    # If file with same name exists, rename to avoid error
    if os.path.exists(dest):
        base, ext = os.path.splitext(file)
        i = 1
        while os.path.exists(os.path.join(os.path.dirname(dest), f"{base}_{i}{ext}")):
            i += 1
        dest = os.path.join(os.path.dirname(dest), f"{base}_{i}{ext}")

    # Move the file
    shutil.move(filepath, dest)
    print(f"Moved: {file} -> {dest}")
