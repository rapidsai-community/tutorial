#!/usr/bin/env python3

import os
import urllib.request
import gzip
import zipfile
import shutil
import argparse


def create_data_directory():
    """Create data directory if it doesn't exist"""
    if not os.path.exists("data"):
        print("Creating data directory...")
        os.makedirs("data")


def download_file(url, filename, description):
    """Download a file if it doesn't exist"""
    filepath = os.path.join("data", filename)
    if not os.path.exists(filepath):
        print(f"Downloading {description}...")
        urllib.request.urlretrieve(url, filepath)
    else:
        print(f"{filename} already exists, skipping download")


def process_cover_type_dataset():
    """Download and process cover type dataset"""
    filepath = os.path.join("data", "cover_forest_type.csv")
    if not os.path.exists(filepath):
        print("Downloading and processing cover type dataset...")
        gz_file = os.path.join("data", "covtype.data.gz")
        urllib.request.urlretrieve(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/covtype/covtype.data.gz",
            gz_file,
        )
        with gzip.open(gz_file, "rb") as f_in:
            with open(filepath, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(gz_file)
    else:
        print("cover_forest_type.csv already exists, skipping download")


def process_har_dataset():
    """Download and process UCI HAR Dataset"""
    har_dir = os.path.join("data", "UCI_HAR_Dataset")
    if not os.path.exists(har_dir):
        print("Downloading and processing UCI HAR Dataset...")
        zip_path = os.path.join("data", "HAR_data.zip")
        urllib.request.urlretrieve(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/00240/UCI%20HAR%20Dataset.zip",
            zip_path,
        )
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall("data")
        os.rename(os.path.join("data", "UCI HAR Dataset"), har_dir)
        if os.path.exists(os.path.join("data", "__MACOSX")):
            shutil.rmtree(os.path.join("data", "__MACOSX"))
        os.remove(zip_path)
    else:
        print("UCI_HAR_Dataset directory already exists, skipping download")


def main():
    parser = argparse.ArgumentParser(description="Download datasets for RAPIDS tutorial")
    parser.add_argument("--all", action="store_true", help="Download all datasets")
    parser.add_argument(
        "--pydata-vt", action="store_true", help="Download all datasets except 'transactions'"
    )
    parser.add_argument(
        "--pageviews", action="store_true", help="Download pageviews dataset"
    )
    parser.add_argument(
        "--nyc-parking",
        action="store_true",
        help="Download NYC parking violations dataset",
    )
    parser.add_argument(
        "--transactions", action="store_true", help="Download transactions dataset"
    )
    parser.add_argument(
        "--cover-type",
        action="store_true",
        help="Download and process cover type dataset",
    )
    parser.add_argument(
        "--har", action="store_true", help="Download and process HAR dataset"
    )

    args = parser.parse_args()

    # If no specific flags are provided, show help and exit
    if not any(vars(args).values()):
        parser.print_help()
        return

    print("Checking and downloading datasets...")
    create_data_directory()

    if args.all or args.pydata_vt or args.pageviews:
        download_file(
            "https://raw.githubusercontent.com/NVIDIA/accelerated-computing-hub/refs/heads/main/gpu-python-tutorial/data/pageviews_small.csv",
            "pageviews_small.csv",
            "pageviews_small.csv",
        )

    if args.all or args.pydata_vt or args.nyc_parking:
        download_file(
            "https://data.rapids.ai/datasets/nyc_parking/nyc_parking_violations_2022.parquet",
            "nyc_parking_violations_2022.parquet",
            "NYC parking violations dataset",
        )

    if args.all or args.transactions:
        download_file(
            "https://storage.googleapis.com/rapidsai/polars-demo/transactions-t4-20.parquet",
            "transactions.parquet",
            "transactions.parquet"
        )

    if args.all or args.pydata_vt or args.cover_type:
        process_cover_type_dataset()

    if args.all or args.pydata_vt or args.har:
        process_har_dataset()

    print("Download complete!")

if __name__ == "__main__":
    main() 