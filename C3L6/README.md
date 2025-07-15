# Python初学者AI课程 - 第六课：将代码块转换为可重用的函数

本项目是基于 [DeepLearning.AI Python初学者课程](https://learn.deeplearning.ai/courses/ai-python-for-beginners/lesson/vvkwa/turning-code-blocks-into-reusable-functions) 创建的双语学习资源。

## 📚 课程内容

### 学习目标
- 理解函数的基本概念和重要性
- 学会定义和使用自己的函数  
- 掌握函数参数的使用
- 了解函数返回值的概念
- 通过实践练习巩固知识

### 主要概念
1. **函数定义** - Function Definition (`def` keyword)
2. **参数传递** - Parameter Passing 
3. **返回值** - Return Values (`return` statement)
4. **代码重用** - Code Reuse
5. **函数文档字符串** - Function Docstrings

## 🛠️ 项目结构

```
ai-python-for-beginners/
├── Lesson_6.ipynb              # 原始课程文件
├── Lesson_6_Bilingual.ipynb    # 双语版本
├── helper_functions.py         # 辅助函数模块
├── requirements.txt            # Python依赖
├── README.md                   # 项目说明
├── cape_town.txt               # 开普敦美食日记
├── paris.txt                   # 巴黎美食日记
├── sydney.txt                  # 悉尼美食日记
├── tokyo.txt                   # 东京美食日记
└── istanbul.txt                # 伊斯坦布尔美食日记
```

## 🚀 开始使用

### 环境要求
- Python 3.7+
- Jupyter Notebook 或 JupyterLab
- **Ollama (本地大模型服务)**
- 基本的Python知识

### 安装步骤

1. **安装并启动Ollama**
   ```bash
   # 安装Ollama (macOS)
   brew install ollama
   
   # 启动Ollama服务
   ollama serve
   
   # 下载并安装模型 (在新终端窗口中)
   ollama pull gemma3n
   ```

2. **安装Python依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **测试Ollama连接**
   ```bash
   python test_ollama.py
   ```

4. **启动Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

5. **打开课程文件**
   - 双语版本：`Lesson_6_Bilingual.ipynb`
   - 原版：`Lesson_6.ipynb`

## 📖 使用说明

### 特色功能
- 每个代码单元格都包含中英文注释
- 重要概念都有双语解释
- 练习题提供中文指导
- 包含详细的函数文档字符串

## 🏗️ 文件说明

### `helper_functions.py`
包含课程所需的辅助函数，**现已集成本地Ollama大模型**：
- `print_llm_response()` - 调用本地Ollama模型并打印响应
- `get_llm_response()` - 获取本地Ollama模型响应（返回字符串）
- `call_ollama()` - 核心Ollama API调用函数
- `test_ollama_connection()` - 测试Ollama连接和模型可用性

### 示例数据文件
课程使用的美食日记文件，包含不同城市的双语美食体验

## 🎯 练习内容

### 基础练习
1. **摄氏度转华氏度函数**
2. **米转英尺函数**

### 挑战练习
创建文件摘要函数 using LLM

## 💡 学习建议

1. **逐步学习** - 按顺序执行每个单元格
2. **理解概念** - 确保理解每个概念再继续
3. **动手实践** - 尝试修改代码参数
4. **完成练习** - 认真完成所有练习

## 📝 注意事项

- 本项目为教育目的创建
- **已集成本地Ollama大模型，提供真实的AI对话体验**
- 需要确保Ollama服务正在运行才能使用LLM功能
- 所有示例数据为虚构内容
- 模型响应时间取决于您的硬件配置

## 🤖 Ollama大模型集成

### 特色功能
- ✅ **真实AI对话体验** - 不再是模拟响应，而是真正的AI交互
- ✅ **本地部署** - 数据隐私安全，无需联网即可使用
- ✅ **中英文支持** - 支持中英文双语对话
- ✅ **教育优化** - 专门针对编程学习场景优化

### 当前使用模型
- **模型**: `gemma3n:latest` (Google Gemma 3系列)
- **特点**: 轻量级、响应快速、适合教育用途
- **语言支持**: 中文、英文

### 使用示例
```python
from helper_functions import print_llm_response, get_llm_response

# 基础对话
print_llm_response("What is a Python function?")

# 中文对话
response = get_llm_response("请解释Python函数的作用")
print(response)
```

### 故障排除
如果遇到连接问题：
1. 确保Ollama服务正在运行：`ollama serve`
2. 检查模型是否可用：`ollama list`
3. 运行连接测试：`python test_ollama.py`

## 🤝 如何使用双语版本

双语版本 `Lesson_6_Bilingual.ipynb` 的特点：
- 所有重要概念都有中英文对照说明
- 代码注释包含中英文解释
- 练习题提供中文指导和英文原文
- **现在包含真实的AI助手对话功能**
- 适合中文学习者逐步理解Python函数概念

享受学习Python函数的乐趣！🐍✨🤖