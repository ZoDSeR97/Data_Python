from NeuralNetwork.LLMs.Scratch import Transformer
from torch.utils.data import DataLoader
from datasets import load_dataset

# Load dataset
dataset = load_dataset("wikitext", "wikitext-2-raw-v1")

# Tokenize dataset
tokenizer = ...  # Use a tokenizer of your choice
tokenized_dataset = dataset.map(lambda x: tokenizer(x["text"]), batched=True)

# Create DataLoader
train_loader = DataLoader(
    tokenized_dataset["train"], batch_size=32, shuffle=True)

# Initialize model, optimizer, and loss function
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Transformer(src_vocab_size=tokenizer.vocab_size, embed_size=512, num_layers=6,
                    heads=8, device=device, forward_expansion=4, dropout=0.1, max_length=512).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
criterion = nn.CrossEntropyLoss()

# Training loop
for epoch in range(10):
    for batch in train_loader:
        inputs = batch["input_ids"].to(device)
        targets = batch["input_ids"].to(device)

        outputs = model(inputs, mask=None)
        loss = criterion(
            outputs.view(-1, tokenizer.vocab_size), targets.view(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item()}")