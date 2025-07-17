# -*- coding: utf-8 -*-
"""
AI Python双语课程 - 共享工具包
AI Python Bilingual Course - Shared Utilities Package

这个包提供了所有课程共用的辅助函数和工具
This package provides shared helper functions and utilities for all lessons
"""

import os
import sys

# 自动添加项目根目录到Python路径
# Automatically add project root to Python path
def _setup_path():
    """设置Python路径以支持从任意位置导入 / Setup Python path for imports from any location"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

_setup_path()

# 导入所有常用函数 / Import all common functions
try:
    from .model_config import get_default_model, set_default_model
    from .llm_utils import print_llm_response, get_llm_response
    from .common_utils import *
    
    # 提供向后兼容的接口 / Provide backward compatibility interface
    __all__ = [
        'get_default_model',
        'set_default_model',
        'print_llm_response',
        'get_llm_response',
        'read_journal'
    ]
    
except ImportError as e:
    # 如果导入失败，提供友好的错误信息
    # If import fails, provide friendly error message
    print(f"⚠️  导入共享工具包时出现问题 / Issue importing shared utilities: {e}")
    print("请确保所有模块文件都已正确创建 / Please ensure all module files are properly created")

# 版本信息 / Version information
__version__ = "1.0.0"
__author__ = "AI Python Bilingual Course Team"

# 使用说明 / Usage instructions
def show_usage():
    """显示使用说明 / Show usage instructions"""
    print("""
🚀 AI Python双语课程 - 共享工具包使用说明
🚀 AI Python Bilingual Course - Shared Utilities Usage

基本使用 / Basic Usage:
    from shared_utils import print_llm_response, get_llm_response
    from shared_utils import get_default_model, set_default_model

模型配置 / Model Configuration:
    # 检查当前模型 / Check current model
    print(get_default_model())
    
    # 设置默认模型 / Set default model
    set_default_model("llama2:latest")

LLM调用 / LLM Calls:
    # 打印响应 / Print response
    print_llm_response("Hello, how are you?")
    
    # 获取响应 / Get response
    response = get_llm_response("What is Python?")

环境变量配置 / Environment Variable Configuration:
    export OLLAMA_MODEL="your-model:latest"

更多信息请查看项目文档 / For more information, see project documentation
    """)

# 便捷函数 / Convenience functions
def version():
    """返回版本信息 / Return version information"""
    return __version__

def help():
    """显示帮助信息 / Show help information"""
    show_usage()