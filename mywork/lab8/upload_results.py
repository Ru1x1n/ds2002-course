import os
import sys
import glob
import boto3


def parse_args():
    if len(sys.argv) != 3:
        sys.exit(1)
    return sys.argv[1], sys.argv[2]


def upload(input_folder, destination):
    s3 = boto3.client("s3", region_name="us-east-1")

    bucket, prefix = destination.split("/", 1)

    files = glob.glob(os.path.join(input_folder, "results-*.csv"))

    for file_path in files:
        filename = os.path.basename(file_path)
        s3.upload_file(file_path, bucket, prefix + filename)
        print(f"Uploaded {filename}")


def main():
    input_folder, destination = parse_args()
    upload(input_folder, destination)


if __name__ == "__main__":
    main()