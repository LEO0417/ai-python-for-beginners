# C2L2: Repeating tasks with for loops / 第2课：使用for循环重复任务

## Overview / 概述

This lesson introduces the powerful concept of for loops in Python. Students will learn how to use for loops to automate repetitive tasks, especially when working with lists and AI language models. This builds directly on the previous lesson about lists and demonstrates how to eliminate repetitive code.

本课程介绍Python中for循环的强大概念。学生将学习如何使用for循环来自动化重复任务，特别是在处理列表和AI语言模型时。这直接建立在关于列表的上一课基础上，并演示如何消除重复代码。

## Learning Objectives / 学习目标

- Understand the concept and syntax of for loops
- Learn how to iterate through lists using for loops
- Practice using for loops with AI language models
- Understand the importance of proper indentation in Python
- Learn to collect results from loops into new lists
- Master the pattern of processing multiple items automatically

- 理解for循环的概念和语法
- 学习如何使用for循环遍历列表
- 练习将for循环与AI语言模型结合使用
- 理解Python中正确缩进的重要性
- 学习将循环结果收集到新列表中
- 掌握自动处理多个项目的模式

## Prerequisites / 先决条件

- Understanding of lists and list operations
- Basic Python syntax and variables
- Python 3.9+ installed
- Jupyter Notebook environment
- Completion of C2L1 (Lists lesson)

- 理解列表和列表操作
- 基本Python语法和变量
- 安装Python 3.9+
- Jupyter Notebook环境
- 完成C2L1（列表课程）

## Files / 文件

- `C2L2_Bilingual.ipynb` - Main lesson notebook with English and Chinese content / 包含英文和中文内容的主要课程笔记本
- `helper_functions.py` - Helper functions for AI integration / AI集成的辅助函数
- `requirements.txt` - Package dependencies / 包依赖项
- `README.md` - This file / 本文件

## How to Run / 如何运行

1. Ensure you have Python 3.9+ and Jupyter Notebook installed
2. Open the notebook file: `C2L2_Bilingual.ipynb`
3. Run each cell sequentially to follow along with the lesson
4. Pay special attention to indentation when writing for loops
5. Complete the exercises at the end to reinforce learning

1. 确保您已安装Python 3.9+和Jupyter Notebook
2. 打开笔记本文件：`C2L2_Bilingual.ipynb`
3. 按顺序运行每个单元格以跟随课程
4. 编写for循环时要特别注意缩进
5. 完成最后的练习以巩固学习

## Key Concepts Covered / 涵盖的关键概念

- **For Loops (for循环)**: Automated iteration through collections
- **Iteration (迭代)**: Processing each item in a sequence
- **Indentation (缩进)**: Critical Python syntax requirement
- **Loop Variables (循环变量)**: Temporary variables that change each iteration
- **Code Blocks (代码块)**: Indented code that executes in each loop iteration
- **List Accumulation (列表累积)**: Building new lists from loop results
- **AI Automation (AI自动化)**: Using loops to process multiple AI tasks

## Common Patterns / 常见模式

This lesson teaches several important programming patterns:

1. **Simple Iteration**: `for item in list:`
2. **Processing with AI**: Using `print_llm_response()` in loops
3. **Result Collection**: Using `append()` to build new lists
4. **String Formatting**: Using f-strings within loops

本课程教授几个重要的编程模式：

1. **简单迭代**：`for item in list:`
2. **AI处理**：在循环中使用`print_llm_response()`
3. **结果收集**：使用`append()`构建新列表
4. **字符串格式化**：在循环中使用f-strings

## Environment Setup / 环境设置

This notebook is configured to use the `base` virtual environment with integrated helper functions for AI functionality. The helper functions automatically handle LLM integration using Ollama with the default model.

此笔记本配置为使用`base`虚拟环境，并集成了AI功能的辅助函数。辅助函数自动使用Ollama和默认模型处理LLM集成。

## Common Errors to Avoid / 要避免的常见错误

- **Indentation Errors**: Make sure to indent code inside the for loop
- **Missing Colons**: Don't forget the `:` at the end of the for statement
- **Variable Naming**: Use descriptive names for loop variables
- **List Modification**: Be careful when modifying lists during iteration

- **缩进错误**：确保缩进for循环内的代码
- **缺少冒号**：不要忘记for语句末尾的`:`
- **变量命名**：为循环变量使用描述性名称
- **列表修改**：在迭代过程中修改列表时要小心

## Next Steps / 后续步骤

After completing this lesson, you'll be ready to learn about dictionaries, which provide even more powerful ways to organize and process data with AI.

完成本课程后，您将准备好学习字典，这提供了更强大的方式来组织和处理AI数据。
EOF < /dev/null