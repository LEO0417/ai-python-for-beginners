# 故障排除指南 / Troubleshooting Guide

本指南提供了AI Python初学者教程项目中常见问题的详细解决方案。

This guide provides detailed solutions for common issues in the AI Python for Beginners tutorial project.

## 目录 / Table of Contents

1. [快速诊断 / Quick Diagnosis](#快速诊断--quick-diagnosis)
2. [安装问题 / Installation Issues](#安装问题--installation-issues)
3. [配置问题 / Configuration Issues](#配置问题--configuration-issues)
4. [模型问题 / Model Issues](#模型问题--model-issues)
5. [连接问题 / Connection Issues](#连接问题--connection-issues)
6. [性能问题 / Performance Issues](#性能问题--performance-issues)
7. [导入错误 / Import Errors](#导入错误--import-errors)
8. [系统兼容性 / System Compatibility](#系统兼容性--system-compatibility)
9. [高级故障排除 / Advanced Troubleshooting](#高级故障排除--advanced-troubleshooting)

## 快速诊断 / Quick Diagnosis

### 一键诊断脚本 / One-Click Diagnosis Script

在开始故障排除之前，运行以下诊断脚本：

Before starting troubleshooting, run this diagnostic script:

```python
from helper_functions import show_model_info, test_llm_connection, get_available_models
import subprocess
import sys
import os

def quick_diagnosis():
    """快速系统诊断 / Quick system diagnosis"""
    print("🔍 AI Python课程 - 快速诊断 / AI Python Course - Quick Diagnosis")
    print("=" * 60)
    
    # 1. Python环境检查 / Python environment check
    print(f"🐍 Python版本 / Python version: {sys.version}")
    print(f"📍 Python路径 / Python path: {sys.executable}")
    
    # 2. 项目路径检查 / Project path check
    print(f"📁 当前工作目录 / Current working directory: {os.getcwd()}")
    
    # 3. Ollama安装检查 / Ollama installation check
    try:
        result = subprocess.run(['ollama', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Ollama已安装 / Ollama installed: {result.stdout.strip()}")
        else:
            print("❌ Ollama未正确安装 / Ollama not properly installed")
    except FileNotFoundError:
        print("❌ Ollama未找到 / Ollama not found")
    
    # 4. 模型配置检查 / Model configuration check
    print("\n📋 模型配置信息 / Model configuration info:")
    show_model_info()
    
    # 5. 连接测试 / Connection test
    print(f"\n🔗 连接测试 / Connection test:")
    if test_llm_connection():
        print("✅ LLM连接正常 / LLM connection working")
    else:
        print("❌ LLM连接失败 / LLM connection failed")
    
    # 6. 建议下一步 / Next steps suggestion
    print("\n💡 建议 / Recommendations:")
    models = get_available_models()
    if not models:
        print("1. 下载推荐模型 / Download recommended model: ollama pull qwen3:0.6b")
    
    print("2. 检查具体错误信息 / Check specific error messages")
    print("3. 查看详细故障排除指南 / See detailed troubleshooting guide")
    print("=" * 60)

# 运行诊断 / Run diagnosis
quick_diagnosis()
```

## 安装问题 / Installation Issues

### 问题1：Ollama安装失败 / Issue 1: Ollama Installation Failed

**症状 / Symptoms:**
- `ollama: command not found`
- `bash: ollama: command not found`
- 下载安装脚本失败

**解决方案 / Solutions:**

#### macOS

```bash
# 方法1：官方安装脚本 / Method 1: Official install script
curl -fsSL https://ollama.ai/install.sh | sh

# 方法2：使用Homebrew / Method 2: Using Homebrew
brew install ollama

# 方法3：手动下载 / Method 3: Manual download
# 访问 https://ollama.ai/download 下载对应版本

# 验证安装 / Verify installation
ollama --version
which ollama
```

#### Linux

```bash
# 方法1：官方安装脚本 / Method 1: Official install script
curl -fsSL https://ollama.ai/install.sh | sh

# 方法2：使用包管理器 / Method 2: Using package manager
# Ubuntu/Debian
sudo apt update
sudo apt install ollama

# CentOS/RHEL
sudo yum install ollama

# 验证安装 / Verify installation
ollama --version
systemctl status ollama
```

#### Windows

```powershell
# 方法1：从官网下载 / Method 1: Download from official site
# 访问 https://ollama.ai/download 下载Windows版本

# 方法2：使用Chocolatey / Method 2: Using Chocolatey
choco install ollama

# 方法3：使用Scoop / Method 3: Using Scoop
scoop install ollama

# 验证安装 / Verify installation
ollama --version
```

### 问题2：Python依赖安装失败 / Issue 2: Python Dependencies Installation Failed

**症状 / Symptoms:**
- `ModuleNotFoundError: No module named 'xxx'`
- `pip install` 失败

**解决方案 / Solutions:**

```bash
# 1. 升级pip / Upgrade pip
python -m pip install --upgrade pip

# 2. 使用requirements.txt / Use requirements.txt
cd ai-python-for-beginners
pip install -r requirements.txt

# 3. 单独安装缺失模块 / Install missing modules individually
pip install jupyter notebook ipython

# 4. 使用conda环境 / Use conda environment
conda create -n ai-python python=3.9
conda activate ai-python
pip install -r requirements.txt

# 5. 检查Python版本兼容性 / Check Python version compatibility
python --version  # 需要Python 3.9+ / Requires Python 3.9+
```

## 配置问题 / Configuration Issues

### 问题3：配置文件格式错误 / Issue 3: Configuration File Format Error

**症状 / Symptoms:**
- `JSON decode error`
- `Invalid JSON format`
- 配置不生效

**解决方案 / Solutions:**

```python
import json
import os

def fix_config_file():
    """修复配置文件 / Fix configuration file"""
    config_files = [
        'ollama_config.json',
        'C1L9/ollama_config.json',
        'C1L10/ollama_config.json'
    ]
    
    for config_file in config_files:
        if os.path.exists(config_file):
            try:
                # 尝试读取配置文件 / Try to read config file
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                print(f"✅ {config_file} 格式正确 / format is correct")
                
            except json.JSONDecodeError as e:
                print(f"❌ {config_file} JSON格式错误 / JSON format error: {e}")
                
                # 创建标准配置 / Create standard configuration
                standard_config = {
                    "default_model": "qwen3:0.6b",
                    "timeout": 60,
                    "retry_attempts": 3
                }
                
                # 备份错误文件 / Backup error file
                backup_file = f"{config_file}.backup"
                if os.path.exists(config_file):
                    os.rename(config_file, backup_file)
                    print(f"📄 已备份错误文件到 / Backed up error file to: {backup_file}")
                
                # 写入标准配置 / Write standard configuration
                with open(config_file, 'w', encoding='utf-8') as f:
                    json.dump(standard_config, f, indent=2, ensure_ascii=False)
                print(f"✅ 已修复配置文件 / Fixed configuration file: {config_file}")

# 运行修复 / Run fix
fix_config_file()
```

### 问题4：环境变量配置问题 / Issue 4: Environment Variable Configuration Issues

**症状 / Symptoms:**
- 环境变量不生效
- 模型设置被忽略

**解决方案 / Solutions:**

```bash
# 1. 检查当前环境变量 / Check current environment variables
echo $OLLAMA_MODEL
echo $OLLAMA_HOST
echo $OLLAMA_PORT

# 2. 设置临时环境变量 / Set temporary environment variables
export OLLAMA_MODEL="qwen3:0.6b"
export OLLAMA_HOST="127.0.0.1"
export OLLAMA_PORT="11434"

# 3. 永久设置环境变量 / Set permanent environment variables
# 对于bash / For bash
echo 'export OLLAMA_MODEL="qwen3:0.6b"' >> ~/.bashrc
source ~/.bashrc

# 对于zsh / For zsh
echo 'export OLLAMA_MODEL="qwen3:0.6b"' >> ~/.zshrc
source ~/.zshrc

# 4. 验证环境变量 / Verify environment variables
python -c "import os; print('OLLAMA_MODEL:', os.getenv('OLLAMA_MODEL'))"
```

## 模型问题 / Model Issues

### 问题5：模型未找到 / Issue 5: Model Not Found

**症状 / Symptoms:**
- `Error: model 'xxx' not found`
- `pull model first`

**解决方案 / Solutions:**

```bash
# 1. 查看已安装模型 / Check installed models
ollama list

# 2. 下载推荐模型 / Download recommended models
ollama pull qwen3:0.6b         # 轻量级模型 / Lightweight model
ollama pull gemma3n:latest     # 平衡模型 / Balanced model
ollama pull llama3.1:8b        # 高性能模型 / High-performance model

# 3. 验证模型下载 / Verify model download
ollama list
ollama run qwen3:0.6b "Hello, test message"

# 4. 使用Python检查模型 / Check models using Python
from helper_functions import get_available_models, set_default_model

models = get_available_models()
print("可用模型 / Available models:", models)

if models:
    set_default_model(models[0])  # 使用第一个可用模型 / Use first available model
```

### 问题6：模型下载失败 / Issue 6: Model Download Failed

**症状 / Symptoms:**
- 下载中断
- 网络连接错误
- 磁盘空间不足

**解决方案 / Solutions:**

```bash
# 1. 检查磁盘空间 / Check disk space
df -h

# 2. 检查网络连接 / Check network connection
ping ollama.ai
curl -I https://ollama.ai

# 3. 使用代理下载 / Download with proxy
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
ollama pull qwen3:0.6b

# 4. 重试下载 / Retry download
ollama pull qwen3:0.6b --retry 3

# 5. 清理损坏的下载 / Clean corrupted downloads
ollama rm qwen3:0.6b  # 删除损坏的模型 / Remove corrupted model
ollama pull qwen3:0.6b  # 重新下载 / Re-download
```

## 连接问题 / Connection Issues

### 问题7：Ollama服务未运行 / Issue 7: Ollama Service Not Running

**症状 / Symptoms:**
- `Connection refused`
- `Service unavailable`
- `No connection could be made`

**解决方案 / Solutions:**

```bash
# 1. 检查服务状态 / Check service status
ps aux | grep ollama
pgrep ollama

# 2. 启动Ollama服务 / Start Ollama service
# 前台运行 / Run in foreground
ollama serve

# 后台运行 / Run in background
nohup ollama serve > ollama.log 2>&1 &

# 3. 验证服务启动 / Verify service startup
curl http://localhost:11434/api/version

# 4. 检查端口占用 / Check port usage
lsof -i :11434
netstat -tlnp | grep 11434

# 5. 重启服务 / Restart service
pkill ollama
ollama serve &
```

### 问题8：防火墙阻止连接 / Issue 8: Firewall Blocking Connection

**症状 / Symptoms:**
- 连接超时
- 无法访问本地端口

**解决方案 / Solutions:**

```bash
# macOS
# 1. 检查防火墙状态 / Check firewall status
sudo pfctl -s info

# 2. 允许Ollama通过防火墙 / Allow Ollama through firewall
sudo pfctl -f /etc/pf.conf

# Linux (Ubuntu/Debian)
# 1. 检查防火墙状态 / Check firewall status
sudo ufw status

# 2. 允许端口访问 / Allow port access
sudo ufw allow 11434
sudo ufw reload

# 3. 检查iptables规则 / Check iptables rules
sudo iptables -L

# Windows
# 1. 检查Windows防火墙设置 / Check Windows firewall settings
# 2. 添加Ollama到防火墙例外 / Add Ollama to firewall exceptions
```

## 性能问题 / Performance Issues

### 问题9：响应速度慢 / Issue 9: Slow Response Speed

**症状 / Symptoms:**
- 等待时间过长
- 系统资源占用高

**解决方案 / Solutions:**

```python
# 1. 选择合适的模型 / Choose appropriate model
from helper_functions import set_default_model, get_available_models

def optimize_model_selection():
    """优化模型选择 / Optimize model selection"""
    import psutil
    
    # 获取系统资源 / Get system resources
    memory_gb = psutil.virtual_memory().total / (1024**3)
    cpu_count = psutil.cpu_count()
    
    print(f"系统内存 / System memory: {memory_gb:.1f} GB")
    print(f"CPU核心数 / CPU cores: {cpu_count}")
    
    # 根据系统资源推荐模型 / Recommend model based on system resources
    if memory_gb >= 16 and cpu_count >= 8:
        recommended_model = "llama3.1:8b"
        print("推荐高性能模型 / Recommended high-performance model")
    elif memory_gb >= 8 and cpu_count >= 4:
        recommended_model = "gemma3n:latest"
        print("推荐平衡模型 / Recommended balanced model")
    else:
        recommended_model = "qwen3:0.6b"
        print("推荐轻量级模型 / Recommended lightweight model")
    
    set_default_model(recommended_model)
    return recommended_model

# 运行优化 / Run optimization
optimize_model_selection()
```

```bash
# 2. 系统优化 / System optimization
# 关闭不必要的程序 / Close unnecessary programs
# 增加虚拟内存 / Increase virtual memory
# 使用SSD存储 / Use SSD storage

# 3. 监控资源使用 / Monitor resource usage
top -p $(pgrep ollama)
htop
```

### 问题10：内存不足 / Issue 10: Out of Memory

**症状 / Symptoms:**
- `Out of memory`
- 系统卡死
- 进程被杀死

**解决方案 / Solutions:**

```bash
# 1. 检查内存使用情况 / Check memory usage
free -h
ps aux --sort=-%mem | head

# 2. 释放内存 / Free memory
sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'

# 3. 使用更小的模型 / Use smaller model
ollama pull qwen3:0.6b
export OLLAMA_MODEL="qwen3:0.6b"

# 4. 限制内存使用 / Limit memory usage
export OLLAMA_MAX_MEMORY=4GB
export OLLAMA_MEMORY_LIMIT=4096

# 5. 增加交换文件 / Add swap file
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## 导入错误 / Import Errors

### 问题11：模块导入失败 / Issue 11: Module Import Failed

**症状 / Symptoms:**
- `ModuleNotFoundError: No module named 'helper_functions'`
- `ImportError: cannot import name 'xxx'`

**解决方案 / Solutions:**

```python
# 1. 检查Python路径 / Check Python path
import sys
print("Python路径 / Python paths:")
for path in sys.path:
    print(f"  {path}")

# 2. 手动添加项目路径 / Manually add project path
import os
import sys

# 获取项目根目录 / Get project root directory
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 3. 使用相对导入 / Use relative imports
try:
    from helper_functions import print_llm_response
    print("✅ 成功导入 / Successfully imported")
except ImportError as e:
    print(f"❌ 导入失败 / Import failed: {e}")
    
    # 尝试替代导入方法 / Try alternative import methods
    try:
        sys.path.append(os.path.join(os.getcwd(), 'helper_functions'))
        from model_config import get_default_model
        from llm_utils import print_llm_response
        print("✅ 使用替代方法成功导入 / Successfully imported using alternative method")
    except ImportError as e2:
        print(f"❌ 替代方法也失败 / Alternative method also failed: {e2}")
```

```bash
# 4. 检查文件结构 / Check file structure
find . -name "*.py" -type f | head -20
ls -la helper_functions/

# 5. 重新安装包 / Reinstall package
pip uninstall helper_functions
pip install -e .  # 如果有setup.py / If setup.py exists
```

## 系统兼容性 / System Compatibility

### 问题12：Python版本兼容性 / Issue 12: Python Version Compatibility

**症状 / Symptoms:**
- 语法错误
- 功能不可用
- 类型提示错误

**解决方案 / Solutions:**

```bash
# 1. 检查Python版本 / Check Python version
python --version
python3 --version

# 2. 升级Python / Upgrade Python
# macOS
brew install python@3.11
brew link python@3.11

# Ubuntu/Debian
sudo apt update
sudo apt install python3.11

# 3. 使用pyenv管理Python版本 / Use pyenv to manage Python versions
curl https://pyenv.run | bash
pyenv install 3.11.0
pyenv global 3.11.0

# 4. 创建虚拟环境 / Create virtual environment
python3.11 -m venv ai-python-env
source ai-python-env/bin/activate
pip install --upgrade pip
```

### 问题13：操作系统兼容性 / Issue 13: Operating System Compatibility

**症状 / Symptoms:**
- 命令不存在
- 路径分隔符错误
- 权限问题

**解决方案 / Solutions:**

```python
# 1. 跨平台路径处理 / Cross-platform path handling
import os
from pathlib import Path

def get_safe_path(*paths):
    """获取跨平台安全路径 / Get cross-platform safe path"""
    return str(Path(*paths))

# 使用示例 / Usage example
config_path = get_safe_path("helper_functions", "config.json")
print(f"配置文件路径 / Config file path: {config_path}")

# 2. 跨平台命令执行 / Cross-platform command execution
import subprocess
import sys

def run_command(cmd):
    """跨平台命令执行 / Cross-platform command execution"""
    if sys.platform == "win32":
        cmd = ["cmd", "/c"] + cmd if isinstance(cmd, list) else f"cmd /c {cmd}"
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), 1

# 3. 检查系统类型 / Check system type
def get_system_info():
    """获取系统信息 / Get system information"""
    import platform
    
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    }

print("系统信息 / System info:", get_system_info())
```

## 高级故障排除 / Advanced Troubleshooting

### 问题14：深度调试 / Issue 14: Deep Debugging

当常规方法无法解决问题时，使用以下高级调试技巧：

When conventional methods fail to solve the problem, use these advanced debugging techniques:

```python
import logging
import traceback
import sys
from datetime import datetime

# 1. 启用详细日志记录 / Enable verbose logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# 2. 创建调试装饰器 / Create debug decorator
def debug_function(func):
    """调试函数装饰器 / Debug function decorator"""
    def wrapper(*args, **kwargs):
        logging.debug(f"调用函数 / Calling function: {func.__name__}")
        logging.debug(f"参数 / Arguments: args={args}, kwargs={kwargs}")
        
        try:
            result = func(*args, **kwargs)
            logging.debug(f"返回结果 / Return result: {result}")
            return result
        except Exception as e:
            logging.error(f"函数异常 / Function exception: {e}")
            logging.error(f"堆栈跟踪 / Stack trace: {traceback.format_exc()}")
            raise
    
    return wrapper

# 3. 使用调试装饰器 / Use debug decorator
@debug_function
def test_llm_call():
    from helper_functions import print_llm_response
    print_llm_response("This is a test message")

# 4. 创建完整的系统报告 / Create complete system report
def generate_system_report():
    """生成完整系统报告 / Generate complete system report"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'system_info': get_system_info(),
        'python_info': {
            'version': sys.version,
            'executable': sys.executable,
            'path': sys.path
        },
        'environment_variables': dict(os.environ),
        'ollama_status': None,
        'models_available': [],
        'disk_space': None,
        'memory_info': None
    }
    
    # 添加更多系统信息...
    try:
        import psutil
        report['memory_info'] = {
            'total': psutil.virtual_memory().total,
            'available': psutil.virtual_memory().available,
            'percent': psutil.virtual_memory().percent
        }
        report['disk_space'] = {
            'total': psutil.disk_usage('/').total,
            'free': psutil.disk_usage('/').free,
            'percent': psutil.disk_usage('/').percent
        }
    except ImportError:
        pass
    
    # 保存报告 / Save report
    with open('system_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    return report

# 运行系统报告 / Run system report
report = generate_system_report()
print("系统报告已保存到 system_report.json / System report saved to system_report.json")
```

### 问题15：性能分析 / Issue 15: Performance Analysis

```python
import time
import cProfile
import pstats
from functools import wraps

def profile_function(func):
    """性能分析装饰器 / Performance profiling decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        pr.disable()
        
        # 分析结果 / Analyze results
        stats = pstats.Stats(pr)
        stats.sort_stats('cumulative')
        
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        print("性能分析结果:")
        stats.print_stats(10)  # 显示前10个最耗时的函数
        
        return result
    
    return wrapper

# 使用性能分析 / Use performance profiling
@profile_function
def test_performance():
    from helper_functions import get_llm_response
    response = get_llm_response("Test performance analysis")
    return response

# 运行性能测试 / Run performance test
test_performance()
```

## 获取帮助 / Getting Help

### 社区支持 / Community Support

如果本指南无法解决您的问题，请通过以下渠道获取帮助：

If this guide doesn't solve your problem, please get help through these channels:

1. **GitHub Issues**: 在项目仓库中提交详细的问题报告
   **GitHub Issues**: Submit detailed issue reports in the project repository

2. **讨论区**: 参与项目讨论区的交流
   **Discussions**: Participate in project discussions

3. **邮件支持**: 发送邮件至项目维护者
   **Email Support**: Send email to project maintainers

### 提交问题报告 / Submitting Issue Reports

提交问题时，请包含以下信息：

When submitting issues, please include the following information:

```markdown
## 问题描述 / Problem Description
[详细描述问题现象 / Detailed description of the problem]

## 环境信息 / Environment Information
- 操作系统 / Operating System: 
- Python版本 / Python Version: 
- Ollama版本 / Ollama Version: 
- 项目版本 / Project Version: 

## 重现步骤 / Reproduction Steps
1. [第一步 / Step 1]
2. [第二步 / Step 2]
3. [第三步 / Step 3]

## 错误信息 / Error Messages
```
[粘贴完整的错误信息 / Paste complete error messages]
```

## 系统报告 / System Report
[附上system_report.json内容 / Attach system_report.json content]

## 已尝试的解决方案 / Attempted Solutions
[列出已经尝试的解决方法 / List attempted solutions]
```

---

**文档版本 / Document Version**: v1.0.0  
**最后更新 / Last Updated**: 2025-01-18  
**维护者 / Maintainer**: AI Python Bilingual Course Team

希望这个故障排除指南能帮助您解决问题！如果您发现新的问题或有改进建议，请随时联系我们。

Hope this troubleshooting guide helps you solve your problems! If you find new issues or have improvement suggestions, please feel free to contact us.