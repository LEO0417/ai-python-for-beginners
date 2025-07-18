# API Documentation / API文档

## 概述 / Overview

本文档详细介绍了AI Python初学者教程项目中`helper_functions`包的所有API接口。

This document provides detailed information about all API interfaces in the `helper_functions` package of the AI Python for Beginners tutorial project.

## 目录 / Table of Contents

- [模型配置管理 / Model Configuration Management](#模型配置管理--model-configuration-management)
- [LLM工具函数 / LLM Utilities](#llm工具函数--llm-utilities)
- [通用工具函数 / Common Utilities](#通用工具函数--common-utilities)
- [使用示例 / Usage Examples](#使用示例--usage-examples)
- [错误处理 / Error Handling](#错误处理--error-handling)

## 模型配置管理 / Model Configuration Management

### `get_default_model()`

获取当前默认模型名称。

Get the current default model name.

**返回值 / Returns:**
- `str`: 模型名称 / Model name

**优先级顺序 / Priority Order:**
1. 环境变量 `OLLAMA_MODEL` / Environment variable `OLLAMA_MODEL`
2. 课程级配置文件 / Lesson-level configuration file
3. 全局配置文件 / Global configuration file
4. 自动检测的第一个可用模型 / Auto-detected first available model
5. 默认回退值 `"gemma3n:latest"` / Default fallback value `"gemma3n:latest"`

**示例 / Example:**

```python
from helper_functions import get_default_model

# 获取当前默认模型 / Get current default model
current_model = get_default_model()
print(f"当前模型 / Current model: {current_model}")
```

### `set_default_model(model_name, scope='global')`

设置默认模型到配置文件。

Set default model to configuration file.

**参数 / Parameters:**
- `model_name` (str): 模型名称 / Model name
- `scope` (str, optional): 配置范围，可选值：`'global'` 或 `'lesson'` / Configuration scope, options: `'global'` or `'lesson'`

**返回值 / Returns:**
- `None`

**异常 / Exceptions:**
- 如果保存配置失败，会打印错误信息 / Prints error message if saving configuration fails

**示例 / Example:**

```python
from helper_functions import set_default_model

# 设置全局默认模型 / Set global default model
set_default_model("qwen3:0.6b", scope="global")

# 设置课程级默认模型 / Set lesson-level default model
set_default_model("gemma3n:latest", scope="lesson")
```

### `get_available_models()`

获取所有可用的ollama模型列表。

Get list of all available ollama models.

**返回值 / Returns:**
- `list[str]`: 可用模型名称列表 / List of available model names

**示例 / Example:**

```python
from helper_functions import get_available_models

# 获取可用模型列表 / Get available models list
models = get_available_models()
print("可用模型 / Available models:")
for model in models:
    print(f"  - {model}")
```

### `show_model_info()`

显示当前模型配置的详细信息。

Show detailed information about current model configuration.

**返回值 / Returns:**
- `None`

**输出信息包括 / Output includes:**
- 当前使用的模型 / Currently used model
- 环境变量设置 / Environment variable settings
- 课程级配置 / Lesson-level configuration
- 全局配置 / Global configuration
- 可用模型列表 / Available models list

**示例 / Example:**

```python
from helper_functions import show_model_info

# 显示模型配置信息 / Show model configuration info
show_model_info()
```

## LLM工具函数 / LLM Utilities

### `print_llm_response(prompt)`

使用本地Ollama模型生成并打印LLM响应。

Generate and print LLM response using local Ollama model.

**参数 / Parameters:**
- `prompt` (str): 要发送给LLM的提示词 / Prompt to send to the LLM

**返回值 / Returns:**
- `None`: 只打印响应，不返回值 / Only prints response, returns nothing

**示例 / Example:**

```python
from helper_functions import print_llm_response

# 简单对话 / Simple conversation
print_llm_response("What is Python?")

# 使用变量的动态提示 / Dynamic prompt with variables
name = "Alice"
age = 25
print_llm_response(f"Tell me about a {age}-year-old person named {name}.")
```

### `get_llm_response(prompt)`

获取LLM响应但不打印。

Get LLM response without printing.

**参数 / Parameters:**
- `prompt` (str): 要发送给LLM的提示词 / Prompt to send to the LLM

**返回值 / Returns:**
- `str`: LLM的响应文本 / LLM response text

**异常 / Exceptions:**
- 如果调用失败，返回错误信息 / Returns error message if call fails

**示例 / Example:**

```python
from helper_functions import get_llm_response

# 获取响应并存储 / Get response and store
response = get_llm_response("Explain machine learning in simple terms.")
print(f"Response length: {len(response)} characters")

# 处理响应 / Process response
if "machine learning" in response.lower():
    print("Response contains the requested topic.")
```

### `test_llm_connection()`

测试与LLM的连接状态。

Test connection status with LLM.

**返回值 / Returns:**
- `bool`: 连接成功返回 `True`，失败返回 `False` / Returns `True` if connection successful, `False` otherwise

**示例 / Example:**

```python
from helper_functions import test_llm_connection

# 测试连接 / Test connection
if test_llm_connection():
    print("✅ LLM连接正常 / LLM connection is working")
else:
    print("❌ LLM连接失败 / LLM connection failed")
```

## 通用工具函数 / Common Utilities

### `get_project_root()`

获取项目根目录路径。

Get project root directory path.

**返回值 / Returns:**
- `str`: 项目根目录的绝对路径 / Absolute path to project root directory

**示例 / Example:**

```python
from helper_functions import get_project_root

# 获取项目根目录 / Get project root directory
root_path = get_project_root()
print(f"项目根目录 / Project root: {root_path}")
```

### `setup_logging(level='INFO')`

设置日志记录配置。

Setup logging configuration.

**参数 / Parameters:**
- `level` (str, optional): 日志级别，可选值：`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'` / Log level, options: `'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`

**返回值 / Returns:**
- `None`

**示例 / Example:**

```python
from helper_functions import setup_logging

# 设置调试级别日志 / Set debug level logging
setup_logging(level='DEBUG')

# 设置信息级别日志 / Set info level logging
setup_logging(level='INFO')
```

## 使用示例 / Usage Examples

### 基础使用 / Basic Usage

```python
# 导入所需函数 / Import required functions
from helper_functions import (
    print_llm_response,
    get_default_model,
    set_default_model,
    show_model_info
)

# 1. 检查当前模型 / Check current model
print(f"当前模型 / Current model: {get_default_model()}")

# 2. 显示详细配置信息 / Show detailed configuration info
show_model_info()

# 3. 简单的AI对话 / Simple AI conversation
print_llm_response("Hello! Please introduce yourself.")

# 4. 切换模型 / Switch model
set_default_model("qwen3:0.6b", scope="lesson")
```

### 高级使用 / Advanced Usage

```python
from helper_functions import (
    get_llm_response,
    get_available_models,
    test_llm_connection,
    setup_logging
)

# 1. 启用调试日志 / Enable debug logging
setup_logging(level='DEBUG')

# 2. 检查连接状态 / Check connection status
if not test_llm_connection():
    print("❌ 无法连接到LLM服务 / Cannot connect to LLM service")
    exit(1)

# 3. 获取并处理响应 / Get and process response
prompt = "Explain the difference between list and tuple in Python."
response = get_llm_response(prompt)

# 4. 分析响应 / Analyze response
if len(response) > 100:
    print("✅ 获得了详细的响应 / Received detailed response")
else:
    print("⚠️ 响应较短，可能需要更具体的提示 / Response is short, may need more specific prompt")

# 5. 列出所有可用模型 / List all available models
models = get_available_models()
print(f"找到 {len(models)} 个可用模型 / Found {len(models)} available models")
```

### 错误处理示例 / Error Handling Example

```python
from helper_functions import print_llm_response, get_llm_response

def safe_llm_call(prompt):
    """安全的LLM调用函数 / Safe LLM call function"""
    try:
        response = get_llm_response(prompt)
        if response and "Error" not in response:
            return response
        else:
            return "❌ LLM调用失败 / LLM call failed"
    except Exception as e:
        return f"❌ 异常错误 / Exception error: {str(e)}"

# 使用安全调用 / Use safe call
result = safe_llm_call("What is machine learning?")
print(result)
```

## 错误处理 / Error Handling

### 常见错误类型 / Common Error Types

#### 1. 模型未找到 / Model Not Found

```python
# 错误信息示例 / Error message example
# "Error: model 'xxx' not found"

# 解决方案 / Solution
from helper_functions import get_available_models, set_default_model

# 检查可用模型 / Check available models
models = get_available_models()
if models:
    # 使用第一个可用模型 / Use first available model
    set_default_model(models[0])
else:
    print("请先下载模型 / Please download models first")
```

#### 2. 连接超时 / Connection Timeout

```python
# 错误信息示例 / Error message example
# "Connection timeout" or "Service unavailable"

# 解决方案 / Solution
from helper_functions import test_llm_connection
import time

def wait_for_connection(max_attempts=5):
    """等待连接建立 / Wait for connection to establish"""
    for attempt in range(max_attempts):
        if test_llm_connection():
            return True
        print(f"连接尝试 {attempt + 1}/{max_attempts} / Connection attempt {attempt + 1}/{max_attempts}")
        time.sleep(2)
    return False

if not wait_for_connection():
    print("❌ 无法建立连接，请检查ollama服务 / Cannot establish connection, please check ollama service")
```

#### 3. 配置文件错误 / Configuration File Error

```python
# 错误信息示例 / Error message example
# "Failed to save config" or "Invalid JSON"

# 解决方案 / Solution
import json
import os

def fix_config_file(config_path="ollama_config.json"):
    """修复配置文件 / Fix configuration file"""
    try:
        # 检查文件是否存在 / Check if file exists
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                json.load(f)  # 验证JSON格式 / Validate JSON format
        else:
            # 创建默认配置 / Create default configuration
            default_config = {"default_model": "gemma3n:latest"}
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=2)
        print("✅ 配置文件正常 / Configuration file is OK")
    except json.JSONDecodeError:
        print("❌ 配置文件格式错误 / Configuration file format error")
    except Exception as e:
        print(f"❌ 配置文件错误 / Configuration file error: {e}")
```

### 调试技巧 / Debugging Tips

#### 1. 启用详细日志 / Enable Verbose Logging

```python
from helper_functions import setup_logging

# 启用调试日志 / Enable debug logging
setup_logging(level='DEBUG')

# 现在所有操作都会有详细日志 / Now all operations will have detailed logs
```

#### 2. 系统诊断 / System Diagnosis

```python
from helper_functions import show_model_info, test_llm_connection, get_available_models

def diagnose_system():
    """系统诊断函数 / System diagnosis function"""
    print("🔍 系统诊断开始 / System diagnosis started")
    print("=" * 50)
    
    # 1. 检查配置 / Check configuration
    print("📋 模型配置信息 / Model configuration info:")
    show_model_info()
    
    # 2. 测试连接 / Test connection
    print("\n🔗 连接测试 / Connection test:")
    if test_llm_connection():
        print("✅ 连接正常 / Connection OK")
    else:
        print("❌ 连接失败 / Connection failed")
    
    # 3. 检查可用模型 / Check available models
    print("\n📦 可用模型 / Available models:")
    models = get_available_models()
    if models:
        for i, model in enumerate(models, 1):
            print(f"  {i}. {model}")
    else:
        print("  ❌ 未找到任何模型 / No models found")
    
    print("=" * 50)
    print("🔍 系统诊断完成 / System diagnosis completed")

# 运行诊断 / Run diagnosis
diagnose_system()
```

## 最佳实践 / Best Practices

### 1. 模型选择 / Model Selection

```python
from helper_functions import get_available_models, set_default_model

def choose_optimal_model():
    """选择最优模型 / Choose optimal model"""
    models = get_available_models()
    
    # 优先级顺序 / Priority order
    preferred_models = [
        "qwen3:0.6b",      # 快速响应 / Fast response
        "gemma3n:latest",   # 平衡性能 / Balanced performance
        "llama3.1:8b"       # 高质量 / High quality
    ]
    
    for preferred in preferred_models:
        if preferred in models:
            set_default_model(preferred)
            print(f"✅ 选择模型 / Selected model: {preferred}")
            return preferred
    
    # 如果没有找到首选模型，使用第一个可用的 / If no preferred model found, use first available
    if models:
        set_default_model(models[0])
        return models[0]
    
    return None
```

### 2. 批量处理 / Batch Processing

```python
from helper_functions import get_llm_response

def batch_process_prompts(prompts):
    """批量处理提示词 / Batch process prompts"""
    results = []
    
    for i, prompt in enumerate(prompts, 1):
        print(f"处理第 {i}/{len(prompts)} 个提示 / Processing prompt {i}/{len(prompts)}")
        
        try:
            response = get_llm_response(prompt)
            results.append({
                'prompt': prompt,
                'response': response,
                'status': 'success'
            })
        except Exception as e:
            results.append({
                'prompt': prompt,
                'response': None,
                'status': 'error',
                'error': str(e)
            })
    
    return results

# 使用示例 / Usage example
prompts = [
    "What is Python?",
    "Explain variables in programming.",
    "How does machine learning work?"
]

results = batch_process_prompts(prompts)
```

### 3. 性能监控 / Performance Monitoring

```python
import time
from helper_functions import get_llm_response

def monitored_llm_call(prompt):
    """带性能监控的LLM调用 / LLM call with performance monitoring"""
    start_time = time.time()
    
    try:
        response = get_llm_response(prompt)
        end_time = time.time()
        
        # 计算性能指标 / Calculate performance metrics
        response_time = end_time - start_time
        response_length = len(response)
        
        print(f"📊 性能统计 / Performance Stats:")
        print(f"  响应时间 / Response time: {response_time:.2f}s")
        print(f"  响应长度 / Response length: {response_length} chars")
        print(f"  处理速度 / Processing speed: {response_length/response_time:.1f} chars/s")
        
        return response
    
    except Exception as e:
        print(f"❌ 调用失败 / Call failed: {e}")
        return None
```

## 版本兼容性 / Version Compatibility

### 支持的Python版本 / Supported Python Versions

- Python 3.9+
- Python 3.10+
- Python 3.11+
- Python 3.12+

### 依赖要求 / Dependencies

- `subprocess` (内置模块 / Built-in module)
- `json` (内置模块 / Built-in module)
- `os` (内置模块 / Built-in module)
- `sys` (内置模块 / Built-in module)

### 外部依赖 / External Dependencies

- **Ollama**: 需要安装并运行ollama服务 / Requires ollama service to be installed and running
- **Models**: 需要下载至少一个ollama模型 / Requires at least one ollama model to be downloaded

## 贡献指南 / Contributing Guidelines

如果您想为API添加新功能或修复bug，请遵循以下指南：

If you want to add new features or fix bugs for the API, please follow these guidelines:

1. **保持向后兼容性** / Maintain backward compatibility
2. **添加双语注释** / Add bilingual comments
3. **编写单元测试** / Write unit tests
4. **更新文档** / Update documentation
5. **遵循代码风格** / Follow code style guidelines

## 获取帮助 / Getting Help

如果您在使用API时遇到问题：

If you encounter issues while using the API:

1. **查看错误处理部分** / Check the error handling section
2. **运行系统诊断** / Run system diagnosis
3. **检查ollama服务状态** / Check ollama service status
4. **在GitHub上提交Issue** / Submit an issue on GitHub

---

**文档版本 / Document Version**: v1.0.0  
**最后更新 / Last Updated**: 2025-01-18  
**维护者 / Maintainer**: AI Python Bilingual Course Team