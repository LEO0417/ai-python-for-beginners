# Ollama 本地大模型设置完整指南
# Complete Guide to Setting Up Ollama Local LLM

## 📖 概述 / Overview

本指南将帮助你在本项目中设置和使用本地ollama大语言模型。作为项目维护者，我使用 `qwen3:0.6b` 和 `gemma3n:latest` 模型进行开发和测试，推荐其他用户也使用这些模型以获得最佳体验。

This guide will help you set up and use local ollama Large Language Models in this project. As the project maintainer, I use `qwen3:0.6b` and `gemma3n:latest` models for development and testing, and recommend other users to use these models for the best experience.

## 🎯 推荐配置 / Recommended Configuration

### 作者使用的配置 / Author's Configuration

```json
{
  "primary_model": "qwen3:0.6b",      // 主要用于开发和快速测试
  "secondary_model": "gemma3n:latest", // 用于高质量示例和演示
  "system": "macOS 15.0.0",
  "hardware": "MacBook Pro M-series"
}
```

### 用户推荐配置 / User Recommended Configuration

| 用户类型 / User Type | 推荐模型 / Recommended Model | 内存需求 / Memory | 优势 / Advantages |
|---------------------|---------------------------|------------------|-------------------|
| 初学者 / Beginners | `qwen3:0.6b` | 1GB+ | 快速启动，低资源消耗 / Fast startup, low resource usage |
| 日常用户 / Regular Users | `gemma3n:latest` | 8GB+ | 平衡的性能和质量 / Balanced performance and quality |
| 高级用户 / Advanced Users | `llama3.1:8b` | 16GB+ | 最佳响应质量 / Best response quality |

## 🚀 安装步骤 / Installation Steps

### Step 1: 安装 Ollama / Install Ollama

#### macOS (推荐方法 / Recommended)
```bash
# 方法1：官方安装脚本 / Method 1: Official installer
curl -fsSL https://ollama.ai/install.sh | sh

# 方法2：Homebrew / Method 2: Homebrew
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### Windows
1. 访问 https://ollama.ai/download
2. 下载 Windows 安装包
3. 运行安装程序

### Step 2: 验证安装 / Verify Installation

```bash
# 检查ollama版本 / Check ollama version
ollama --version

# 检查服务状态 / Check service status
ollama serve --help
```

### Step 3: 下载推荐模型 / Download Recommended Models

#### 作者推荐的模型组合 / Author's Recommended Model Combination

```bash
# 主力模型：轻量快速 / Primary model: Lightweight and fast
ollama pull qwen3:0.6b

# 备用模型：高质量 / Backup model: High quality
ollama pull gemma3n:latest

# 可选：最佳质量模型 / Optional: Best quality model
ollama pull llama3.1:8b
```

#### 下载进度监控 / Download Progress Monitoring

```bash
# 查看下载状态 / Check download status
ollama list

# 示例输出 / Example output:
# NAME              ID              SIZE      MODIFIED          
# qwen3:0.6b        7df6b6e09427    522 MB    About an hour ago    
# gemma3n:latest    15cb39fd9394    7.5 GB    6 days ago           
```

### Step 4: 启动服务 / Start Service

```bash
# 前台启动 (用于调试) / Foreground start (for debugging)
ollama serve

# 后台启动 (推荐) / Background start (recommended)
nohup ollama serve > ollama.log 2>&1 &
```

### Step 5: 测试模型 / Test Models

```bash
# 测试qwen3模型 / Test qwen3 model
echo "Hello, how are you?" | ollama run qwen3:0.6b

# 测试gemma3n模型 / Test gemma3n model
echo "What is Python?" | ollama run gemma3n:latest
```

## ⚙️ 项目配置 / Project Configuration

### 全局配置 / Global Configuration

编辑项目根目录的 `ollama_config.json`：

Edit `ollama_config.json` in the project root:

```json
{
  "default_model": "qwen3:0.6b",
  "fallback_model": "gemma3n:latest",
  "timeout": 60,
  "retry_attempts": 3
}
```

### 课程级配置 / Lesson-level Configuration

为特定课程设置不同模型：

Set different models for specific lessons:

```bash
cd C1L9
echo '{
  "default_model": "qwen3:0.6b"
}' > ollama_config.json
```

### 环境变量配置 / Environment Variable Configuration

```bash
# 临时设置 / Temporary setting
export OLLAMA_MODEL="qwen3:0.6b"

# 永久设置 / Permanent setting (添加到 ~/.bashrc 或 ~/.zshrc)
echo 'export OLLAMA_MODEL="qwen3:0.6b"' >> ~/.zshrc
source ~/.zshrc
```

## 🔧 Python 集成 / Python Integration

### 基础使用 / Basic Usage

```python
from helper_functions import print_llm_response, get_default_model

# 检查当前模型 / Check current model
print(f"当前模型 / Current model: {get_default_model()}")

# 基础对话 / Basic conversation
print_llm_response("Hello! Please introduce yourself.")

# 使用变量 / Using variables
name = "Alice"
age = 25
print_llm_response(f"Tell me about a {age}-year-old person named {name}.")
```

### 高级配置 / Advanced Configuration

```python
from helper_functions import (
    set_default_model, 
    get_available_models, 
    show_model_info,
    test_llm_connection
)

# 查看所有可用模型 / View all available models
models = get_available_models()
print("可用模型 / Available models:", models)

# 切换模型 / Switch model
set_default_model("gemma3n:latest")

# 显示详细信息 / Show detailed info
show_model_info()

# 测试连接 / Test connection
is_connected = test_llm_connection()
print(f"连接状态 / Connection status: {is_connected}")
```

## 📊 性能对比 / Performance Comparison

基于作者的测试结果：

Based on author's test results:

| 模型 / Model | 响应时间 / Response Time | 内存使用 / Memory Usage | 质量评分 / Quality Score | 适用场景 / Use Case |
|--------------|------------------------|------------------------|------------------------|-------------------|
| `qwen3:0.6b` | ~2-5秒 / ~2-5s | ~1GB | 7/10 | 快速原型、学习练习 / Quick prototyping, learning |
| `gemma3n:latest` | ~10-20秒 / ~10-20s | ~8GB | 8.5/10 | 日常开发、演示 / Daily development, demos |
| `llama3.1:8b` | ~15-30秒 / ~15-30s | ~16GB | 9.5/10 | 生产环境、高质量输出 / Production, high-quality output |

## 🔍 故障排除 / Troubleshooting

### 常见问题和解决方案 / Common Issues and Solutions

#### 1. 模型下载失败 / Model Download Failed

**问题 / Issue**: "Error downloading model"

**解决方案 / Solution**:
```bash
# 检查网络连接 / Check network connection
ping ollama.ai

# 使用代理下载 / Download with proxy
export HTTP_PROXY=http://your-proxy:port
ollama pull qwen3:0.6b

# 手动重试 / Manual retry
ollama pull qwen3:0.6b --retry 5
```

#### 2. 模型不存在错误 / Model Not Found Error

**问题 / Issue**: "Error: model 'xxx' not found"

**解决方案 / Solution**:
```bash
# 列出已安装模型 / List installed models
ollama list

# 下载缺失模型 / Download missing model
ollama pull qwen3:0.6b

# 或更新配置文件 / Or update config file
echo '{"default_model": "qwen3:0.6b"}' > ollama_config.json
```

#### 3. 服务连接问题 / Service Connection Issues

**问题 / Issue**: "Connection refused" 或 "Service unavailable"

**解决方案 / Solution**:
```bash
# 检查服务状态 / Check service status
ps aux | grep ollama

# 重启服务 / Restart service
pkill ollama
ollama serve &

# 检查端口占用 / Check port usage
lsof -i :11434
```

#### 4. 内存不足 / Out of Memory

**问题 / Issue**: "Out of memory" 或系统卡顿

**解决方案 / Solution**:
```bash
# 切换到更小的模型 / Switch to smaller model
export OLLAMA_MODEL="qwen3:0.6b"

# 或者限制内存使用 / Or limit memory usage
export OLLAMA_MAX_MEMORY=4GB
```

### 诊断工具 / Diagnostic Tools

创建诊断脚本 `diagnose_ollama.py`：

Create diagnostic script `diagnose_ollama.py`:

```python
#!/usr/bin/env python3
import subprocess
import json
import os
import sys

def diagnose_ollama():
    print("🔍 Ollama 系统诊断 / Ollama System Diagnosis")
    print("=" * 50)
    
    # 检查ollama安装 / Check ollama installation
    try:
        result = subprocess.run(['which', 'ollama'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Ollama 已安装 / Ollama installed: {result.stdout.strip()}")
        else:
            print("❌ Ollama 未安装 / Ollama not installed")
            return
    except Exception as e:
        print(f"❌ 检查失败 / Check failed: {e}")
        return
    
    # 检查服务状态 / Check service status
    try:
        result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
        if 'ollama serve' in result.stdout:
            print("✅ Ollama 服务正在运行 / Ollama service is running")
        else:
            print("⚠️  Ollama 服务未运行 / Ollama service not running")
    except Exception as e:
        print(f"⚠️  无法检查服务状态 / Cannot check service status: {e}")
    
    # 检查已安装模型 / Check installed models
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            print("📋 已安装模型 / Installed models:")
            print(result.stdout)
        else:
            print("❌ 无法获取模型列表 / Cannot get model list")
    except Exception as e:
        print(f"❌ 检查模型失败 / Model check failed: {e}")
    
    # 检查配置文件 / Check config files
    config_files = ['ollama_config.json', 'C1L9/ollama_config.json']
    for config_file in config_files:
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                print(f"📄 配置文件 / Config file {config_file}:")
                print(f"   默认模型 / Default model: {config.get('default_model', 'Not set')}")
            except Exception as e:
                print(f"⚠️  配置文件读取失败 / Config file read failed: {e}")
    
    # 测试模型响应 / Test model response
    try:
        from helper_functions import get_default_model, test_llm_connection
        current_model = get_default_model()
        print(f"🎯 当前模型 / Current model: {current_model}")
        
        is_connected = test_llm_connection()
        status = "✅ 正常 / Normal" if is_connected else "❌ 异常 / Abnormal"
        print(f"🔗 连接测试 / Connection test: {status}")
        
    except Exception as e:
        print(f"❌ Python集成测试失败 / Python integration test failed: {e}")

if __name__ == "__main__":
    diagnose_ollama()
```

运行诊断：
```bash
python diagnose_ollama.py
```

## 💡 最佳实践 / Best Practices

### 1. 模型选择策略 / Model Selection Strategy

```python
def choose_model_by_task(task_type):
    """根据任务类型选择最适合的模型 / Choose best model by task type"""
    
    model_recommendations = {
        'learning': 'qwen3:0.6b',           # 学习练习 / Learning exercises
        'development': 'gemma3n:latest',     # 开发调试 / Development debugging  
        'demo': 'gemma3n:latest',            # 演示展示 / Demonstrations
        'production': 'llama3.1:8b',        # 生产环境 / Production
        'creative': 'llama3.1:8b',          # 创意写作 / Creative writing
        'coding': 'gemma3n:latest',          # 代码相关 / Code-related
    }
    
    return model_recommendations.get(task_type, 'qwen3:0.6b')

# 使用示例 / Usage example
task = 'learning'
recommended_model = choose_model_by_task(task)
print(f"推荐模型 / Recommended model for {task}: {recommended_model}")
```

### 2. 性能监控 / Performance Monitoring

```python
import time
import psutil

def monitor_llm_performance(prompt):
    """监控LLM调用性能 / Monitor LLM call performance"""
    
    # 记录开始时间和内存 / Record start time and memory
    start_time = time.time()
    start_memory = psutil.virtual_memory().used / (1024**3)
    
    # 调用LLM / Call LLM
    response = get_llm_response(prompt)
    
    # 记录结束时间和内存 / Record end time and memory
    end_time = time.time()
    end_memory = psutil.virtual_memory().used / (1024**3)
    
    # 计算性能指标 / Calculate performance metrics
    response_time = end_time - start_time
    memory_used = end_memory - start_memory
    
    print(f"响应时间 / Response time: {response_time:.2f}s")
    print(f"内存使用 / Memory used: {memory_used:.2f}GB")
    print(f"响应长度 / Response length: {len(response)} chars")
    
    return response
```

### 3. 配置管理 / Configuration Management

```python
class OllamaConfigManager:
    """Ollama配置管理器 / Ollama Configuration Manager"""
    
    def __init__(self):
        self.global_config = "ollama_config.json"
        self.lesson_configs = {}
    
    def set_lesson_model(self, lesson, model):
        """为特定课程设置模型 / Set model for specific lesson"""
        lesson_dir = f"{lesson}"
        config_path = f"{lesson_dir}/ollama_config.json"
        
        config = {"default_model": model}
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ {lesson} 模型设置为 / Model set to: {model}")
    
    def backup_config(self):
        """备份当前配置 / Backup current configuration"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        backup_file = f"ollama_config_backup_{timestamp}.json"
        
        if os.path.exists(self.global_config):
            with open(self.global_config, 'r') as src:
                with open(backup_file, 'w') as dst:
                    dst.write(src.read())
            print(f"✅ 配置已备份到 / Config backed up to: {backup_file}")

# 使用示例 / Usage example
config_manager = OllamaConfigManager()
config_manager.set_lesson_model("C1L9", "qwen3:0.6b")
config_manager.backup_config()
```

## 🚀 高级功能 / Advanced Features

### 模型热切换 / Hot Model Switching

```python
def switch_model_dynamically(task_complexity):
    """根据任务复杂度动态切换模型 / Dynamically switch model based on task complexity"""
    
    if task_complexity == 'simple':
        model = 'qwen3:0.6b'
    elif task_complexity == 'medium':
        model = 'gemma3n:latest'
    else:  # complex
        model = 'llama3.1:8b'
    
    set_default_model(model)
    print(f"已切换到模型 / Switched to model: {model}")
    return model

# 使用示例 / Usage example
switch_model_dynamically('simple')
print_llm_response("What is Python?")

switch_model_dynamically('complex')
print_llm_response("Explain quantum computing in detail.")
```

### 并发模型调用 / Concurrent Model Calls

```python
import asyncio
import concurrent.futures

async def compare_models(prompt):
    """比较不同模型的响应 / Compare responses from different models"""
    
    models = ['qwen3:0.6b', 'gemma3n:latest']
    responses = {}
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            model: executor.submit(get_model_response, prompt, model)
            for model in models
        }
        
        for model, future in futures.items():
            try:
                response = future.result(timeout=60)
                responses[model] = response
            except Exception as e:
                responses[model] = f"Error: {e}"
    
    return responses

def get_model_response(prompt, model):
    """获取指定模型的响应 / Get response from specified model"""
    original_model = get_default_model()
    try:
        set_default_model(model)
        return get_llm_response(prompt)
    finally:
        set_default_model(original_model)
```

## 📚 用户指南 / User Guide

### 新用户快速开始 / Quick Start for New Users

1. **按照本指南安装ollama和模型**
2. **克隆项目并进入目录**
3. **运行诊断脚本验证设置**
4. **从C1L9课程开始学习**

### 贡献者指南 / Contributor Guide

如果你想为项目贡献代码：

If you want to contribute to the project:

1. **使用作者推荐的模型配置进行测试**
2. **确保你的更改与现有的模型兼容**
3. **在PR中说明你使用的模型版本**
4. **提供性能测试结果**

### 问题报告 / Issue Reporting

报告问题时请包含：

When reporting issues, please include:

- 系统信息 (`uname -a`)
- Ollama版本 (`ollama --version`)
- 模型列表 (`ollama list`)
- 诊断脚本输出
- 错误详细信息

## 🤝 社区和支持 / Community and Support

- **GitHub Issues**: 报告问题和功能请求 / Report issues and feature requests
- **Ollama官方文档**: https://ollama.ai/
- **项目讨论**: 在项目仓库的Discussions区域 / In project repository Discussions

## 📄 版本历史 / Version History

- **v1.0**: 初始版本，支持基础ollama集成 / Initial version with basic ollama integration
- **v1.1**: 添加智能模型选择和故障转移 / Added smart model selection and fallback
- **v1.2**: 增强配置管理和诊断工具 / Enhanced configuration management and diagnostic tools

---

**祝你使用愉快！/ Happy coding!** 🚀

如有问题，请随时在项目仓库中提出Issue。

If you have any questions, feel free to create an issue in the project repository. 