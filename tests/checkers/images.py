import os

MAX_IMAGE_SIZE = {  # bytes
    '.png': 505000,
    '.gif': 2100000,
}

def log_error(file, line, msg, checker_name):
    """Log an error in the sphinx-lint log format to ease runbot processing of linting errors."""
    print(f"{file}:{line or 0}: {msg} ({checker_name})")

def check_image_compression(file_path):
    img_extension = ''
    for ext in MAX_IMAGE_SIZE:
        if file_path.endswith(ext):
            img_extension = ext
            break
    if img_extension:
        file_size = os.stat(file_path).st_size
        max_allowed_size = MAX_IMAGE_SIZE[img_extension]
        if file_size > max_allowed_size:
            log_error(
                file_path,
                0,
                f"file size is greater than {max_allowed_size/1000000}MB, you probably forgot to"
                " compress it.",
                "img-compression"
            )
