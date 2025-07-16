# Design Document

## Overview

本系统设计为一个可重复执行的任务，能够处理raw notebook文件夹中的单个Jupyter notebook文件，生成双语版本并创建完整的项目结构。每次执行任务时，处理一个notebook文件，完成从翻译到项目创建的全部工作流程。

## 工作流程

### 任务执行流程
每次执行任务时，AI助手将完成以下步骤：

1. **文件选择**：从raw notebook文件夹中选择一个未处理的.ipynb文件
2. **内容解析**：解析notebook结构，识别需要翻译的markdown单元格和代码注释
3. **双语翻译**：将英文内容翻译为中文，创建双语格式（英文+中文）
4. **函数分析**：识别notebook中引用但缺失的函数，推断其功能并实现
5. **项目创建**：创建对应的项目文件夹和相关文件
6. **环境配置**：设置notebook使用base虚拟环境，如果涉及LLM调用则配置ollama后端和gemma3n:latest模型
7. **包结构创建**：确保项目根目录的helper_functions包存在，并在课程文件夹中创建代理文件
7. **文件清理**：删除原始文件

### 输出结构
每个处理完的notebook将生成：
- `{notebook_name}/` - 项目文件夹（如C1L6, C1L7等，与原notebook文件名对应）
- `{notebook_name}/{notebook_name}_Bilingual.ipynb` - 双语notebook
- `{notebook_name}/helper_functions.py` - 辅助函数代理文件（导入根目录的helper_functions包）
- `{notebook_name}/requirements.txt` - 依赖文件
- `{notebook_name}/README.md` - 项目说明
- 其他必要的数据文件

### 项目级结构
项目根目录将包含：
- `helper_functions/` - 统一的辅助函数包
  - `__init__.py` - 包初始化文件
  - `model_config.py` - 智能模型配置管理
  - `llm_utils.py` - LLM调用功能
  - `common_utils.py` - 通用工具函数
- `ollama_config.json.example` - 全局配置示例
- `test_model_config.py` - 配置测试脚本

### 翻译原则
- 保持原文完整性，在英文下方添加中文翻译
- 技术术语保持一致性
- 代码逻辑不变，仅翻译注释和字符串
- 练习题提供中文说明