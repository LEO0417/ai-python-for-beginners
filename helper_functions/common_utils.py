# -*- coding: utf-8 -*-
"""
通用工具模块
Common Utilities Module

提供通用的辅助函数和工具
Provides common helper functions and utilities
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, List, Optional, Union

def read_text_file(file_path: str, encoding: str = 'utf-8') -> str:
    """
    读取文本文件
    Read text file
    
    Args:
        file_path (str): 文件路径 / File path
        encoding (str): 文件编码 / File encoding
        
    Returns:
        str: 文件内容 / File content
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    except Exception as e:
        print(f"❌ 读取文件失败 / Failed to read file {file_path}: {e}")
        return ""

def write_text_file(file_path: str, content: str, encoding: str = 'utf-8') -> bool:
    """
    写入文本文件
    Write text file
    
    Args:
        file_path (str): 文件路径 / File path
        content (str): 文件内容 / File content
        encoding (str): 文件编码 / File encoding
        
    Returns:
        bool: 是否成功 / Whether successful
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ 写入文件失败 / Failed to write file {file_path}: {e}")
        return False

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    加载JSON文件
    Load JSON file
    
    Args:
        file_path (str): 文件路径 / File path
        
    Returns:
        dict: JSON数据 / JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ 加载JSON文件失败 / Failed to load JSON file {file_path}: {e}")
        return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """
    保存JSON文件
    Save JSON file
    
    Args:
        file_path (str): 文件路径 / File path
        data (dict): 要保存的数据 / Data to save
        
    Returns:
        bool: 是否成功 / Whether successful
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ 保存JSON文件失败 / Failed to save JSON file {file_path}: {e}")
        return False

def get_project_info() -> Dict[str, Any]:
    """
    获取项目信息
    Get project information
    
    Returns:
        dict: 项目信息 / Project information
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    info = {
        'project_root': project_root,
        'current_dir': os.getcwd(),
        'python_path': os.sys.path,
        'timestamp': datetime.now().isoformat()
    }
    
    # 尝试读取项目配置
    try:
        readme_path = os.path.join(project_root, 'README.md')
        if os.path.exists(readme_path):
            info['has_readme'] = True
        
        config_path = os.path.join(project_root, 'ollama_config.json')
        if os.path.exists(config_path):
            info['has_global_config'] = True
            info['global_config'] = load_json_file(config_path)
    except Exception:
        pass
    
    return info

def list_lessons() -> List[str]:
    """
    列出所有课程文件夹
    List all lesson folders
    
    Returns:
        list: 课程列表 / List of lessons
    """
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lessons = []
    
    try:
        for item in os.listdir(project_root):
            item_path = os.path.join(project_root, item)
            if os.path.isdir(item_path) and (item.startswith('C') and 'L' in item):
                lessons.append(item)
        
        lessons.sort()  # 按字母顺序排序
    except Exception as e:
        print(f"❌ 列出课程失败 / Failed to list lessons: {e}")
    
    return lessons

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    摄氏度转华氏度
    Convert Celsius to Fahrenheit
    
    Args:
        celsius (float): 摄氏度 / Celsius temperature
        
    Returns:
        float: 华氏度 / Fahrenheit temperature
    """
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    华氏度转摄氏度
    Convert Fahrenheit to Celsius
    
    Args:
        fahrenheit (float): 华氏度 / Fahrenheit temperature
        
    Returns:
        float: 摄氏度 / Celsius temperature
    """
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters: float) -> float:
    """
    米转英尺
    Convert meters to feet
    
    Args:
        meters (float): 米 / Meters
        
    Returns:
        float: 英尺 / Feet
    """
    return meters * 3.28084

def feet_to_meters(feet: float) -> float:
    """
    英尺转米
    Convert feet to meters
    
    Args:
        feet (float): 英尺 / Feet
        
    Returns:
        float: 米 / Meters
    """
    return feet / 3.28084

def format_file_size(size_bytes: int) -> str:
    """
    格式化文件大小
    Format file size
    
    Args:
        size_bytes (int): 字节数 / Size in bytes
        
    Returns:
        str: 格式化的大小 / Formatted size
    """
    if size_bytes == 0:
        return "0B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    
    return f"{size_bytes:.1f}{size_names[i]}"

def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    获取文件信息
    Get file information
    
    Args:
        file_path (str): 文件路径 / File path
        
    Returns:
        dict: 文件信息 / File information
    """
    try:
        stat = os.stat(file_path)
        return {
            'path': file_path,
            'size': stat.st_size,
            'size_formatted': format_file_size(stat.st_size),
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'exists': True
        }
    except Exception as e:
        return {
            'path': file_path,
            'error': str(e),
            'exists': False
        }

def read_journal(filename: str) -> str:
    """
    读取日志文件
    Read journal file
    
    Args:
        filename (str): 日志文件名 / Journal filename
        
    Returns:
        str: 日志内容 / Journal content
    """
    try:
        # 首先尝试相对路径
        # First try relative path
        if os.path.exists(filename):
            return read_text_file(filename)
        
        # 如果不存在，尝试在journal_entries目录中查找
        # If not found, try to find in journal_entries directory
        journal_path = os.path.join("journal_entries", filename)
        if os.path.exists(journal_path):
            return read_text_file(journal_path)
        
        # 如果还是找不到，尝试在当前目录查找
        # If still not found, try in current directory
        current_dir = os.getcwd()
        full_path = os.path.join(current_dir, filename)
        if os.path.exists(full_path):
            return read_text_file(full_path)
        
        # 最后尝试在项目根目录查找
        # Finally try in project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        root_path = os.path.join(project_root, filename)
        if os.path.exists(root_path):
            return read_text_file(root_path)
            
        return f"Journal file '{filename}' not found. Please ensure the file exists in the current directory or journal_entries folder."
        
    except Exception as e:
        return f"Error reading journal file '{filename}': {e}"

def display_html(html_content: str) -> None:
    """
    在Jupyter notebook中显示HTML内容
    Display HTML content in Jupyter notebook
    
    Args:
        html_content (str): HTML内容 / HTML content
    """
    try:
        # 尝试导入IPython显示模块
        # Try to import IPython display module
        from IPython.display import HTML, display
        display(HTML(html_content))
    except ImportError:
        # 如果不在Jupyter环境中，打印HTML内容
        # If not in Jupyter environment, print HTML content
        print("HTML Content:")
        print("=" * 50)
        print(html_content)
        print("=" * 50)
        print("Note: For proper HTML rendering, please run this in a Jupyter notebook environment.")
    except Exception as e:
        print(f"Error displaying HTML: {e}")
        print("HTML Content:")
        print("=" * 50)
        print(html_content)
        print("=" * 50)