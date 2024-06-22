import torch
import torch.nn as nn


# Neural network model
class BoW(nn.Module):
    def __init__(self, vocab_size, embed_size, output_size):
        super(BoW, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.fc = nn.Linear(embed_size, output_size)
        nn.init.xavier_uniform_(self.fc.weight)

        self.type = (
            torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor
        )
        self.bias = nn.Parameter(torch.zeros(output_size))

    def forward(self, x):
        embeds = self.embedding(x)
        embeds = torch.mean(embeds, dim=0, keepdim=True)
        output = self.fc(embeds) + self.bias
        return output
