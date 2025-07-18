# -*- coding: utf-8 -*-
"""
课程级helper_functions模块
Lesson-level helper_functions module

这个文件自动导入项目根目录的helper_functions包，
保持与吴恩达课程的兼容性
This file automatically imports the helper_functions package from project root,
maintaining compatibility with Andrew Ng's courses
"""

import os
import sys

# 添加项目根目录到Python路径
# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 从根目录的helper_functions包导入所有功能
# Import all functionality from root helper_functions package
try:
    # 直接导入根目录的模块，避免循环导入
    # Directly import root modules to avoid circular imports
    import importlib.util
    import sys
    
    # 导入model_config模块
    spec = importlib.util.spec_from_file_location("model_config", os.path.join(project_root, "helper_functions", "model_config.py"))
    model_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(model_config)
    
    # 导入llm_utils模块
    spec = importlib.util.spec_from_file_location("llm_utils", os.path.join(project_root, "helper_functions", "llm_utils.py"))
    llm_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(llm_utils)
    
    # 导入common_utils模块
    spec = importlib.util.spec_from_file_location("common_utils", os.path.join(project_root, "helper_functions", "common_utils.py"))
    common_utils = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(common_utils)
    
    # 导出常用函数
    # Export common functions
    print_llm_response = llm_utils.print_llm_response
    get_llm_response = llm_utils.get_llm_response
    get_default_model = model_config.get_default_model
    set_default_model = model_config.set_default_model
    
except ImportError as e:
    print(f"⚠️  导入helper_functions包时出现问题 / Issue importing helper_functions package: {e}")
    print("请确保项目根目录的helper_functions包存在 / Please ensure helper_functions package exists in project root")