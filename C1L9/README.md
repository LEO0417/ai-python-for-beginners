# 第9课：使用变量构建LLM提示词 / L9: Building LLM prompts with variables

## 📚 课程概述 / Course Overview

本课程教你如何在Python中使用变量来构建动态的LLM提示词。你将学习如何将变量嵌入到字符串中，创建个性化的AI交互体验。

This lesson teaches you how to use variables in Python to build dynamic LLM prompts. You'll learn how to embed variables into strings to create personalized AI interaction experiences.

## 🎯 学习目标 / Learning Objectives

- 理解如何使用f-string格式化字符串 / Understand how to use f-string formatting
- 学习将变量嵌入到LLM提示词中 / Learn to embed variables into LLM prompts  
- 掌握Python变量命名规则 / Master Python variable naming rules
- 练习调试变量名错误 / Practice debugging variable name errors
- 创建动态的AI交互 / Create dynamic AI interactions

## 🏗️ 项目结构 / Project Structure

```
C1L9/
├── C1L9_Bilingual.ipynb      # 双语课程笔记本 / Bilingual lesson notebook
├── helper_functions.py       # 辅助函数模块 / Helper functions module  
├── requirements.txt          # Python依赖 / Python dependencies
└── README.md                # 项目说明 / Project documentation
```

## 🚀 快速开始 / Quick Start

### 环境要求 / Prerequisites

- Python 3.7+ 
- Jupyter Notebook
- (可选) Ollama + gemma2:latest 模型 / (Optional) Ollama + gemma2:latest model

### 安装步骤 / Installation Steps

1. **克隆或下载项目文件 / Clone or download project files**

2. **安装依赖 / Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **启动Jupyter Notebook / Start Jupyter Notebook**
   ```bash
   jupyter notebook C1L9_Bilingual.ipynb
   ```

### Ollama配置 (可选) / Ollama Configuration (Optional)

如果你想使用真实的LLM模型而不是模拟响应，可以安装Ollama：

If you want to use real LLM models instead of simulated responses, you can install Ollama:

1. **安装Ollama / Install Ollama**
   - 访问 https://ollama.ai 下载安装 / Visit https://ollama.ai to download and install

2. **下载gemma3n模型 / Download gemma3n model**
   ```bash
   ollama pull gemma3n:latest
   ```

3. **验证安装 / Verify installation**
   ```bash
   ollama run gemma3n:latest "Hello, how are you?"
   ```

## 📖 课程内容 / Lesson Content

### 核心概念 / Core Concepts

1. **变量与字符串格式化 / Variables and String Formatting**
   - 使用f-string语法 / Using f-string syntax
   - 变量插值 / Variable interpolation

2. **LLM提示词构建 / LLM Prompt Construction**
   - 动态提示词生成 / Dynamic prompt generation
   - 个性化AI交互 / Personalized AI interactions

3. **变量命名规则 / Variable Naming Rules**
   - 有效的变量名 / Valid variable names
   - 常见错误和修复 / Common errors and fixes

### 实践练习 / Practical Exercises

- 修复变量名错误 / Fix variable name errors
- 创建个性化推荐系统 / Create personalized recommendation system
- 构建动态故事生成器 / Build dynamic story generator

## 🏗️ 文件说明 / File Descriptions

### `helper_functions.py`

包含课程所需的辅助函数，**现已集成本地Ollama大模型**：

Contains helper functions required for the lesson, **now integrated with local Ollama LLM**:

- `print_llm_response()` - 调用本地Ollama模型并打印响应 / Call local Ollama model and print response
- `get_llm_response()` - 获取LLM响应但不打印 / Get LLM response without printing
- `_get_fallback_response()` - 备用响应函数 / Fallback response function

**智能降级机制 / Intelligent Fallback Mechanism:**
- 优先使用Ollama本地模型 / Prioritize Ollama local model
- 如果Ollama不可用，自动切换到智能模拟响应 / Automatically switch to intelligent simulated responses if Ollama unavailable
- 确保课程始终可以正常运行 / Ensure the lesson always runs smoothly

## 🔧 故障排除 / Troubleshooting

### 常见问题 / Common Issues

1. **变量名错误 / Variable Name Errors**
   - 不能以数字开头 / Cannot start with numbers
   - 不能包含空格或特殊字符 / Cannot contain spaces or special characters
   - 使用下划线连接单词 / Use underscores to connect words

2. **字符串格式化错误 / String Formatting Errors**
   - 检查f-string语法 / Check f-string syntax
   - 确保变量已定义 / Ensure variables are defined
   - 注意引号匹配 / Pay attention to quote matching

3. **Ollama连接问题 / Ollama Connection Issues**
   - 确保Ollama服务正在运行 / Ensure Ollama service is running
   - 检查模型是否已下载 / Check if model is downloaded
   - 系统会自动降级到模拟模式 / System automatically falls back to simulation mode

## 🎓 学习成果 / Learning Outcomes

完成本课程后，你将能够：

After completing this lesson, you will be able to:

- ✅ 使用变量创建动态LLM提示词 / Use variables to create dynamic LLM prompts
- ✅ 掌握Python字符串格式化技巧 / Master Python string formatting techniques  
- ✅ 理解并遵循变量命名规范 / Understand and follow variable naming conventions
- ✅ 调试和修复常见的语法错误 / Debug and fix common syntax errors
- ✅ 创建个性化的AI交互体验 / Create personalized AI interaction experiences

## 📚 相关资源 / Related Resources

- [Python f-string官方文档 / Python f-string Official Documentation](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)
- [Python变量命名规范 / Python Variable Naming Conventions](https://pep8.org/#naming-conventions)
- [Ollama官方网站 / Ollama Official Website](https://ollama.ai)

## 🤝 贡献 / Contributing

欢迎提交问题和改进建议！/ Welcome to submit issues and improvement suggestions!

## 📄 许可证 / License

本项目仅用于教育目的 / This project is for educational purposes only.