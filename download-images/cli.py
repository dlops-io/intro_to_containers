"""Downloading the images from Firefox based on the search term specified

    This scripts scrapes Firefox and downloads Google images of different images

    Typical usage example from command line:
        python -m cli --nums 10 --search "oyster mushrooms" "crimini mushrooms" "amanita mushrooms" --opp "search"
"""

# built-in libraries
import os
import argparse

# third-party libraries
import tensorflow as tf

# function from downloader.py module
from downloader import download_google_images

dataset_path = "/persistent/dataset"


def main(nums, search, opp):
    # if a command option was "download", go and download the images
    if opp == "search":
        num_images_requested = nums
        search_term_list = search
        download_google_images(num_images_requested, search_term_list)
    # if a command option was NOT "download", verify the downloaded images can be read by Tensorflow
    elif opp == "verify":
        # Verify downloaded images
        label_names = os.listdir(basedataset_path_path)
        print("Labels:", label_names)

        # Generate a list of labels and path to images
        data_list = []
        for label in label_names:
            # Images
            image_files = os.listdir(os.path.join(dataset_path, label))
            data_list.extend(
                [(label, os.path.join(dataset_path, label, f)) for f in image_files])

        print("Full size of the dataset:", len(data_list))
        print(data_list[:5])

        for label, path in data_list:
            try:
                image = tf.io.read_file(path)
                image = tf.image.decode_jpeg(image, channels=3)
            except:
                print(
                    f'Path for file that could not be read as Tensorflow image: {path}')
                os.remove(path)


if __name__ == "__main__":

    # Generate the inputs arguments parser
    # if you type into the terminal 'python3 cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(
        description='obtaining or verifying images for Jordan sneakers downloaded from Google')
    # two different command options for inputting the three optional commands
    parser.add_argument("-o", "--opp", type=str, default="search",
                        help="whether or not to download the Google images")
    parser.add_argument("-n", "--nums", type=int, default=1,
                        help="number of images to download")
    parser.add_argument("-s", "--search", nargs="+", default="default",
                        help="the Google search term(s)since there can be multiple")

    args = parser.parse_args()
    main(args.nums, args.search, args.opp)
