# Usage

这个文档将指导您如何使用 toolmind 库。

(installation)=
## Installation

安装 toolmind 有多种方式：

### 使用 pip 安装

推荐使用 pip 进行安装：

```console
(.venv) $ pip install toolmind
```

### 从源码安装

如果您想使用最新的开发版本：

```console
(.venv) $ git clone https://github.com/yourname/toolmind.git
(.venv) $ cd toolmind
(.venv) $ pip install -e .
```

### 验证安装

安装完成后，验证是否成功：

```python
import toolmind
print(toolmind.__version__)
```

## 快速开始

### 基本用法

开始使用 toolmind 的基本示例：

```python
import toolmind

# 创建一个简单的实例
tool = toolmind.Tool()
result = tool.process()
print(result)
```

### 高级配置

对于更复杂的使用场景：

```python
import toolmind

# 高级配置
config = {
    'mode': 'advanced',
    'debug': True
}

tool = toolmind.Tool(config=config)
result = tool.advanced_process()
```

## API 参考

### 核心类

主要的类和方法说明：

#### Tool 类

`Tool` 是主要的工具类：

```python
class Tool:
    def __init__(self, config=None):
        """初始化工具"""
        pass
    
    def process(self):
        """基本处理方法"""
        pass
```

#### 配置选项

支持的配置参数：

- `mode`: 运行模式 (`'basic'` 或 `'advanced'`)
- `debug`: 是否开启调试模式
- `timeout`: 超时设置（秒）

## Creating recipes

To retrieve a list of random ingredients,
you can use the `lumache.get_random_ingredients()` function:

The `kind` parameter should be either `"meat"`, `"fish"`,
or `"veggies"`. Otherwise, `lumache.get_random_ingredients`
will raise an exception.

For example:

```python
>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
``` 