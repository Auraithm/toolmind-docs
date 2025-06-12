# Functions

本章节详细介绍toolmind的功能以及用法。

## datasets

### 下载数据集
```python
from toolmind.datasets import download_dataset

# 下载 AIME-2024 数据集
download_dataset("AIME-2024", download_dir="./data")

# 使用镜像加速
download_dataset("AIME-2024", download_dir="./data", use_hf_mirror=True)
```

### 添加数据集
修改 toolmind/datasets/dataset_name.yaml进行手动添加。

### 加载数据集
```python
from toolmind.datasets import load_dataset

# 加载本地数据集
dataset = load_dataset("./data/GSM8K")
```

### 处理数据集
```python
from toolmind.datasets. import load_dataset, apply_func

# 加载本地数据集
dataset = load_dataset("./data/GSM8K")
dataset = apply_func(dataset)
print(dataset)
```

