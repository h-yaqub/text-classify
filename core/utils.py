import logging

import torch

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Utils:
    # Read data
    def read_data(self, filename):
        data = []

        with open(filename, "r") as f:
            for _line in f:
                line = _line.lower().strip()
                line = line.split(" ||| ")
                data.append(line)

        return data

    # Create dictionaries
    def create_dict(self, data, word_to_index, tag_to_index, check_unk=False):
        for _line in data:
            for word in _line[1].split(" "):
                if not check_unk:
                    if word not in word_to_index:
                        word_to_index[word] = len(word_to_index)
                else:
                    if word not in word_to_index:
                        word_to_index[word] = word_to_index["<unk>"]

            if _line[0] not in tag_to_index:
                tag_to_index[_line[0]] = len(tag_to_index)

    # Create tensors
    def create_tensor(self, data, word_to_index, tag_to_index):
        for _line in data:
            yield (
                [word_to_index[word] for word in _line[1].split(" ")],
                tag_to_index[_line[0]],
            )

    # Training function
    def train_model(self, model, criterion, optimizer, train_data, device, epochs=10):
        model.train()
        for epoch in range(epochs):
            total_loss = 0
            for words, label in train_data:
                words = torch.tensor(words).to(device)
                label = torch.tensor([label]).to(device)

                optimizer.zero_grad()
                output = model(words)
                loss = criterion(output, label)
                loss.backward()

                optimizer.step()
                total_loss += loss.item()

            logger.info(f"Epoch {epoch + 1}, Loss: {total_loss / len(train_data):.4f}")

    # Inference function
    def perform_inference(self, model, sentence, word_to_index, tag_to_index, device):
        """
        Perform inference on the trained BoW model.

        Args:
            model (torch.nn.Module): The trained BoW model.
            sentence (str): The input sentence for inference.
            word_to_index (dict): A dictionary mapping words to their indices.
            tag_to_index (dict): A dictionary mapping tags to their indices.
            device (str): "cuda" or "cpu" based on availability.

        Returns:
            str: The predicted class/tag for the input sentence.
        """

        sentence_tensor = torch.tensor(
            [
                word_to_index.get(word, word_to_index["<unk>"])
                for word in sentence.split()
            ]
        ).to(device)
        model.eval()

        with torch.no_grad():
            output = model(sentence_tensor)

        predicted_class = torch.argmax(output).item()
        for tag, index in tag_to_index.items():
            if index == predicted_class:
                return tag

        return "Tag not found"
