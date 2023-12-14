import os
import zstandard

def decompress_zstd_file(input_file, output_file):
    with open(input_file, 'rb') as compressed_file, open(output_file, 'wb') as decompressed_file:
        decompressor = zstandard.ZstdDecompressor()
        decompressed_data = decompressor.decompressobj().decompress(compressed_file.read())
        decompressed_file.write(decompressed_data)

def process_new_files(directory, processed_files):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if file_path not in processed_files and filename.endswith('.zst'):
            decompressed_filename = filename[:-4]  # Remove '.zst' extension
            decompressed_path = os.path.join(directory, decompressed_filename)
            decompress_zstd_file(file_path, decompressed_path)
            processed_files.append(file_path)

def main():
    directory_path = '/path/to/your/files'
    processed_files = []  # Keep track of processed files
    process_new_files(directory_path, processed_files)

if __name__ == "__main__":
    main()
