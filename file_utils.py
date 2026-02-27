import os
import shutil

BASE_DIR = os.path.abspath("workspace")
ALLOWED_EXTENSIONS = [".txt", ".md", ".json", ".py"]

def safe_path(path):
    full_path = os.path.abspath(os.path.join(BASE_DIR, path))

    if not full_path.startswith(BASE_DIR):
        raise ValueError("Unsafe path detected")

    if not any(full_path.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise ValueError("File type not allowed")

    return full_path


def read_file(path):
    path = safe_path(path)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    path = safe_path(path)

    if os.path.exists(path):
        shutil.copy(path, path + ".bak")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return "File written successfully."


def append_file(path, content):
    path = safe_path(path)

    with open(path, "a", encoding="utf-8") as f:
        f.write(content)

    return "Content appended successfully."

def save_uploaded_file(uploaded_file):
    if uploaded_file is None:
        return None

    filename = os.path.basename(uploaded_file.name)

    if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise ValueError("File type not allowed")

    if uploaded_file.size > 2 * 1024 * 1024:
        raise ValueError("File too large (max 2MB)")

    save_path = os.path.join(BASE_DIR, filename)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return filename