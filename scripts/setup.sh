#!/bin/bash

# AI Python课程快速设置脚本 / AI Python Course Quick Setup Script
# 这个脚本会自动设置AI Python课程的基本环境
# This script automatically sets up the basic environment for AI Python course

set -e  # 在任何命令失败时退出 / Exit on any command failure

# 颜色定义 / Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数 / Print functions
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# 检查操作系统 / Check operating system
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        OS="windows"
    else
        OS="unknown"
    fi
    print_info "检测到操作系统 / Detected OS: $OS"
}

# 检查Python版本 / Check Python version
check_python() {
    print_header "检查Python版本 / Checking Python version..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_error "未找到Python / Python not found"
        print_error "请安装Python 3.9或更高版本 / Please install Python 3.9 or higher"
        exit 1
    fi
    
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -ge 9 ]]; then
        print_success "Python版本符合要求 / Python version OK: $PYTHON_VERSION"
    else
        print_error "Python版本过低 / Python version too low: $PYTHON_VERSION"
        print_error "需要Python 3.9或更高版本 / Requires Python 3.9 or higher"
        exit 1
    fi
}

# 检查Ollama安装 / Check Ollama installation
check_ollama() {
    print_header "检查Ollama安装 / Checking Ollama installation..."
    
    if command -v ollama &> /dev/null; then
        OLLAMA_VERSION=$(ollama --version 2>&1 | head -n 1)
        print_success "Ollama已安装 / Ollama installed: $OLLAMA_VERSION"
        return 0
    else
        print_warning "Ollama未安装 / Ollama not installed"
        return 1
    fi
}

# 安装Ollama / Install Ollama
install_ollama() {
    print_header "安装Ollama / Installing Ollama..."
    
    case $OS in
        "macos")
            # 检查是否有Homebrew / Check if Homebrew is available
            if command -v brew &> /dev/null; then
                print_info "使用Homebrew安装Ollama / Installing Ollama using Homebrew..."
                brew install ollama
            else
                print_info "使用官方安装脚本 / Using official install script..."
                curl -fsSL https://ollama.ai/install.sh | sh
            fi
            ;;
        "linux")
            print_info "使用官方安装脚本 / Using official install script..."
            curl -fsSL https://ollama.ai/install.sh | sh
            ;;
        "windows")
            print_error "Windows系统请手动安装Ollama / Please manually install Ollama on Windows"
            print_error "访问 https://ollama.ai/download 下载Windows版本 / Visit https://ollama.ai/download for Windows version"
            exit 1
            ;;
        *)
            print_error "不支持的操作系统 / Unsupported operating system"
            exit 1
            ;;
    esac
    
    # 验证安装 / Verify installation
    if check_ollama; then
        print_success "Ollama安装成功 / Ollama installed successfully"
    else
        print_error "Ollama安装失败 / Ollama installation failed"
        exit 1
    fi
}

# 检查Ollama服务 / Check Ollama service
check_ollama_service() {
    print_header "检查Ollama服务状态 / Checking Ollama service status..."
    
    if pgrep -x "ollama" > /dev/null; then
        print_success "Ollama服务正在运行 / Ollama service is running"
        return 0
    else
        print_warning "Ollama服务未运行 / Ollama service is not running"
        return 1
    fi
}

# 启动Ollama服务 / Start Ollama service
start_ollama_service() {
    print_header "启动Ollama服务 / Starting Ollama service..."
    
    case $OS in
        "macos"|"linux")
            # 在后台启动服务 / Start service in background
            nohup ollama serve > /dev/null 2>&1 &
            
            # 等待服务启动 / Wait for service to start
            sleep 3
            
            if check_ollama_service; then
                print_success "Ollama服务启动成功 / Ollama service started successfully"
            else
                print_error "Ollama服务启动失败 / Ollama service failed to start"
                exit 1
            fi
            ;;
        "windows")
            print_error "Windows系统请手动启动Ollama服务 / Please manually start Ollama service on Windows"
            print_error "在命令行中运行 / Run in command line: ollama serve"
            exit 1
            ;;
        *)
            print_error "不支持的操作系统 / Unsupported operating system"
            exit 1
            ;;
    esac
}

# 检查模型 / Check models
check_models() {
    print_header "检查已安装的模型 / Checking installed models..."
    
    if ! command -v ollama &> /dev/null; then
        print_error "Ollama未安装 / Ollama not installed"
        return 1
    fi
    
    MODELS=$(ollama list 2>/dev/null | tail -n +2 | awk '{print $1}' | grep -v "^$" || true)
    
    if [ -z "$MODELS" ]; then
        print_warning "没有找到已安装的模型 / No installed models found"
        return 1
    else
        print_success "找到已安装模型 / Found installed models:"
        echo "$MODELS" | while read -r model; do
            echo "  - $model"
        done
        return 0
    fi
}

# 安装推荐模型 / Install recommended models
install_recommended_models() {
    print_header "安装推荐模型 / Installing recommended models..."
    
    RECOMMENDED_MODELS=("qwen3:0.6b" "gemma3n:latest")
    SUCCESS_COUNT=0
    
    for model in "${RECOMMENDED_MODELS[@]}"; do
        print_info "正在安装模型 / Installing model: $model"
        
        if timeout 300 ollama pull "$model" 2>/dev/null; then
            print_success "模型安装成功 / Model installed successfully: $model"
            ((SUCCESS_COUNT++))
        else
            print_error "模型安装失败 / Model installation failed: $model"
        fi
    done
    
    if [ $SUCCESS_COUNT -gt 0 ]; then
        print_success "成功安装 $SUCCESS_COUNT 个模型 / Successfully installed $SUCCESS_COUNT models"
        return 0
    else
        print_error "没有成功安装任何模型 / No models installed successfully"
        return 1
    fi
}

# 创建配置文件 / Create configuration file
create_config_file() {
    print_header "创建配置文件 / Creating configuration file..."
    
    CONFIG_FILE="ollama_config.json"
    
    # 检查已安装的模型 / Check installed models
    MODELS=$(ollama list 2>/dev/null | tail -n +2 | awk '{print $1}' | grep -v "^$" || true)
    
    if [ -z "$MODELS" ]; then
        print_error "没有可用模型，无法创建配置文件 / No available models, cannot create config file"
        return 1
    fi
    
    # 选择默认模型 / Choose default model
    if echo "$MODELS" | grep -q "qwen3:0.6b"; then
        DEFAULT_MODEL="qwen3:0.6b"
    else
        DEFAULT_MODEL=$(echo "$MODELS" | head -n 1)
    fi
    
    # 创建配置文件 / Create configuration file
    cat > "$CONFIG_FILE" << EOF
{
  "default_model": "$DEFAULT_MODEL",
  "timeout": 60,
  "retry_attempts": 3,
  "setup_version": "1.0.0",
  "setup_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF
    
    if [ -f "$CONFIG_FILE" ]; then
        print_success "配置文件创建成功 / Configuration file created successfully: $CONFIG_FILE"
        print_info "默认模型 / Default model: $DEFAULT_MODEL"
        return 0
    else
        print_error "创建配置文件失败 / Failed to create configuration file"
        return 1
    fi
}

# 安装Python依赖 / Install Python dependencies
install_python_dependencies() {
    print_header "安装Python依赖 / Installing Python dependencies..."
    
    if [ -f "requirements.txt" ]; then
        print_info "从requirements.txt安装依赖 / Installing dependencies from requirements.txt..."
        
        if $PYTHON_CMD -m pip install -r requirements.txt; then
            print_success "Python依赖安装成功 / Python dependencies installed successfully"
            return 0
        else
            print_error "Python依赖安装失败 / Python dependencies installation failed"
            return 1
        fi
    else
        print_warning "没有找到requirements.txt文件 / requirements.txt file not found"
        return 1
    fi
}

# 测试设置 / Test setup
test_setup() {
    print_header "测试设置 / Testing setup..."
    
    # 测试Python导入 / Test Python import
    if $PYTHON_CMD -c "
import sys
sys.path.insert(0, '.')
try:
    from helper_functions import get_default_model, test_llm_connection
    print('✅ Python模块导入成功 / Python modules imported successfully')
    
    model = get_default_model()
    print(f'当前模型 / Current model: {model}')
    
    if test_llm_connection():
        print('✅ 连接测试成功 / Connection test successful')
        exit(0)
    else:
        print('❌ 连接测试失败 / Connection test failed')
        exit(1)
except Exception as e:
    print(f'❌ 测试失败 / Test failed: {e}')
    exit(1)
" 2>/dev/null; then
        print_success "设置测试成功 / Setup test successful"
        return 0
    else
        print_error "设置测试失败 / Setup test failed"
        return 1
    fi
}

# 主函数 / Main function
main() {
    echo
    print_header "====================================================================="
    print_header "AI Python课程快速设置脚本 / AI Python Course Quick Setup Script"
    print_header "====================================================================="
    echo
    
    # 检测操作系统 / Detect operating system
    detect_os
    
    # 检查Python版本 / Check Python version
    check_python
    
    # 检查Ollama安装 / Check Ollama installation
    if ! check_ollama; then
        install_ollama
    fi
    
    # 检查Ollama服务 / Check Ollama service
    if ! check_ollama_service; then
        start_ollama_service
    fi
    
    # 检查模型 / Check models
    if ! check_models; then
        install_recommended_models
    fi
    
    # 安装Python依赖 / Install Python dependencies
    install_python_dependencies
    
    # 创建配置文件 / Create configuration file
    create_config_file
    
    # 测试设置 / Test setup
    test_setup
    
    echo
    print_header "====================================================================="
    print_success "设置完成！/ Setup completed!"
    print_header "====================================================================="
    echo
    print_info "你现在可以开始使用AI Python课程了！"
    print_info "You can now start using the AI Python course!"
    echo
    print_info "运行以下命令开始第一课："
    print_info "Run the following command to start the first lesson:"
    print_info "cd C1L9 && jupyter notebook C1L9_Bilingual.ipynb"
    echo
}

# 运行主函数 / Run main function
main "$@"