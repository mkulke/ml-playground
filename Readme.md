# ML Playground

## Requirements

### Packages

```
virtualenv -p python2.7 jupyter
cd jupyter
. jupyter/bin/activate
pip install jupyter numpy scipy matplotlib
```

### Vim Extension

```
mkdir -p $(jupyter --data-dir)/nbextensions
cd $(jupyter --data-dir)/nbextensions
git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding
```

### Prepare MNIST data

```
MNIST_URL=http://yann.lecun.com/exdb/mnist
# MNIST_URL=http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz # harder drop in replacement from zalando: https://github.com/zalandoresearch/fashion-mnist
wget ${MNIST_URL}/train-images-idx3-ubyte.gz
wget ${MNIST_URL}/train-labels-idx1-ubyte.gz
wget ${MNIST_URL}/t10k-images-idx3-ubyte.gz
wget ${MNIST_URL}/t10k-labels-idx1-ubyte.gz
gunzip train-images-idx3-ubyte.gz
gunzip train-labels-idx1-ubyte.gz
gunzip t10k-images-idx3-ubyte.gz
gunzip t10k-labels-idx1-ubyte.gz
./convert_idx_to_csv.py train-images-idx3-ubyte train-labels-idx1-ubyte 60000 > train.csv
./convert_idx_to_csv.py t10k-labels-idx1-ubyte t10k-images-idx3-ubyte 10000 > test.csv
```

## Start Notebook

```
jupyter notebook
```
