import logging
import os

import wget

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_data():
    logger.info("Downloading dataset...")
    urls = [
        "https://raw.githubusercontent.com/neubig/nn4nlp-code/master/data/classes/dev.txt",  # noqa
        "https://raw.githubusercontent.com/neubig/nn4nlp-code/master/data/classes/test.txt",  # noqa
        "https://raw.githubusercontent.com/neubig/nn4nlp-code/master/data/classes/train.txt",  # noqa
    ]

    outpath = os.getenv("DATASET_OUTPATH")
    os.makedirs(outpath, exist_ok=True)

    for url in urls:
        wget.download(url, out=outpath)


if __name__ == "__main__":
    download_data()
