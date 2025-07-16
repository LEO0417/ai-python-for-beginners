# C1L9: Building LLM prompts with variables
# 第9课：使用变量构建LLM提示词

## 📋 课程概述 / Course Overview

本课程将教你如何使用Python变量与大语言模型(LLM)进行交互，学习如何构建动态的提示词并获得智能响应。

This lesson teaches you how to use Python variables to interact with Large Language Models (LLMs), learning to build dynamic prompts and get intelligent responses.

## 🚀 本地模型设置 / Local Model Setup

### 🎯 推荐配置 / Recommended Configuration

对于C1L9课程，我们推荐以下模型配置：

For C1L9 lesson, we recommend the following model configuration:

| 使用场景 / Use Case | 推荐模型 / Recommended Model | 原因 / Reason |
|-------------------|----------------------------|---------------|
| 初学者/快速测试 / Beginners/Quick Testing | `qwen3:0.6b` | 响应快速，资源占用低 / Fast response, low resource usage |
| 日常学习 / Daily Learning | `gemma3n:latest` | 平衡性能与质量 / Balanced performance and quality |
| 高质量练习 / High-quality Practice | `llama3.1:8b` | 最佳回答质量 / Best response quality |

### 🔧 快速设置步骤 / Quick Setup Steps

#### 1. 检查系统状态 / Check System Status

```bash
# 检查ollama是否已安装 / Check if ollama is installed
which ollama

# 查看已安装的模型 / View installed models
ollama list

# 检查ollama服务状态 / Check ollama service status
ollama serve --help
```

#### 2. 下载推荐模型 / Download Recommended Model

```bash
# 方案1：小型快速模型 (推荐新手) / Option 1: Small fast model (recommended for beginners)
ollama pull qwen3:0.6b

# 方案2：中等性能模型 / Option 2: Medium performance model
ollama pull gemma3n:latest

# 方案3：高性能模型 / Option 3: High performance model
ollama pull llama3.1:8b
```

#### 3. 配置课程模型 / Configure Course Model

**方法1：使用课程级配置文件 / Method 1: Course-level Configuration**

```bash
cd C1L9

# 创建课程专用配置 / Create course-specific config
echo '{
  "default_model": "qwen3:0.6b"
}' > ollama_config.json
```

**方法2：使用Python设置 / Method 2: Python Configuration**

```python
from helper_functions import set_default_model

# 设置为快速模型 / Set to fast model
set_default_model("qwen3:0.6b", scope="lesson")

# 或设置为高质量模型 / Or set to high-quality model
# set_default_model("llama3.1:8b", scope="lesson")
```

#### 4. 验证设置 / Verify Setup

```python
from helper_functions import print_llm_response, get_default_model, show_model_info

# 检查当前配置 / Check current configuration
print(f"当前模型 / Current model: {get_default_model()}")

# 运行测试 / Run test
print_llm_response("Hello! Please respond to confirm the connection is working.")

# 查看详细信息 / View detailed information
show_model_info()
```

### 🧪 课程功能测试 / Course Function Testing

运行以下代码测试课程中的主要功能：

Run the following code to test the main functions in the course:

```python
# 测试基础功能 / Test basic functionality
from helper_functions import print_llm_response

# 测试1：简单问答 / Test 1: Simple Q&A
print("=== 测试1：简单问答 / Test 1: Simple Q&A ===")
print_llm_response("What is the capital of France?")

# 测试2：变量插值 / Test 2: Variable interpolation
print("\n=== 测试2：变量插值 / Test 2: Variable Interpolation ===")
name = "Otto Matic"
dog_age = 21/7
print_llm_response(f"""If {name} were a dog, he would be {dog_age} years old.
Describe what life stage that would be for a dog and what that might 
entail in terms of energy level, interests, and behavior.""")

# 测试3：创意写作 / Test 3: Creative writing
print("\n=== 测试3：创意写作 / Test 3: Creative Writing ===")
driver = "unicorn"
drivers_vehicle = "colorful, asymmetric dinosaur car"
favorite_planet = "Pluto"
print_llm_response(f"""Write me a 300 word children's story about a {driver} racing
a {drivers_vehicle} for the {favorite_planet} champion cup.""")
```

### 🔍 故障排除 / Troubleshooting

#### 常见问题及解决方案 / Common Issues and Solutions

1. **模型未找到错误 / Model Not Found Error**
   
   **错误信息 / Error Message**: "Error: model 'xxx' not found"
   
   **解决方案 / Solution**:
   ```bash
   # 查看可用模型 / Check available models
   ollama list
   
   # 下载缺失的模型 / Download missing model
   ollama pull qwen3:0.6b
   
   # 或更新配置文件使用已有模型 / Or update config to use existing model
   ```

2. **连接超时 / Connection Timeout**
   
   **错误信息 / Error Message**: "Connection timeout" 或 "Service unavailable"
   
   **解决方案 / Solution**:
   ```bash
   # 启动ollama服务 / Start ollama service
   ollama serve
   
   # 或在后台运行 / Or run in background
   nohup ollama serve > /dev/null 2>&1 &
   ```

3. **权限问题 / Permission Issues**
   
   **错误信息 / Error Message**: "Permission denied"
   
   **解决方案 / Solution**:
   ```bash
   # 修复ollama目录权限 / Fix ollama directory permissions
   sudo chown -R $USER ~/.ollama
   
   # 或重新安装ollama / Or reinstall ollama
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

4. **导入错误 / Import Error**
   
   **错误信息 / Error Message**: "ModuleNotFoundError: No module named 'helper_functions'"
   
   **解决方案 / Solution**:
   ```bash
   # 确保在正确的目录 / Ensure in correct directory
   cd C1L9
   
   # 安装依赖 / Install dependencies
   pip install -r requirements.txt
   
   # 检查Python路径 / Check Python path
   python -c "import sys; print(sys.path)"
   ```

#### 诊断工具 / Diagnostic Tools

运行诊断脚本获取详细的系统信息：

Run diagnostic script to get detailed system information:

```python
from helper_functions import show_model_info, test_llm_connection, get_available_models

print("🔍 C1L9 诊断报告 / C1L9 Diagnostic Report")
print("=" * 50)

# 显示配置信息 / Show configuration info
show_model_info()

print("\n📋 可用模型列表 / Available Models List:")
models = get_available_models()
for i, model in enumerate(models, 1):
    print(f"  {i}. {model}")

print(f"\n🔗 连接测试 / Connection Test:")
connection_status = test_llm_connection()
status_text = "✅ 成功 / Success" if connection_status else "❌ 失败 / Failed"
print(f"  状态 / Status: {status_text}")

if not connection_status:
    print("\n💡 建议 / Suggestions:")
    print("  1. 检查ollama服务是否运行 / Check if ollama service is running")
    print("  2. 验证模型是否已下载 / Verify model is downloaded")
    print("  3. 检查配置文件 / Check configuration file")
```

### 💡 性能优化建议 / Performance Optimization Tips

#### 模型选择策略 / Model Selection Strategy

```python
# 根据你的硬件配置选择模型 / Choose model based on your hardware

import psutil
import os

def recommend_model():
    # 获取系统内存 / Get system memory
    memory_gb = psutil.virtual_memory().total / (1024**3)
    
    # 获取CPU核心数 / Get CPU cores
    cpu_cores = os.cpu_count()
    
    print(f"系统内存 / System Memory: {memory_gb:.1f} GB")
    print(f"CPU核心 / CPU Cores: {cpu_cores}")
    
    if memory_gb >= 16 and cpu_cores >= 8:
        print("推荐模型 / Recommended Model: llama3.1:8b (高性能)")
    elif memory_gb >= 8 and cpu_cores >= 4:
        print("推荐模型 / Recommended Model: gemma3n:latest (平衡)")
    else:
        print("推荐模型 / Recommended Model: qwen3:0.6b (轻量)")

recommend_model()
```

#### 课程学习建议 / Course Learning Tips

1. **从小模型开始 / Start with Small Models**
   - 使用 `qwen3:0.6b` 先熟悉功能
   - 确保所有代码都能正常运行
   - 理解变量插值的概念

2. **逐步升级 / Gradual Upgrade**
   - 熟悉后可以尝试 `gemma3n:latest`
   - 比较不同模型的响应质量
   - 观察响应时间的差异

3. **实验不同提示词 / Experiment with Different Prompts**
   - 尝试修改课程中的示例
   - 观察变量变化对输出的影响
   - 学习如何构建更好的提示词

### 📚 扩展练习 / Extended Exercises

完成课程基础内容后，可以尝试以下扩展练习：

After completing the basic course content, try these extended exercises:

```python
# 扩展练习1：多变量故事生成 / Extended Exercise 1: Multi-variable Story Generation
character = "勇敢的小兔子"  # brave little rabbit
setting = "神秘的森林"     # mysterious forest
quest = "寻找失落的宝藏"   # search for lost treasure
obstacle = "智慧的老龙"    # wise old dragon

print_llm_response(f"""创建一个关于{character}在{setting}中{quest}，
但遇到{obstacle}阻挡的冒险故事。故事要有开头、发展、高潮和结局。

Create an adventure story about {character} in {setting} on a quest to {quest},
but encountering {obstacle} as an obstacle. The story should have a beginning, 
development, climax, and ending.""")

# 扩展练习2：个性化学习助手 / Extended Exercise 2: Personalized Learning Assistant
subject = "Python编程"
difficulty = "初级"
learning_style = "实践为主"
time_available = "30分钟"

print_llm_response(f"""作为一个学习助手，请为想学习{subject}的学生制定一个{difficulty}难度、
{learning_style}的{time_available}学习计划。

As a learning assistant, please create a {time_available} study plan for a student 
who wants to learn {subject} at {difficulty} level with a {learning_style} approach.""")
```

### 🆘 获得帮助 / Getting Help

如果在C1L9课程中遇到问题：

If you encounter issues in C1L9 course:

1. **检查基础设置 / Check Basic Setup**
   - 运行上述诊断工具
   - 确认ollama服务状态
   - 验证模型是否下载

2. **查看错误日志 / Check Error Logs**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   # 然后重新运行有问题的代码
   ```

3. **寻求帮助 / Seek Help**
   - 查看项目主README的故障排除部分
   - 访问ollama官方文档：https://ollama.ai/
   - 在项目仓库提交Issue

---

## 🎯 学习目标 / Learning Objectives

完成本课程后，你将能够：

After completing this lesson, you will be able to:

- ✅ 理解Python变量的基本概念 / Understand basic Python variable concepts
- ✅ 使用f-string格式化字符串 / Use f-string for string formatting
- ✅ 将变量插入到LLM提示词中 / Insert variables into LLM prompts
- ✅ 构建动态的AI交互程序 / Build dynamic AI interaction programs
- ✅ 修复常见的变量命名错误 / Fix common variable naming errors

**开始你的AI编程之旅！/ Start your AI programming journey!** 🚀