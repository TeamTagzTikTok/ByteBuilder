import sys
import time

def generate_txt_file(filename, size_in_mb, content="A"):
    size_in_bytes = int(size_in_mb * 1024 * 1024)
    written_bytes = 0
    bar_length = 50

    with open(filename, "w") as f:
        chunk = content * 1024  # 1KB per chunk
        chunk_size = len(chunk)
        total_chunks = size_in_bytes // chunk_size

        for i in range(total_chunks):
            f.write(chunk)
            written_bytes += chunk_size

            # update progress bar
            percent = int((written_bytes / size_in_bytes) * 100)
            filled = int(bar_length * (written_bytes / size_in_bytes))
            bar = "#" * filled + "-" * (bar_length - filled)
            sys.stdout.write(f"\rMAKING <{bar}> {percent}% - Size: {written_bytes // (1024 * 1024)}MB")
            sys.stdout.flush()

    print(f"\n{filename} created with size ~{size_in_mb}MB")


name = input("filename (with .txt): ")
try:
    size = float(input("size in MB: "))
    generate_txt_file(name, size)
except ValueError:
    print("Invalid number.")
