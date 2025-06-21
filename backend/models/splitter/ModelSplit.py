import os

def split_file(input_file_path, output_dir, part_size_mb=15):
    part_size = part_size_mb * 1024 * 1024  # Convert MB to bytes
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file_path, 'rb') as infile:
        part_num = 1
        while True:
            chunk = infile.read(part_size)
            if not chunk:
                break
            part_filename = os.path.join(
                output_dir,
                f"{os.path.basename(input_file_path)}.part{part_num}"
            )
            with open(part_filename, 'wb') as outfile:
                outfile.write(chunk)
            part_num += 1
    print(f"Split {input_file_path} into {part_num - 1} parts in {output_dir}")

def join_files(input_dir, output_file_path):
    with open(output_file_path, 'wb') as outfile:
        part_num = 1
        while True:
            part_filename = os.path.join(
                input_dir,
                f"{os.path.basename(output_file_path)}.part{part_num}"
            )
            if not os.path.exists(part_filename):
                break
            with open(part_filename, 'rb') as infile:
                outfile.write(infile.read())
            part_num += 1
    
    print(f"Joined files into {output_file_path}")
    
# input_file = "../best.pt"
# output_dir = "../split_models/best"

# split_file(input_file, output_dir)


