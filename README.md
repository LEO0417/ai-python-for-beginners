# AI Python for Beginners - Bilingual Course
# AI Python 初学者双语课程

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

## 项目简介 / Project Overview

这是一个面向初学者的AI Python双语教学项目，提供中英文对照的Jupyter notebook课程。每个课程都包含完整的项目结构、辅助函数和实践练习，帮助学习者逐步掌握Python编程和AI应用开发。

This is a bilingual AI Python tutorial project for beginners, providing Jupyter notebook courses with Chinese-English parallel content. Each lesson includes complete project structure, helper functions, and practical exercises to help learners gradually master Python programming and AI application development.

## 特色功能 / Key Features

- **双语教学** / **Bilingual Learning**: 中英文对照，适合中文学习者
- **实践导向** / **Practice-Oriented**: 每课都包含实际项目和练习
- **AI集成** / **AI Integration**: 集成ollama本地LLM，学习AI应用开发
- **完整项目结构** / **Complete Project Structure**: 每课都是独立的完整项目
- **渐进式学习** / **Progressive Learning**: 从基础到进阶，循序渐进

## 课程列表 / Course List

### 第一章 / Chapter 1
- **C1L6**: 基础Python语法和数据类型 / Basic Python syntax and data types
- **C1L7**: 控制流程和循环 / Control flow and loops  
- **C1L9**: 数据结构和文件操作 / Data structures and file operations
- **C1L10**: 错误处理和调试 / Error handling and debugging

### 第三章 / Chapter 3
- **C3L6**: 函数定义和重用 / Function definition and reuse

## 快速开始 / Quick Start

### 环境要求 / Prerequisites

- Python 3.8+
- Jupyter Notebook
- ollama (可选，用于AI功能 / Optional, for AI features)

### 安装步骤 / Installation

1. **克隆项目** / **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-python-bilingual-course
   ```

2. **安装依赖** / **Install dependencies**
   ```bash
   # 为每个课程安装依赖 / Install dependencies for each lesson
   cd C1L6 && pip install -r requirements.txt && cd ..
   cd C1L7 && pip install -r requirements.txt && cd ..
   cd C1L9 && pip install -r requirements.txt && cd ..
   cd C1L10 && pip install -r requirements.txt && cd ..
   cd C3L6 && pip install -r requirements.txt && cd ..
   ```

3. **配置ollama (可选)** / **Setup ollama (Optional)**
   ```bash
   # 安装ollama / Install ollama
   # 访问 https://ollama.ai 下载安装包
   
   # 拉取默认模型 / Pull default model
   ollama pull gemma3n:latest
   
   # 或者拉取其他模型 / Or pull other models
   # ollama pull llama2:latest
   # ollama pull codellama:latest
   
   # 启动服务 / Start service
   ollama serve
   ```
   
   **智能模型配置** / **Smart Model Configuration**:
   
   本项目使用智能模型选择机制，按以下优先级自动选择模型：
   
   This project uses smart model selection with the following priority order:
   
   1. **环境变量** / **Environment Variable** (最高优先级 / Highest Priority)
   2. **配置文件** / **Configuration File**
   3. **自动检测** / **Auto Detection** (检测第一个可用模型 / Detect first available model)
   4. **默认回退** / **Default Fallback** (`gemma3n:latest`)
   
   **方法1：环境变量配置** / **Method 1: Environment Variable** (推荐 / Recommended)
   ```bash
   # 设置环境变量 / Set environment variable
   export OLLAMA_MODEL="llama2:latest"
   jupyter notebook
   
   # 或者临时设置 / Or set temporarily
   OLLAMA_MODEL="codellama:latest" jupyter notebook
   ```
   
   **方法2：配置文件** / **Method 2: Configuration File**
   ```python
   # 在任意课程中运行以下代码 / Run the following code in any lesson
   from helper_functions import set_default_model
   
   # 设置默认模型 / Set default model
   set_default_model("llama2:latest")
   
   # 推荐的模型选择 / Recommended model options:
   # set_default_model("llama2:latest")        # 通用对话模型 / General chat model
   # set_default_model("codellama:latest")     # 代码专用模型 / Code-specific model  
   # set_default_model("mistral:latest")       # 轻量级模型 / Lightweight model
   # set_default_model("qwen:latest")          # 中文优化模型 / Chinese-optimized model
   ```
   
   **方法3：自动检测** / **Method 3: Auto Detection**
   
   如果没有设置环境变量或配置文件，系统会自动使用 `ollama list` 中的第一个可用模型。
   
   If no environment variable or config file is set, the system will automatically use the first available model from `ollama list`.
   
   **检查当前使用的模型** / **Check Current Model**:
   ```python
   from helper_functions import get_default_model
   print(f"当前使用的模型 / Current model: {get_default_model()}")
   ```

4. **测试配置 (可选)** / **Test Configuration (Optional)**
   ```bash
   # 运行配置测试脚本 / Run configuration test script
   python test_model_config.py
   ```

5. **启动学习** / **Start Learning**
   ```bash
   # 进入任意课程文件夹 / Enter any lesson folder
   cd C1L6
   
   # 启动Jupyter notebook / Start Jupyter notebook
   jupyter notebook C1L6_Bilingual.ipynb
   ```

## 项目结构 / Project Structure

```
ai-python-bilingual-course/
├── README.md                    # 项目主说明 / Main project documentation
├── LICENSE                      # 开源许可证 / Open source license
├── CONTRIBUTING.md             # 贡献指南 / Contribution guidelines
├── CODE_OF_CONDUCT.md          # 行为准则 / Code of conduct
├── helper_functions/            # 共享辅助函数包 / Shared helper functions package
│   ├── __init__.py             # 包初始化文件 / Package initialization
│   ├── llm_utils.py           # LLM相关功能 / LLM related functions
│   ├── model_config.py        # 模型配置管理 / Model configuration management
│   └── common_utils.py        # 通用工具函数 / Common utility functions
├── ollama_config.json.example  # 全局配置示例 / Global config example
├── test_model_config.py        # 配置测试脚本 / Configuration test script
├── .kiro/                      # Kiro AI助手配置 / Kiro AI assistant config
│   └── specs/                  # 项目规格文档 / Project specifications
├── C1L6/                       # 第1章第6课 / Chapter 1 Lesson 6
│   ├── C1L6_Bilingual.ipynb   # 双语notebook / Bilingual notebook
│   ├── requirements.txt        # 依赖文件 / Dependencies
│   └── README.md              # 课程说明 / Lesson documentation
├── C1L7/                       # 第1章第7课 / Chapter 1 Lesson 7
├── C1L9/                       # 第1章第9课 / Chapter 1 Lesson 9
├── C1L10/                      # 第1章第10课 / Chapter 1 Lesson 10
└── C3L6/                       # 第3章第6课 / Chapter 3 Lesson 6
    ├── C3L6_Bilingual.ipynb   # 双语notebook / Bilingual notebook
    ├── requirements.txt        # 依赖文件 / Dependencies
    ├── README.md              # 课程说明 / Lesson documentation
    ├── cape_town.txt          # 示例数据文件 / Sample data files
    ├── paris.txt
    ├── sydney.txt
    ├── tokyo.txt
    └── istanbul.txt
```

## 学习路径 / Learning Path

### 建议学习顺序 / Recommended Learning Order

1. **C1L6**: Python基础语法 / Python basic syntax
2. **C1L7**: 控制结构 / Control structures  
3. **C1L9**: 数据处理 / Data processing
4. **C1L10**: 错误处理 / Error handling
5. **C3L6**: 函数编程 / Function programming

### 学习建议 / Learning Tips

- 每课都包含理论讲解和实践练习 / Each lesson includes theory and practice
- 建议按顺序学习，每课都有前置知识要求 / Follow the sequence as each lesson builds on previous ones
- 充分利用双语对照，加深理解 / Make full use of bilingual content for better understanding
- 动手实践所有代码示例 / Practice all code examples hands-on
- 完成每课的练习题 / Complete exercises in each lesson

## 技术栈 / Tech Stack

- **Python 3.8+**: 主要编程语言 / Main programming language
- **Jupyter Notebook**: 交互式学习环境 / Interactive learning environment
- **ollama**: 本地LLM后端 / Local LLM backend
- **gemma3n**: 默认AI模型 / Default AI model

## 贡献 / Contributing

我们欢迎各种形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

We welcome contributions of all kinds! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### 贡献方式 / Ways to Contribute

- 报告问题 / Report bugs
- 提出功能建议 / Suggest features
- 改进文档 / Improve documentation
- 添加新课程 / Add new lessons
- 优化翻译 / Improve translations

## 许可证 / License

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 支持 / Support

如果你在使用过程中遇到问题，可以通过以下方式获取帮助：

If you encounter any issues, you can get help through:

- 提交 Issue / Submit an Issue
- 查看课程README / Check lesson README files
- 参考技术文档 / Refer to technical documentation

## 致谢 / Acknowledgments

感谢所有为这个项目做出贡献的开发者和学习者。

Thanks to all developers and learners who have contributed to this project.

---

**开始你的AI Python学习之旅吧！/ Start your AI Python learning journey!** 🚀