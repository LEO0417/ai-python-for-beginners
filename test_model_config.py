#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模型配置测试脚本 / Model Configuration Test Script

这个脚本帮助你测试智能模型配置是否正常工作
This script helps you test if the smart model configuration is working properly
"""

import os
import sys
import subprocess

def test_ollama_installation():
    """测试ollama是否已安装 / Test if ollama is installed"""
    print("🔍 检查ollama安装状态 / Checking ollama installation...")
    try:
        result = subprocess.run(['which', 'ollama'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ ollama已安装 / ollama is installed")
            return True
        else:
            print("❌ ollama未安装 / ollama is not installed")
            print("请访问 https://ollama.ai 下载安装 / Please visit https://ollama.ai to download and install")
            return False
    except Exception as e:
        print(f"❌ 检查ollama时出错 / Error checking ollama: {e}")
        return False

def test_available_models():
    """测试可用的模型 / Test available models"""
    print("\n📋 检查可用模型 / Checking available models...")
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                print("✅ 发现以下模型 / Found the following models:")
                for line in lines[1:]:
                    if line.strip():
                        model_info = line.split()
                        if model_info:
                            print(f"   - {model_info[0]}")
                return lines[1:]
            else:
                print("❌ 没有找到任何模型 / No models found")
                print("请运行 'ollama pull gemma3n:latest' 下载模型 / Please run 'ollama pull gemma3n:latest' to download a model")
                return []
        else:
            print("❌ 无法获取模型列表 / Cannot get model list")
            return []
    except Exception as e:
        print(f"❌ 检查模型时出错 / Error checking models: {e}")
        return []

def test_environment_variable():
    """测试环境变量配置 / Test environment variable configuration"""
    print("\n🌍 检查环境变量配置 / Checking environment variable configuration...")
    env_model = os.getenv('OLLAMA_MODEL')
    if env_model:
        print(f"✅ 发现环境变量 OLLAMA_MODEL: {env_model}")
        print(f"✅ Found environment variable OLLAMA_MODEL: {env_model}")
        return env_model
    else:
        print("ℹ️  未设置环境变量 OLLAMA_MODEL / Environment variable OLLAMA_MODEL not set")
        print("   可以通过以下方式设置 / You can set it with:")
        print("   export OLLAMA_MODEL='your-model:latest'")
        return None

def test_helper_functions():
    """测试helper_functions的智能配置 / Test smart configuration in helper_functions"""
    print("\n🧪 测试helper_functions模块 / Testing helper_functions module...")
    
    try:
        # 测试导入helper_functions模块
        # Test importing helper_functions modules
        from helper_functions import get_default_model, set_default_model
        from helper_functions.model_config import show_model_info, get_available_models
        
        print("   ✅ helper_functions模块导入成功 / helper_functions modules imported successfully")
        
        # 测试get_default_model函数
        # Test get_default_model function
        model = get_default_model()
        print(f"   ✅ 默认模型 / Default model: {model}")
        
        # 测试获取可用模型
        # Test getting available models
        available_models = get_available_models()
        if available_models:
            print(f"   ✅ 可用模型 / Available models: {', '.join(available_models)}")
        else:
            print("   ⚠️  未检测到可用模型 / No available models detected")
        
        # 显示详细配置信息
        # Show detailed configuration info
        print("\n📋 详细配置信息 / Detailed Configuration Info:")
        show_model_info()
        
    except Exception as e:
        print(f"   ❌ 测试失败 / Test failed: {e}")

def test_model_response():
    """测试模型响应 / Test model response"""
    print("\n🤖 测试模型响应 / Testing model response...")
    
    # 使用helper_functions模块测试
    # Test using helper_functions module
    try:
        from helper_functions import get_llm_response
        from helper_functions.llm_utils import test_llm_connection
        
        print("   发送测试提示词 / Sending test prompt...")
        response = get_llm_response("Hello, please respond with 'Test successful'")
        
        if "test successful" in response.lower():
            print("   ✅ 模型响应测试成功 / Model response test successful")
        else:
            print("   ⚠️  收到响应但可能是备用响应 / Received response but might be fallback")
            print(f"   响应内容 / Response: {response[:100]}...")
        
        # 测试连接状态
        # Test connection status
        print("   测试LLM连接状态 / Testing LLM connection status...")
        is_connected = test_llm_connection()
        if is_connected:
            print("   ✅ LLM连接正常 / LLM connection is working")
        else:
            print("   ⚠️  LLM连接可能有问题，使用备用响应 / LLM connection might have issues, using fallback")
        
    except Exception as e:
        print(f"   ❌ 模型响应测试失败 / Model response test failed: {e}")

def main():
    """主测试函数 / Main test function"""
    print("🚀 AI Python双语课程 - 模型配置测试")
    print("🚀 AI Python Bilingual Course - Model Configuration Test")
    print("=" * 60)
    
    # 1. 测试ollama安装
    if not test_ollama_installation():
        return
    
    # 2. 测试可用模型
    models = test_available_models()
    if not models:
        return
    
    # 3. 测试环境变量
    test_environment_variable()
    
    # 4. 测试helper_functions模块
    test_helper_functions()
    
    # 5. 测试模型响应
    test_model_response()
    
    print("\n" + "=" * 60)
    print("🎉 测试完成 / Testing completed!")
    print("\n💡 使用建议 / Usage suggestions:")
    print("1. 设置环境变量: export OLLAMA_MODEL='your-model:latest'")
    print("2. 或在notebook中使用: set_default_model('your-model:latest')")
    print("3. 或让系统自动检测第一个可用模型")
    print("\n1. Set environment variable: export OLLAMA_MODEL='your-model:latest'")
    print("2. Or use in notebook: set_default_model('your-model:latest')")
    print("3. Or let system auto-detect first available model")

if __name__ == "__main__":
    main()