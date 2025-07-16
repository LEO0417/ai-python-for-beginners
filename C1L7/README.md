# C1L7: Displaying text and calculations together
# C1L7: 将文本和计算结果一起显示

## Overview / 概述

This lesson teaches how to combine text and calculations in Python using f-strings (formatted strings). You'll learn to display computational results within readable text, format numbers, and work with multi-line strings.

本课程教授如何使用f-字符串（格式化字符串）在Python中结合文本和计算。你将学习在可读文本中显示计算结果、格式化数字以及使用多行字符串。

## Learning Objectives / 学习目标

- Understand how to use f-strings to combine text and calculations
- Learn to format numbers in f-strings (e.g., removing decimal places)
- Practice with multi-line f-strings
- Apply f-strings to real-world examples like temperature conversion

- 了解如何使用f-字符串结合文本和计算
- 学习在f-字符串中格式化数字（例如，去除小数位）
- 练习多行f-字符串
- 将f-字符串应用到现实世界的例子中，如温度转换

## Key Concepts / 关键概念

### F-strings / f-字符串
- Syntax: `f"text {expression} more text"`
- 语法：`f"文本 {表达式} 更多文本"`

### Number Formatting / 数字格式化
- `{value:.0f}` - Display without decimal places / 不显示小数位
- `{value:.1f}` - Display with one decimal place / 显示一位小数

### Multi-line Strings / 多行字符串
- Use triple quotes `"""` for multi-line f-strings
- 使用三重引号 `"""` 创建多行f-字符串

## Prerequisites / 前置条件

- Basic understanding of Python variables
- Knowledge of print() function
- Understanding of basic arithmetic operations

- 基本的Python变量理解
- 了解print()函数
- 理解基本算术运算

## Setup / 设置

1. Ensure you have Python 3.6+ installed (f-strings were introduced in Python 3.6)
2. Install Jupyter notebook if you haven't already:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the notebook:
   ```bash
   jupyter notebook C1L7_Bilingual.ipynb
   ```

1. 确保安装了Python 3.6+（f-字符串在Python 3.6中引入）
2. 如果还没有安装Jupyter notebook：
   ```bash
   pip install -r requirements.txt
   ```
3. 打开notebook：
   ```bash
   jupyter notebook C1L7_Bilingual.ipynb
   ```

## Practice Exercises / 练习题

The notebook includes several practice exercises:
1. Modify code to print your age
2. Fix broken f-string syntax
3. Complete incomplete f-string expressions
4. Format numbers with specific decimal places

notebook包含几个练习题：
1. 修改代码以打印你的年龄
2. 修复损坏的f-字符串语法
3. 完成不完整的f-字符串表达式
4. 用特定小数位格式化数字

## Next Steps / 下一步

After completing this lesson, you'll be ready to learn about variables and how to make your code more readable and reusable.

完成本课程后，你将准备学习变量以及如何使你的代码更可读和可重用。