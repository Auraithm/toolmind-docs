# MyST 语法示例

这是一个展示 MyST Markdown 语法的示例文件。

## 基本语法

### 文本格式

**粗体文字** 和 *斜体文字* 以及 `行内代码`

### 列表

- 无序列表项1
- 无序列表项2
  - 嵌套项目

1. 有序列表项1
2. 有序列表项2

(quick-start)=
## 快速开始

这个章节有一个锚点标签。

### 代码示例

```python
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

# 调用函数
message = greet("World")
print(message)
```

### 带高亮的代码

```{code-block} python
:linenos:
:emphasize-lines: 3,5

def calculate(x, y):
    """计算函数"""
    result = x + y    # 这行会高亮
    print(f"计算结果: {result}")
    return result     # 这行也会高亮
```

## 提示框示例

```{note}
这是一个普通提示框
```

```{warning}
这是一个警告提示框
```

```{tip}
这是一个小贴士提示框
```

## 交叉引用示例

- 链接到本页面的章节：{ref}`快速开始 <quick-start>`
- 链接到其他文档：{doc}`usage`
- 普通链接：[使用指南](usage.md)

## 数学公式

行内公式：爱因斯坦质能方程 {math}`E = mc^2`

独立公式：
```{math}
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
```

## 表格示例

```{list-table} 功能对比表
:header-rows: 1
:widths: 30 35 35

* - 功能
  - Markdown
  - MyST
* - 基本格式
  - ✅ 支持
  - ✅ 支持
* - 交叉引用
  - ❌ 不支持
  - ✅ 支持
* - 数学公式
  - ❌ 不支持
  - ✅ 支持
```

## 总结

MyST 在保持 Markdown 简洁性的同时，添加了强大的文档功能！ 