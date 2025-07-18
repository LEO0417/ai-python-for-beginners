@echo off
setlocal enabledelayedexpansion

REM AI Python课程Windows设置脚本 / AI Python Course Windows Setup Script
REM 这个脚本会自动设置AI Python课程的基本环境
REM This script automatically sets up the basic environment for AI Python course

echo.
echo =====================================================================
echo AI Python课程Windows设置脚本 / AI Python Course Windows Setup Script
echo =====================================================================
echo.

REM 检查Python版本 / Check Python version
echo [INFO] 检查Python版本 / Checking Python version...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] 未找到Python / Python not found
    echo [ERROR] 请从 https://python.org 下载并安装Python 3.9或更高版本
    echo [ERROR] Please download and install Python 3.9 or higher from https://python.org
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [SUCCESS] Python版本 / Python version: %PYTHON_VERSION%

REM 检查Python版本是否符合要求 / Check if Python version meets requirements
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if %MAJOR% lss 3 (
    echo [ERROR] Python版本过低 / Python version too low: %PYTHON_VERSION%
    echo [ERROR] 需要Python 3.9或更高版本 / Requires Python 3.9 or higher
    pause
    exit /b 1
)

if %MAJOR% equ 3 if %MINOR% lss 9 (
    echo [ERROR] Python版本过低 / Python version too low: %PYTHON_VERSION%
    echo [ERROR] 需要Python 3.9或更高版本 / Requires Python 3.9 or higher
    pause
    exit /b 1
)

REM 检查Ollama安装 / Check Ollama installation
echo [INFO] 检查Ollama安装 / Checking Ollama installation...

ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Ollama未安装 / Ollama not installed
    echo [INFO] 请从 https://ollama.ai/download 下载并安装Ollama
    echo [INFO] Please download and install Ollama from https://ollama.ai/download
    echo [INFO] 安装完成后重新运行此脚本 / Run this script again after installation
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('ollama --version') do set OLLAMA_VERSION=%%i
    echo [SUCCESS] Ollama已安装 / Ollama installed: !OLLAMA_VERSION!
)

REM 检查Ollama服务 / Check Ollama service
echo [INFO] 检查Ollama服务状态 / Checking Ollama service status...

tasklist /FI "IMAGENAME eq ollama.exe" 2>nul | find /I "ollama.exe" >nul
if %errorlevel% neq 0 (
    echo [WARNING] Ollama服务未运行 / Ollama service is not running
    echo [INFO] 请在另一个命令行窗口中运行: ollama serve
    echo [INFO] Please run in another command line window: ollama serve
    echo [INFO] 然后按任意键继续 / Then press any key to continue
    pause
) else (
    echo [SUCCESS] Ollama服务正在运行 / Ollama service is running
)

REM 检查模型 / Check models
echo [INFO] 检查已安装的模型 / Checking installed models...

ollama list >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] 无法获取模型列表 / Cannot get model list
    set MODELS_FOUND=0
) else (
    REM 简单检查是否有模型 / Simple check if models exist
    for /f "skip=1 tokens=*" %%i in ('ollama list') do (
        set MODELS_FOUND=1
        goto :models_check_done
    )
    set MODELS_FOUND=0
)

:models_check_done
if %MODELS_FOUND% equ 0 (
    echo [WARNING] 没有找到已安装的模型 / No installed models found
    echo [INFO] 正在安装推荐模型 / Installing recommended models...
    
    echo [INFO] 安装轻量级模型 / Installing lightweight model: qwen3:0.6b
    ollama pull qwen3:0.6b
    
    if %errorlevel% equ 0 (
        echo [SUCCESS] 模型安装成功 / Model installed successfully: qwen3:0.6b
    ) else (
        echo [WARNING] 模型安装失败 / Model installation failed: qwen3:0.6b
    )
    
    echo [INFO] 安装平衡模型 / Installing balanced model: gemma3n:latest
    ollama pull gemma3n:latest
    
    if %errorlevel% equ 0 (
        echo [SUCCESS] 模型安装成功 / Model installed successfully: gemma3n:latest
    ) else (
        echo [WARNING] 模型安装失败 / Model installation failed: gemma3n:latest
    )
) else (
    echo [SUCCESS] 找到已安装的模型 / Found installed models
)

REM 安装Python依赖 / Install Python dependencies
echo [INFO] 安装Python依赖 / Installing Python dependencies...

if exist requirements.txt (
    python -m pip install -r requirements.txt
    if %errorlevel% equ 0 (
        echo [SUCCESS] Python依赖安装成功 / Python dependencies installed successfully
    ) else (
        echo [WARNING] Python依赖安装失败 / Python dependencies installation failed
    )
) else (
    echo [WARNING] 没有找到requirements.txt文件 / requirements.txt file not found
)

REM 创建配置文件 / Create configuration file
echo [INFO] 创建配置文件 / Creating configuration file...

REM 获取第一个可用模型 / Get first available model
for /f "skip=1 tokens=1" %%i in ('ollama list') do (
    set DEFAULT_MODEL=%%i
    goto :model_found
)

:model_found
if "%DEFAULT_MODEL%"=="" (
    set DEFAULT_MODEL=qwen3:0.6b
)

REM 创建配置文件 / Create configuration file
echo {> ollama_config.json
echo   "default_model": "%DEFAULT_MODEL%",>> ollama_config.json
echo   "timeout": 60,>> ollama_config.json
echo   "retry_attempts": 3,>> ollama_config.json
echo   "setup_version": "1.0.0",>> ollama_config.json
echo   "setup_date": "%date% %time%">> ollama_config.json
echo }>> ollama_config.json

if exist ollama_config.json (
    echo [SUCCESS] 配置文件创建成功 / Configuration file created successfully: ollama_config.json
    echo [INFO] 默认模型 / Default model: %DEFAULT_MODEL%
) else (
    echo [ERROR] 创建配置文件失败 / Failed to create configuration file
)

REM 测试设置 / Test setup
echo [INFO] 测试设置 / Testing setup...

python -c "
import sys
sys.path.insert(0, '.')
try:
    from helper_functions import get_default_model, test_llm_connection
    print('[SUCCESS] Python模块导入成功 / Python modules imported successfully')
    
    model = get_default_model()
    print(f'[INFO] 当前模型 / Current model: {model}')
    
    if test_llm_connection():
        print('[SUCCESS] 连接测试成功 / Connection test successful')
        exit(0)
    else:
        print('[WARNING] 连接测试失败 / Connection test failed')
        exit(1)
except Exception as e:
    print(f'[ERROR] 测试失败 / Test failed: {e}')
    exit(1)
" 2>nul

if %errorlevel% equ 0 (
    echo [SUCCESS] 设置测试成功 / Setup test successful
) else (
    echo [WARNING] 设置测试失败 / Setup test failed
)

echo.
echo =====================================================================
echo [SUCCESS] 设置完成！/ Setup completed!
echo =====================================================================
echo.
echo [INFO] 你现在可以开始使用AI Python课程了！
echo [INFO] You can now start using the AI Python course!
echo.
echo [INFO] 运行以下命令开始第一课：
echo [INFO] Run the following command to start the first lesson:
echo [INFO] cd C1L9 ^&^& jupyter notebook C1L9_Bilingual.ipynb
echo.

pause