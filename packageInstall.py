import subprocess
import sys

package = [
    "--upgrade pip", 
    "opencv-python", 
    "numpy", 
    "matplotlib", 
    "scipy", 
    "scikit-learn", 
    "jupyter", 
    "pandas", 
    "theano", 
    "tensorflow", 
    "torch", 
    "torchvision", 
    "torchaudio",
    "virtualenv"
]

platform = {
    "darwin": "Mac", 
    "linux": "Linux", 
    "win32": "Window", 
    "cygwin": "Window/Cygwin", 
    "aix": "AIX"
}

print(platform[sys.platform])

for i in package:
    if sys.platform == "darwin" or sys.platform == "linux":
        subprocess.call("pip3 install " + i, shell=True)
    else:
        subprocess.call("pip install " + i, shell=True)
