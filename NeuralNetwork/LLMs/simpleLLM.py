import torch
import torch.nn as nn
import torch.nn.functional as F


class PositionalEncoding(nn.Module):
    """Implements positional encoding for sequence data"""

    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float(
        ) * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)


class SimpleLLM(nn.Module):
    """Basic transformer-based language model"""

    def __init__(self, vocab_size, d_model=256, nhead=4, num_layers=2, dropout=0.1):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model, nhead, dim_feedforward=2048, dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers)
        self.fc = nn.Linear(d_model, vocab_size)

    def forward(self, src):
        # Create mask to prevent attending to future positions
        mask = self.generate_square_subsequent_mask(src.size(0)).to(src.device)

        # Embedding and scaling
        embedded = self.embedding(src) * (self.embedding.embedding_dim ** 0.5)
        embedded = self.pos_encoder(embedded)

        # Transformer encoder
        output = self.transformer_encoder(embedded, mask)

        # Final linear layer
        return F.log_softmax(self.fc(output), dim=-1)

    def generate_square_subsequent_mask(self, sz):
        """Generate a mask to prevent attention to future positions"""
        mask = (torch.triu(torch.ones(sz, sz)) == 1).transpose(0, 1)
        mask = mask.float().masked_fill(mask == 0, float(
            '-inf')).masked_fill(mask == 1, float(0.0))
        return mask


# Example usage:
vocab_size = 10000  # Size of your vocabulary
model = SimpleLLM(vocab_size=vocab_size)

# Sample input (batch_size=1, sequence_length=5)
input_tensor = torch.LongTensor([[1, 2, 3, 4, 5]])
output = model(input_tensor)

print(output.shape)  # Should be [sequence_length, batch_size, vocab_size]