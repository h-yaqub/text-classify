import logging
import os

import torch
import torch.nn as nn
from models import BoW
from utils import Utils

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Main execution
if __name__ == "__main__":
    # Setup
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    WORDTOINDEX = {"<unk>": 0}
    TAGTOINDEX = {}

    TRAIN_DATA = Utils().read_data(os.getenv("TRAIN_DATA"))
    TEST_DATA = Utils().read_data(os.getenv("TEST_DATA"))

    Utils().create_dict(TRAIN_DATA, WORDTOINDEX, TAGTOINDEX)
    Utils().create_dict(TEST_DATA, WORDTOINDEX, TAGTOINDEX, check_unk=True)

    TRAIN_DATA = list(Utils().create_tensor(TRAIN_DATA, WORDTOINDEX, TAGTOINDEX))
    TEST_DATA = list(Utils().create_tensor(TEST_DATA, WORDTOINDEX, TAGTOINDEX))

    vocab_size = len(WORDTOINDEX)
    output_size = len(TAGTOINDEX)
    embed_size = 100

    model = BoW(vocab_size, embed_size, output_size).to(DEVICE)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    Utils().train_model(model, criterion, optimizer, TRAIN_DATA, DEVICE)

    # Example inference
    sample_sentence = "I love me"
    predicted_tag = Utils().perform_inference(
        model, sample_sentence, WORDTOINDEX, TAGTOINDEX, DEVICE
    )

    logger.info(f"Predicted Tag: {predicted_tag}")
