# 自动化设置脚本 / Automated Setup Scripts

这个目录包含了AI Python初学者教程项目的自动化设置脚本。

This directory contains automated setup scripts for the AI Python for Beginners tutorial project.

## 脚本列表 / Script List

### 1. `setup.py` - Python设置脚本 / Python Setup Script

**功能 / Features:**
- 全面的系统检查和设置
- 智能错误处理和恢复
- 详细的日志记录
- 跨平台支持

**使用方法 / Usage:**

```bash
# 运行Python设置脚本 / Run Python setup script
python3 scripts/setup.py

# 或者 / Or
cd scripts && python3 setup.py
```

**特点 / Features:**
- ✅ 检查Python版本 / Check Python version
- ✅ 检查并安装Ollama / Check and install Ollama
- ✅ 启动Ollama服务 / Start Ollama service
- ✅ 下载推荐模型 / Download recommended models
- ✅ 安装Python依赖 / Install Python dependencies
- ✅ 创建配置文件 / Create configuration file
- ✅ 测试设置 / Test setup
- ✅ 生成详细日志 / Generate detailed logs

### 2. `setup.sh` - Bash设置脚本 / Bash Setup Script

**功能 / Features:**
- 轻量级快速设置
- 支持macOS和Linux
- 彩色输出
- 简单易用

**使用方法 / Usage:**

```bash
# 运行Bash设置脚本 / Run Bash setup script
./scripts/setup.sh

# 或者 / Or
cd scripts && ./setup.sh
```

**特点 / Features:**
- ✅ 自动检测操作系统 / Auto-detect operating system
- ✅ 检查Python版本 / Check Python version
- ✅ 安装Ollama（通过Homebrew或官方脚本） / Install Ollama (via Homebrew or official script)
- ✅ 启动Ollama服务 / Start Ollama service
- ✅ 下载推荐模型 / Download recommended models
- ✅ 创建配置文件 / Create configuration file
- ✅ 测试设置 / Test setup

### 3. `setup.bat` - Windows批处理脚本 / Windows Batch Script

**功能 / Features:**
- 专为Windows系统设计
- 简单的GUI提示
- 自动暂停等待用户输入

**使用方法 / Usage:**

```cmd
REM 运行Windows设置脚本 / Run Windows setup script
scripts\setup.bat

REM 或者双击文件 / Or double-click the file
```

**特点 / Features:**
- ✅ 检查Python版本 / Check Python version
- ✅ 检查Ollama安装 / Check Ollama installation
- ✅ 引导用户手动启动服务 / Guide user to manually start service
- ✅ 下载推荐模型 / Download recommended models
- ✅ 安装Python依赖 / Install Python dependencies
- ✅ 创建配置文件 / Create configuration file
- ✅ 测试设置 / Test setup

## 选择合适的脚本 / Choose the Right Script

### 推荐使用 / Recommended

**Python脚本 (`setup.py`)**
- 最全面的功能
- 智能错误处理
- 详细的日志记录
- 适合所有用户

### 其他选择 / Alternatives

**Bash脚本 (`setup.sh`)**
- 适合Linux/macOS用户
- 快速轻量级
- 命令行友好

**Windows批处理 (`setup.bat`)**
- 适合Windows用户
- 简单易用
- GUI友好

## 系统要求 / System Requirements

### 通用要求 / Common Requirements
- Python 3.9 或更高版本 / Python 3.9 or higher
- 互联网连接（用于下载模型） / Internet connection (for downloading models)
- 至少 4GB 可用磁盘空间 / At least 4GB available disk space
- 至少 4GB 内存 / At least 4GB RAM

### 操作系统支持 / Operating System Support
- ✅ macOS 10.15 或更高版本 / macOS 10.15 or higher
- ✅ Ubuntu 18.04 或更高版本 / Ubuntu 18.04 or higher
- ✅ Windows 10 或更高版本 / Windows 10 or higher
- ✅ 其他Linux发行版 / Other Linux distributions

## 设置流程 / Setup Process

### 1. 准备工作 / Preparation

```bash
# 1. 克隆项目 / Clone project
git clone <repository-url>
cd ai-python-for-beginners

# 2. 检查Python版本 / Check Python version
python3 --version

# 3. 确保网络连接 / Ensure network connection
ping google.com
```

### 2. 运行设置脚本 / Run Setup Script

选择适合您系统的脚本：

Choose the script suitable for your system:

```bash
# Python脚本（推荐） / Python script (recommended)
python3 scripts/setup.py

# Bash脚本（Linux/macOS） / Bash script (Linux/macOS)
./scripts/setup.sh

# Windows批处理 / Windows batch
scripts\setup.bat
```

### 3. 验证设置 / Verify Setup

```bash
# 检查Ollama服务 / Check Ollama service
ollama list

# 测试Python模块 / Test Python modules
python3 -c "from helper_functions import print_llm_response; print_llm_response('Hello!')"

# 启动Jupyter / Start Jupyter
cd C1L9 && jupyter notebook C1L9_Bilingual.ipynb
```

## 常见问题 / Common Issues

### 问题1：权限错误 / Issue 1: Permission Error

**解决方案 / Solution:**
```bash
# 为脚本添加执行权限 / Add execute permission to script
chmod +x scripts/setup.sh

# 使用sudo运行（如果需要） / Use sudo if needed
sudo ./scripts/setup.sh
```

### 问题2：网络连接问题 / Issue 2: Network Connection Issues

**解决方案 / Solution:**
```bash
# 检查网络连接 / Check network connection
ping ollama.ai

# 使用代理（如果需要） / Use proxy if needed
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
```

### 问题3：Python版本不符合要求 / Issue 3: Python Version Not Meeting Requirements

**解决方案 / Solution:**
```bash
# 安装Python 3.9+ / Install Python 3.9+
# macOS
brew install python@3.11

# Ubuntu
sudo apt install python3.11

# Windows: 从 python.org 下载 / Download from python.org
```

### 问题4：模型下载失败 / Issue 4: Model Download Failed

**解决方案 / Solution:**
```bash
# 手动下载模型 / Manually download models
ollama pull qwen3:0.6b
ollama pull gemma3n:latest

# 检查磁盘空间 / Check disk space
df -h

# 清理旧模型 / Clean old models
ollama rm old-model-name
```

## 高级设置 / Advanced Setup

### 自定义模型 / Custom Models

```bash
# 下载其他模型 / Download other models
ollama pull llama3.1:8b
ollama pull codellama:latest

# 修改配置文件 / Modify configuration file
nano ollama_config.json
```

### 开发环境 / Development Environment

```bash
# 创建虚拟环境 / Create virtual environment
python3 -m venv ai-python-env
source ai-python-env/bin/activate

# 安装开发依赖 / Install development dependencies
pip install -r requirements-dev.txt
```

### 性能优化 / Performance Optimization

```bash
# 设置环境变量 / Set environment variables
export OLLAMA_MAX_MEMORY=8GB
export OLLAMA_NUM_THREADS=4

# 监控资源使用 / Monitor resource usage
htop
```

## 日志和调试 / Logs and Debugging

### 日志文件 / Log Files

```bash
# Python脚本日志 / Python script logs
cat setup.log

# Ollama服务日志 / Ollama service logs
tail -f ollama.log

# 系统日志 / System logs
journalctl -u ollama
```

### 调试模式 / Debug Mode

```bash
# 启用调试模式 / Enable debug mode
export DEBUG=1
python3 scripts/setup.py

# 详细输出 / Verbose output
bash -x scripts/setup.sh
```

## 获取帮助 / Getting Help

如果设置过程中遇到问题，请：

If you encounter issues during setup:

1. **查看日志文件** / Check log files
2. **运行诊断脚本** / Run diagnostic script
3. **查看故障排除指南** / Check troubleshooting guide: `TROUBLESHOOTING.md`
4. **提交Issue** / Submit issue on GitHub

## 贡献 / Contributing

欢迎改进设置脚本！

Welcome to improve the setup scripts!

```bash
# 测试脚本 / Test script
python3 scripts/setup.py --dry-run

# 添加新功能 / Add new features
# 遵循现有代码风格 / Follow existing code style
# 添加双语注释 / Add bilingual comments
```

---

**版本 / Version**: 1.0.0  
**维护者 / Maintainer**: AI Python Bilingual Course Team  
**最后更新 / Last Updated**: 2025-01-18