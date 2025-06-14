import os
filename = "input_file"
def expand_file_by_gb(filename, gigabytes):
    chunk_size = 1024 * 1024  
    total_chunks = gigabytes * 1024  
    written = 0

    if not os.path.isfile(filename):
        print(f"File '{filename}' not found.")
        return

    print(f"Starting to add {gigabytes} GB to '{filename}'...")

    try:
        with open(filename, 'ab') as f:
            for i in range(total_chunks):
                f.write(b'\0' * chunk_size)
                written += 1
                if (written % 100) == 0:
                    print(f"{written} MB written...")

        print(f" Successfully added {gigabytes} GB to '{filename}'.")
        final_size = os.path.getsize(filename) / (1024 * 1024 * 1024)
        print(f" New file size: {final_size:.2f} GB")

    except Exception as e:
        print(f"Error while writing: {e}")


expand_file_by_gb('output_file', 10)  