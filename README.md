# Data_Python
Learn Data Handling and ML models with Python

## ✅ Requirement
[Python](https://www.python.org/) to be installed.
```bash
cd /Data_Python
pip install 'tensorflow[and-cuda]'
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt --upgrade
```

## ⁉️ Note ⁉️
Having latest version of python (at the earliest) will break installation of ML libraries such as Tensorflow, Torch, Theano, etc.
  - This is common issue for almost a decade, as for some reason, utilizing backward compatibility feature does not cross these distributor mind
  - Solution is to wait for these distributors update
  - Once these distributors update then new Python version is almost available then new Python version is almost available
  - You can also downgrade your python version, aka downgrade performance and QoL

ML model does not have same weight or (sometime) not produce same output
  - ML models relies on implementation (70%) and hardware optimization (30%)
  - Depending on implementation, each training will generate/manipulate weight differently and these weights play major factor to the outcome

ML model has high accuracy but produce inaccurate result in practical test
  - The model probably is trained on the test set
  - Make sure test set is fresh and training set is well shuffle
