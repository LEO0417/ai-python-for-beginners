# AI Python for Beginners
# AI Python 初学者教程

这个项目提供了一系列Python和AI的入门教程，支持使用本地ollama大模型进行学习和实践。

This project provides a series of Python and AI beginner tutorials, supporting local ollama large language models for learning and practice.

## 🚀 本地大模型设置指南 / Local LLM Setup Guide

### 📋 前提条件 / Prerequisites

1. **安装Python 3.9+**
2. **安装Ollama** - 从 [https://ollama.ai](https://ollama.ai) 下载并安装

### 🔧 快速设置 / Quick Setup

#### 1. 安装Ollama / Install Ollama

**macOS/Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
从官网下载安装包：https://ollama.ai/download

#### 2. 下载推荐模型 / Download Recommended Models

```bash
# 小型快速模型 (推荐初学者) / Small fast model (recommended for beginners)
ollama pull qwen3:0.6b

# 中等性能模型 / Medium performance model  
ollama pull gemma3n:latest

# 大型高性能模型 / Large high-performance model
ollama pull llama3.1:8b
```

#### 3. 启动Ollama服务 / Start Ollama Service

```bash
ollama serve
```

#### 4. 配置项目 / Configure Project

克隆项目并配置：
```bash
git clone <this-repository>
cd ai-python-for-beginners

# 复制配置文件模板 / Copy config template
cp ollama_config.json.example ollama_config.json

# 编辑配置文件，设置你选择的模型 / Edit config file with your chosen model
```

在 `ollama_config.json` 中设置你的模型：
```json
{
  "default_model": "qwen3:0.6b"
}
```

### 🎯 模型选择建议 / Model Selection Guide

| 模型 / Model | 大小 / Size | 速度 / Speed | 质量 / Quality | 适用场景 / Use Case |
|--------------|-------------|--------------|----------------|---------------------|
| `qwen3:0.6b` | 522MB | ⚡⚡⚡ | ⭐⭐⭐ | 初学者、快速测试 / Beginners, Quick testing |
| `gemma3n:latest` | 7.5GB | ⚡⚡ | ⭐⭐⭐⭐ | 日常使用、课程练习 / Daily use, Course exercises |
| `llama3.1:8b` | ~4.7GB | ⚡ | ⭐⭐⭐⭐⭐ | 高质量对话、复杂任务 / High-quality chat, Complex tasks |

### 📦 安装依赖 / Install Dependencies

```bash
# 全局依赖 / Global dependencies
pip install -r requirements.txt

# 或进入具体课程目录 / Or enter specific lesson directory
cd C1L9
pip install -r requirements.txt
```

### 🧪 测试设置 / Test Setup

运行测试脚本验证配置：
```python
# 测试连接 / Test connection
from helper_functions import print_llm_response, get_default_model

print(f"当前模型 / Current model: {get_default_model()}")
print_llm_response("Hello, this is a test!")
```

### ⚙️ 高级配置 / Advanced Configuration

#### 切换模型 / Switch Models

```python
from helper_functions import set_default_model, get_available_models

# 查看可用模型 / View available models
print(get_available_models())

# 切换到其他模型 / Switch to another model
set_default_model("gemma3n:latest")
```

#### 课程级配置 / Lesson-level Configuration

你可以为每个课程设置不同的模型：
```bash
cd C1L9
echo '{"default_model": "qwen3:0.6b"}' > ollama_config.json
```

#### 环境变量配置 / Environment Variable Configuration

```bash
# 临时设置 / Temporary setting
export OLLAMA_MODEL="llama3.1:8b"

# 永久设置 (添加到 ~/.bashrc 或 ~/.zshrc) / Permanent setting
echo 'export OLLAMA_MODEL="qwen3:0.6b"' >> ~/.zshrc
```

### 🔍 故障排除 / Troubleshooting

#### 常见问题 / Common Issues

1. **模型未找到 / Model not found**
   ```bash
   ollama list  # 查看已安装模型 / Check installed models
   ollama pull <model-name>  # 下载缺失模型 / Download missing model
   ```

2. **连接超时 / Connection timeout**
   ```bash
   ollama serve  # 确保服务正在运行 / Ensure service is running
   ```

3. **权限问题 / Permission issues**
   ```bash
   sudo chown -R $USER ~/.ollama  # 修复权限 / Fix permissions
   ```

#### 诊断工具 / Diagnostic Tools

```python
from helper_functions import show_model_info, test_llm_connection

# 显示详细配置信息 / Show detailed config info
show_model_info()

# 测试连接状态 / Test connection status
is_connected = test_llm_connection()
print(f"连接状态 / Connection status: {is_connected}")
```

### 💡 性能优化建议 / Performance Optimization Tips

1. **选择合适的模型大小** / Choose appropriate model size
   - 学习阶段：使用 `qwen3:0.6b` (快速响应)
   - 日常使用：使用 `gemma3n:latest` (平衡性能)
   - 高质量需求：使用 `llama3.1:8b` (最佳质量)

2. **系统资源建议** / System Resource Recommendations
   - 内存：至少8GB (推荐16GB+)
   - 存储：至少10GB可用空间
   - CPU：现代多核处理器

3. **网络设置** / Network Settings
   - 首次下载模型需要良好的网络连接
   - 后续使用完全离线

### 📚 使用示例 / Usage Examples

#### 基础使用 / Basic Usage
```python
from helper_functions import print_llm_response

# 简单对话 / Simple conversation
print_llm_response("What is Python?")

# 使用变量 / Using variables
name = "Alice"
age = 25
print_llm_response(f"Tell me about a {age}-year-old person named {name}")
```

#### 课程练习 / Course Exercises
```python
# C1L9 示例 / C1L9 Example
name = "Otto Matic"
dog_age = 21/7
print_llm_response(f"""If {name} were a dog, he would be {dog_age} years old.
Describe what life stage that would be for a dog.""")
```

### 🆘 获得帮助 / Getting Help

如果遇到问题，请：
1. 查看上述故障排除部分
2. 运行诊断工具
3. 检查ollama官方文档：https://ollama.ai/
4. 提交Issue到项目仓库

If you encounter issues:
1. Check the troubleshooting section above
2. Run diagnostic tools
3. Check ollama official docs: https://ollama.ai/
4. Submit an issue to the project repository

---

## 🎓 课程目录 / Course Contents

- **C1L6**: Python基础 / Python Basics
- **C1L7**: 数据类型 / Data Types  
- **C1L9**: 变量与LLM提示 / Variables and LLM Prompts
- **C1L10**: 函数与控制流 / Functions and Control Flow
- **C2L1-C2L7**: 中级Python / Intermediate Python
- **C3L6**: 高级应用 / Advanced Applications

每个课程目录包含：
- Jupyter Notebook (.ipynb)
- 辅助函数 (helper_functions.py)
- 依赖文件 (requirements.txt)
- 说明文档 (README.md)

Each lesson directory contains:
- Jupyter Notebook (.ipynb)
- Helper functions (helper_functions.py)
- Dependencies (requirements.txt)  
- Documentation (README.md)

## 🤝 贡献 / Contributing

欢迎贡献代码、报告问题或提出建议！
Welcome to contribute code, report issues, or suggest improvements!

## 📄 许可证 / License

请查看 LICENSE 文件了解详情。
See LICENSE file for details.