# C2L3: Prioritizing tasks with dictionaries and AI / 第3课：使用字典和AI优先排序任务

## Overview / 概述

This lesson introduces dictionaries, one of Python's most powerful data structures. Students will learn how to use dictionaries to store key-value pairs and organize data more efficiently than with lists. The lesson demonstrates practical applications of dictionaries for task prioritization and AI automation.

本课程介绍字典，这是Python最强大的数据结构之一。学生将学习如何使用字典来存储键值对，并比使用列表更有效地组织数据。本课程演示了字典在任务优先级排序和AI自动化中的实际应用。

## Learning Objectives / 学习目标

- Understand what dictionaries are and how they differ from lists
- Learn dictionary syntax and key-value pair concepts
- Practice accessing, adding, and updating dictionary elements
- Store different data types in dictionaries (strings, numbers, lists)
- Use dictionaries to organize and prioritize tasks
- Combine dictionaries with for loops and AI for automation

- 理解字典是什么以及它们与列表的区别
- 学习字典语法和键值对概念
- 练习访问、添加和更新字典元素
- 在字典中存储不同数据类型（字符串、数字、列表）
- 使用字典来组织和优先排序任务
- 将字典与for循环和AI结合用于自动化

## Prerequisites / 先决条件

- Understanding of lists and for loops
- Basic Python syntax and variables
- Python 3.9+ installed
- Jupyter Notebook environment
- Completion of C2L1 (Lists) and C2L2 (For loops)

- 理解列表和for循环
- 基本Python语法和变量
- 安装Python 3.9+
- Jupyter Notebook环境
- 完成C2L1（列表）和C2L2（for循环）

## Files / 文件

- `C2L3_Bilingual.ipynb` - Main lesson notebook with English and Chinese content / 包含英文和中文内容的主要课程笔记本
- `helper_functions.py` - Helper functions for AI integration / AI集成的辅助函数
- `requirements.txt` - Package dependencies / 包依赖项
- `README.md` - This file / 本文件

## How to Run / 如何运行

1. Ensure you have Python 3.9+ and Jupyter Notebook installed
2. Open the notebook file: `C2L3_Bilingual.ipynb`
3. Run each cell sequentially to follow along with the lesson
4. Pay attention to the key-value pair syntax in dictionaries
5. Complete the exercises at the end to reinforce learning

1. 确保您已安装Python 3.9+和Jupyter Notebook
2. 打开笔记本文件：`C2L3_Bilingual.ipynb`
3. 按顺序运行每个单元格以跟随课程
4. 注意字典中的键值对语法
5. 完成最后的练习以巩固学习

## Key Concepts Covered / 涵盖的关键概念

- **Dictionaries (字典)**: Key-value pair data structures
- **Keys (键)**: Unique identifiers for dictionary values
- **Values (值)**: Data associated with keys
- **Dictionary Access (字典访问)**: Using keys to retrieve values
- **Dictionary Methods (字典方法)**: `.keys()`, `.values()`, element assignment
- **Mixed Data Types (混合数据类型)**: Storing different types in dictionaries
- **Task Prioritization (任务优先级)**: Using dictionaries for organization
- **AI Integration (AI集成)**: Combining dictionaries with AI tasks

## Dictionary vs List Comparison / 字典与列表比较

| Feature | Lists | Dictionaries |
|---------|--------|-------------|
| Access Method | Index (0, 1, 2...) | Key ("name", "age"...) |
| Ordering | Ordered | Ordered (Python 3.7+) |
| Duplicates | Allowed | Keys must be unique |
| Use Case | Sequential data | Labeled data |

| 特性 | 列表 | 字典 |
|------|------|------|
| 访问方式 | 索引 (0, 1, 2...) | 键 ("name", "age"...) |
| 排序 | 有序 | 有序 (Python 3.7+) |
| 重复 | 允许 | 键必须唯一 |
| 使用场景 | 顺序数据 | 标签数据 |

## Environment Setup / 环境设置

This notebook is configured to use the `base` virtual environment with integrated helper functions for AI functionality. The helper functions automatically handle LLM integration using Ollama with the default model.

此笔记本配置为使用`base`虚拟环境，并集成了AI功能的辅助函数。辅助函数自动使用Ollama和默认模型处理LLM集成。

## Common Patterns / 常见模式

This lesson teaches several important programming patterns:

1. **Dictionary Creation**: `{key: value, key2: value2}`
2. **Element Access**: `dict[key]`
3. **Element Assignment**: `dict[key] = value`
4. **Iteration**: `for key in dict:` or `for task in dict[key]:`
5. **Nested Data**: Dictionaries containing lists

本课程教授几个重要的编程模式：

1. **字典创建**：`{key: value, key2: value2}`
2. **元素访问**：`dict[key]`
3. **元素赋值**：`dict[key] = value`
4. **迭代**：`for key in dict:` 或 `for task in dict[key]:`
5. **嵌套数据**：包含列表的字典

## Real-World Applications / 实际应用

- Task management and prioritization
- User profile storage
- Configuration settings
- Data organization and retrieval
- AI prompt customization

- 任务管理和优先级排序
- 用户配置文件存储
- 配置设置
- 数据组织和检索
- AI提示自定义

## Next Steps / 后续步骤

After completing this lesson, you'll be ready to learn about more advanced dictionary operations and how to create custom recipes using dictionaries with AI.

完成本课程后，您将准备好学习更高级的字典操作，以及如何使用字典和AI创建自定义配方。
EOF < /dev/null