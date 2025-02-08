import subprocess
import sys

package = [
    "--upgrade pip", # Upgrade pip
    "numpy", # Scientific Computing
    "pandas", # Data Manipulation
    "matplotlib", # Data Visualization
    "opencv-python",  # Computer Vision
    "scipy", # Scientific Computing
    "scikit-learn", # Machine Learning
    "tensorflow[and-cuda]",  # ML & Deep Learning
    "torch", "torchvision", "torchaudio",  # PyTorch ecosystem
    "transformers",  # Hugging Face models
    "datasets",  # Hugging Face datasets for NLP & ML
    "sentencepiece",  # Tokenization for LLMs
    "accelerate",  # Optimize training on multiple GPUs/TPUs
    "bitsandbytes",  # Efficient LLM quantization
    "optimum",  # Hardware acceleration for Hugging Face models
    "langchain",  # Framework for LLM-based applications
    "tiktoken",  # Efficient tokenization (used in OpenAI models)
    "openai",  # OpenAI API wrapper
    "xformers",  # Optimization for training LLMs
    "peft",  # Parameter-efficient fine-tuning
    "vllm",  # Vision & Language models
    "google-genail",  # Google AI models
]

platform = {
    "darwin": "Mac",
    "linux": "Linux",
    "win32": "Windows",
    "cygwin": "Windows/Cygwin",
    "aix": "AIX"
}

print(f"Detected OS: {platform.get(sys.platform, 'Unknown')}")

for i in package:
    if sys.platform in ["darwin", "linux"]:
        subprocess.call(f"pip3 install {i}", shell=True)
    else:
        subprocess.call(f"pip install {i}", shell=True)
print("All packages installed successfully!")