# -*- coding: utf-8 -*-
"""
模型配置管理模块
Model Configuration Management Module

提供智能的ollama模型配置和管理功能
Provides intelligent ollama model configuration and management
"""

import os
import json
import subprocess

def get_default_model():
    """
    智能获取默认模型，按优先级顺序：
    1. 环境变量 OLLAMA_MODEL
    2. 课程级配置文件 {lesson}/ollama_config.json
    3. 全局配置文件 ollama_config.json
    4. 自动检测第一个可用模型
    5. 回退到预设默认值
    
    Smart default model detection with priority order:
    1. Environment variable OLLAMA_MODEL
    2. Lesson-level config file {lesson}/ollama_config.json
    3. Global config file ollama_config.json
    4. Auto-detect first available model
    5. Fallback to preset default
    
    Returns:
        str: 模型名称 / Model name
    """
    
    # 1. 检查环境变量 / Check environment variable
    env_model = os.getenv('OLLAMA_MODEL')
    if env_model:
        return env_model
    
    # 2. 检查课程级配置文件 / Check lesson-level config file
    lesson_config_model = _get_lesson_config_model()
    if lesson_config_model:
        return lesson_config_model
    
    # 3. 检查全局配置文件 / Check global config file
    global_config_model = _get_global_config_model()
    if global_config_model:
        return global_config_model
    
    # 4. 自动检测可用模型 / Auto-detect available models
    available_model = _get_first_available_model()
    if available_model:
        return available_model
    
    # 5. 回退到默认值 / Fallback to default
    return "gemma3n:latest"

def _get_lesson_config_model():
    """从课程级配置文件读取模型设置 / Read model setting from lesson-level config file"""
    try:
        # 尝试找到当前课程的配置文件
        # Try to find current lesson's config file
        current_dir = os.getcwd()
        lesson_config_file = os.path.join(current_dir, 'ollama_config.json')
        
        if os.path.exists(lesson_config_file):
            with open(lesson_config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('default_model')
    except Exception:
        pass
    return None

def _get_global_config_model():
    """从全局配置文件读取模型设置 / Read model setting from global config file"""
    try:
        # 查找项目根目录的配置文件
        # Look for config file in project root
        project_root = _get_project_root()
        global_config_file = os.path.join(project_root, 'ollama_config.json')
        
        if os.path.exists(global_config_file):
            with open(global_config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get('default_model')
    except Exception:
        pass
    return None

def _get_first_available_model():
    """自动检测第一个可用的ollama模型 / Auto-detect first available ollama model"""
    try:
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            # 跳过标题行，获取第一个模型
            # Skip header line, get first model
            for line in lines[1:]:
                if line.strip():
                    model_name = line.split()[0]  # 获取模型名称
                    if model_name and ':' in model_name:
                        return model_name
    except Exception:
        pass
    return None

def _get_project_root():
    """获取项目根目录 / Get project root directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(current_dir)

def set_default_model(model_name, scope='global'):
    """
    设置默认模型到配置文件
    Set default model to config file
    
    Args:
        model_name (str): 模型名称 / Model name
        scope (str): 配置范围 'global' 或 'lesson' / Configuration scope 'global' or 'lesson'
    """
    try:
        if scope == 'lesson':
            # 设置课程级配置 / Set lesson-level config
            config_file = os.path.join(os.getcwd(), 'ollama_config.json')
        else:
            # 设置全局配置 / Set global config
            project_root = _get_project_root()
            config_file = os.path.join(project_root, 'ollama_config.json')
        
        config = {}
        
        # 读取现有配置 / Read existing config
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            except Exception:
                pass
        
        # 更新配置 / Update config
        config['default_model'] = model_name
        
        # 保存配置 / Save config
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        scope_text = "全局" if scope == 'global' else "课程级"
        print(f"✅ {scope_text}默认模型已设置为: {model_name}")
        print(f"✅ {scope.title()} default model set to: {model_name}")
        
    except Exception as e:
        print(f"❌ 保存配置失败 / Failed to save config: {e}")

def get_available_models():
    """
    获取所有可用的ollama模型列表
    Get list of all available ollama models
    
    Returns:
        list: 可用模型列表 / List of available models
    """
    try:
        result = subprocess.run(['ollama', 'list'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            models = []
            for line in lines[1:]:  # 跳过标题行
                if line.strip():
                    model_info = line.split()
                    if model_info and ':' in model_info[0]:
                        models.append(model_info[0])
            return models
    except Exception:
        pass
    return []

def show_model_info():
    """显示当前模型配置信息 / Show current model configuration info"""
    print("🔍 当前模型配置信息 / Current Model Configuration Info")
    print("=" * 50)
    
    # 显示当前使用的模型
    current_model = get_default_model()
    print(f"📍 当前使用模型 / Current model: {current_model}")
    
    # 显示配置来源
    env_model = os.getenv('OLLAMA_MODEL')
    if env_model:
        print(f"🌍 环境变量 / Environment variable: {env_model}")
    
    lesson_model = _get_lesson_config_model()
    if lesson_model:
        print(f"📁 课程级配置 / Lesson config: {lesson_model}")
    
    global_model = _get_global_config_model()
    if global_model:
        print(f"🌐 全局配置 / Global config: {global_model}")
    
    # 显示可用模型
    available_models = get_available_models()
    if available_models:
        print(f"📋 可用模型 / Available models: {', '.join(available_models)}")
    else:
        print("⚠️  未检测到可用模型 / No available models detected")
    
    print("=" * 50)