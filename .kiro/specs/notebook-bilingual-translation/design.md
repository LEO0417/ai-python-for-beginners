# Design Document

## Overview

本系统设计为一个可重复执行的任务，能够处理raw notebook文件夹中的Jupyter notebook文件，生成双语版本并创建完整的项目结构。系统采用批量处理模式，一次性处理多个notebook文件，同时优化helper_functions包以支持所有课程需求。原始文件将被保留以供参考和备份。

## 工作流程

### 任务执行流程
每次执行任务时，AI助手将完成以下步骤：

1. **需求分析**：分析所有raw notebook文件的结构和内容，识别共同需求
2. **包优化**：优化helper_functions包，添加缺失的函数（如read_journal, display_html）
3. **批量处理**：逐个处理notebook文件，创建双语版本
4. **内容解析**：解析notebook结构，识别需要翻译的markdown单元格和代码注释
5. **双语翻译**：将英文内容翻译为中文，创建双语格式（英文+中文）
6. **项目创建**：创建对应的项目文件夹和相关文件
7. **环境配置**：设置notebook使用base虚拟环境，如果涉及LLM调用则配置ollama后端和gemma3n:latest模型
8. **包结构创建**：在每个课程文件夹中创建代理文件，指向根目录的helper_functions包
9. **文件保留**：保留原始文件以供参考和备份

### 输出结构
每个处理完的notebook将生成：
- `{notebook_name}/` - 项目文件夹（如C2L1, C2L2等，与原notebook文件名对应）
- `{notebook_name}/{notebook_name}_Bilingual.ipynb` - 双语notebook
- `{notebook_name}/helper_functions.py` - 辅助函数代理文件（导入根目录的helper_functions包）
- `{notebook_name}/requirements.txt` - 依赖文件，包含详细的中英文说明
- `{notebook_name}/README.md` - 详细的项目说明文档，包含学习目标、先决条件、使用方法等
- 其他必要的数据文件（如journal_entries/文件夹）

### 项目级结构
项目根目录将包含：
- `helper_functions/` - 统一的辅助函数包
  - `__init__.py` - 包初始化文件，包含所有函数的导出
  - `model_config.py` - 智能模型配置管理
  - `llm_utils.py` - LLM调用功能
  - `common_utils.py` - 通用工具函数（包含read_journal, display_html等）
- `raw notebook/` - 原始notebook文件（保留不删除）
- `C2L1/`, `C2L2/`, ..., `C2L7/` - 各课程文件夹
- `ollama_config.json.example` - 全局配置示例
- `test_model_config.py` - 配置测试脚本

### 翻译原则
- 保持原文完整性，在英文下方添加中文翻译
- 技术术语保持一致性
- 代码逻辑不变，仅翻译注释和字符串
- 练习题提供中文说明
- 创建完整的双语notebook，而非修改原始文件

### 技术架构

#### 代理文件模式
为避免代码重复，采用代理文件模式：
- 每个课程文件夹包含一个helper_functions.py代理文件
- 代理文件通过动态导入指向根目录的helper_functions包
- 确保代码一致性和可维护性

#### helper_functions包优化
根据实际需求优化了helper_functions包：
- 添加了read_journal()函数，支持灵活的文件路径查找
- 添加了display_html()函数，支持Jupyter notebook中的HTML显示
- 完善了__init__.py，确保所有函数正确导出
- 保持向后兼容性

#### 文件处理策略
- 批量处理：一次性处理多个notebook文件
- 非破坏性：保留原始文件
- 增量式：可以重复执行而不会产生冲突
- 模块化：每个课程独立成文件夹

### 质量保证
- 每个课程文件夹包含详细的README.md文档
- 提供完整的依赖项说明
- 包含使用指南和环境设置说明
- 支持多语言（中英文）文档