# Lesson 6: Turning code blocks into reusable functions
# 第6课：将代码块转换为可重用的函数

## 项目简介 / Project Overview

本项目是AI Python初学者课程的第6课，重点介绍如何创建自定义函数，以及如何使用函数避免重复编写相同的代码。

This project is Lesson 6 of the AI Python for Beginners course, focusing on how to create custom functions and how to use functions to avoid writing the same code repeatedly.

## 学习目标 / Learning Objectives

- 理解函数的概念和重要性 / Understand the concept and importance of functions
- 学习如何定义自己的函数 / Learn how to define your own functions
- 掌握函数参数的使用 / Master the use of function parameters
- 理解函数返回值的概念 / Understand the concept of function return values
- 练习创建实用的函数来处理文件和数据 / Practice creating practical functions for handling files and data

## 文件结构 / File Structure

```
C3L6/
├── C3L6_Bilingual.ipynb    # 双语版本的Jupyter notebook / Bilingual Jupyter notebook
├── requirements.txt         # 项目依赖 / Project dependencies
├── README.md               # 项目说明 / Project documentation
├── cape_town.txt           # 开普敦美食日记 / Cape Town food journal
├── paris.txt               # 巴黎美食日记 / Paris food journal
├── sydney.txt              # 悉尼美食日记 / Sydney food journal
├── tokyo.txt               # 东京美食日记 / Tokyo food journal
└── istanbul.txt            # 伊斯坦布尔美食日记 / Istanbul food journal

注意：辅助函数现在位于项目根目录的 helper_functions/ 包中
Note: Helper functions are now located in the helper_functions/ package at project root
```

## 环境配置 / Environment Setup

### 虚拟环境 / Virtual Environment
本项目配置为使用base虚拟环境。请确保你的Jupyter notebook运行在base环境中。

This project is configured to use the base virtual environment. Please ensure your Jupyter notebook runs in the base environment.

### LLM后端配置 / LLM Backend Configuration
本项目使用ollama作为LLM后端，默认模型为gemma3n:latest。

This project uses ollama as the LLM backend with gemma3n:latest as the default model.

#### 安装ollama / Install ollama
1. 访问 https://ollama.ai 下载并安装ollama
2. 运行命令：`ollama pull gemma3n:latest`
3. 启动ollama服务

#### 智能模型配置 / Smart Model Configuration

本课程使用智能模型选择机制，按以下优先级自动选择模型：

This lesson uses smart model selection with the following priority order:

1. **环境变量** / **Environment Variable** (最高优先级 / Highest Priority)
2. **配置文件** / **Configuration File**  
3. **自动检测** / **Auto Detection** (检测第一个可用模型 / Detect first available model)
4. **默认回退** / **Default Fallback** (`gemma3n:latest`)

**方法1：环境变量配置** / **Method 1: Environment Variable** (推荐 / Recommended)
```bash
# 设置环境变量 / Set environment variable
export OLLAMA_MODEL="llama2:latest"
jupyter notebook C3L6_Bilingual.ipynb

# 或者临时设置 / Or set temporarily
OLLAMA_MODEL="codellama:latest" jupyter notebook C3L6_Bilingual.ipynb
```

**方法2：配置文件** / **Method 2: Configuration File**
```python
# 在notebook中运行以下代码 / Run the following code in notebook
from helper_functions import set_default_model

# 设置默认模型 / Set default model
set_default_model("llama2:latest")

# 推荐的模型选择 / Recommended model options:
# set_default_model("llama2:latest")        # 通用对话模型 / General chat model
# set_default_model("codellama:latest")     # 代码专用模型 / Code-specific model  
# set_default_model("mistral:latest")       # 轻量级模型 / Lightweight model
# set_default_model("qwen:latest")          # 中文优化模型 / Chinese-optimized model
```

**检查当前使用的模型** / **Check Current Model**:
```python
from helper_functions import get_default_model
print(f"当前使用的模型 / Current model: {get_default_model()}")
```

**显示详细配置信息** / **Show Detailed Configuration Info**:
```python
from helper_functions.model_config import show_model_info
show_model_info()
```

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
   jupyter notebook C3L6_Bilingual.ipynb
   ```

3. 按顺序执行notebook中的单元格

## 主要功能 / Key Features

### 函数概念学习 / Function Concept Learning
- 回顾已使用的内置函数 / Review built-in functions already used
- 学习定义自定义函数 / Learn to define custom functions
- 理解函数参数和返回值 / Understand function parameters and return values

### 实践示例 / Practical Examples
- 文件读取函数 / File reading functions
- 温度转换函数 / Temperature conversion functions
- 单位转换函数 / Unit conversion functions
- LLM集成函数 / LLM integration functions

### 数据文件 / Data Files
项目包含5个城市的美食日记文件，用于函数练习：
- 开普敦 (Cape Town)
- 巴黎 (Paris)  
- 悉尼 (Sydney)
- 东京 (Tokyo)
- 伊斯坦布尔 (Istanbul)

The project includes food journal files from 5 cities for function practice:
- Cape Town
- Paris
- Sydney
- Tokyo
- Istanbul

### 练习内容 / Practice Exercises
- 创建摄氏度转华氏度函数 / Create Celsius to Fahrenheit function
- 创建米转英尺函数 / Create meters to feet function
- 挑战：创建LLM摘要函数 / Challenge: Create LLM summary function

## 技术特点 / Technical Features

- **函数重用性** / **Function Reusability**: 学习如何避免重复代码
- **参数传递** / **Parameter Passing**: 掌握向函数传递数据的方法
- **返回值处理** / **Return Value Handling**: 理解如何从函数获取结果
- **文件操作** / **File Operations**: 学习读取和处理文本文件
- **LLM集成** / **LLM Integration**: 将AI功能集成到自定义函数中

## 注意事项 / Notes

- 所有markdown内容都提供了中英双语版本 / All markdown content is provided in both Chinese and English
- 代码注释已翻译为中文 / Code comments have been translated to Chinese
- 练习题包含中文说明和提示 / Exercises include Chinese instructions and hints
- 数据文件包含丰富的美食文化内容 / Data files contain rich food culture content
- 确保ollama服务正常运行以获得最佳LLM体验 / Ensure ollama service is running for the best LLM experience

## 学习路径 / Learning Path

1. **基础概念** / **Basic Concepts**: 理解什么是函数以及为什么需要函数
2. **函数定义** / **Function Definition**: 学习如何定义和调用函数
3. **参数使用** / **Parameter Usage**: 掌握函数参数的传递和使用
4. **返回值** / **Return Values**: 理解如何从函数返回数据
5. **实际应用** / **Practical Application**: 通过练习巩固所学知识

## 技术支持 / Technical Support

如果遇到问题，请检查：
- ollama是否正确安装和运行
- Python环境是否配置正确
- 所有依赖包是否已安装
- 数据文件是否存在于正确位置

If you encounter issues, please check:
- Whether ollama is properly installed and running
- Whether the Python environment is configured correctly
- Whether all dependency packages are installed
- Whether data files exist in the correct location