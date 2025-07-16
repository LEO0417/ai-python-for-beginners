# Lesson 10: Functions - Actions on Data
# 第10课：函数 - 对数据的操作

## 项目简介 / Project Overview

本项目是AI Python初学者课程的第10课，重点介绍Python中的函数概念以及如何在AI程序中使用函数。

This project is Lesson 10 of the AI Python for Beginners course, focusing on the concept of functions in Python and how to use functions in AI programs.

## 学习目标 / Learning Objectives

- 理解Python中内置函数的使用方法 / Understand how to use built-in functions in Python
- 学习如何将函数结果保存到变量中 / Learn how to save function results to variables  
- 掌握在AI程序中结合使用函数和变量 / Master combining functions and variables in AI programs
- 练习使用LLM相关函数进行交互 / Practice using LLM-related functions for interaction

## 文件结构 / File Structure

```
C1L10/
├── C1L10_Bilingual.ipynb    # 双语版本的Jupyter notebook / Bilingual Jupyter notebook
├── helper_functions.py      # 辅助函数文件 / Helper functions file
├── requirements.txt         # 项目依赖 / Project dependencies
└── README.md               # 项目说明 / Project documentation
```

## 环境配置 / Environment Setup

### 虚拟环境 / Virtual Environment
本项目配置为使用base虚拟环境。请确保你的Jupyter notebook运行在base环境中。

This project is configured to use the base virtual environment. Please ensure your Jupyter notebook runs in the base environment.

### LLM后端配置 / LLM Backend Configuration
本项目使用ollama作为LLM后端，默认模型为gemma2:latest。

This project uses ollama as the LLM backend with gemma2:latest as the default model.

#### 安装ollama / Install ollama
1. 访问 https://ollama.ai 下载并安装ollama
2. 运行命令：`ollama pull gemma2:latest`
3. 启动ollama服务

#### 备用方案 / Fallback Option
如果ollama不可用，helper_functions.py中包含了备用响应机制，会提供模拟的LLM响应。

If ollama is unavailable, helper_functions.py includes a fallback response mechanism that provides simulated LLM responses.

## 使用方法 / Usage

1. 确保已安装所需依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 启动Jupyter notebook：
   ```bash
   jupyter notebook C1L10_Bilingual.ipynb
   ```

3. 按顺序执行notebook中的单元格

## 主要功能 / Key Features

### 内置函数示例 / Built-in Function Examples
- `len()` - 计算字符串长度 / Calculate string length
- `round()` - 数字四舍五入 / Round numbers
- `type()` - 获取数据类型 / Get data type
- `print()` - 输出显示 / Display output

### LLM交互函数 / LLM Interaction Functions
- `print_llm_response()` - 打印LLM响应 / Print LLM response
- `get_llm_response()` - 获取LLM响应字符串 / Get LLM response string

### 练习内容 / Practice Exercises
- 变量操作和函数调用 / Variable operations and function calls
- LLM提示词构建 / LLM prompt construction
- 函数结果的存储和使用 / Storing and using function results

## 注意事项 / Notes

- 所有markdown内容都提供了中英双语版本 / All markdown content is provided in both Chinese and English
- 代码注释已翻译为中文 / Code comments have been translated to Chinese
- 练习题包含中文说明 / Exercises include Chinese instructions
- 确保ollama服务正常运行以获得最佳体验 / Ensure ollama service is running for the best experience

## 技术支持 / Technical Support

如果遇到问题，请检查：
- ollama是否正确安装和运行
- Python环境是否配置正确
- 所有依赖包是否已安装

If you encounter issues, please check:
- Whether ollama is properly installed and running
- Whether the Python environment is configured correctly  
- Whether all dependency packages are installed