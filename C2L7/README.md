# Lesson 7: Next course preview - working with files
# 第7课：下个课程预览 - 文件操作

## 项目简介 / Project Overview

本项目是AI Python初学者课程的第7课。你将在此了解如何在Python中读取文本文件，并运用LLM抽取关键信息。

This project is Lesson 7 of the AI Python for Beginners course. It shows how to read text files in Python and use an LLM to highlight key information.

## 文件结构 / File Structure
```
C2L7/
├── C2L7_Bilingual.ipynb    # 双语Jupyter notebook / Bilingual notebook
├── helper_functions.py      # 辅助函数 / Helper functions
├── requirements.txt         # 项目依赖 / Project dependencies
└── journal_entries/
    └── cape_town.txt        # 示例日记文本 / Sample journal text
```

## 环境配置 / Environment Setup
- 本项目使用base虚拟环境并依赖jupyter与ipython。
- 如需LLM响应，项目默认使用ollama后端 (gemma3n:latest)。

## 使用方法 / Usage
1. `pip install -r requirements.txt`
2. `jupyter notebook C2L7_Bilingual.ipynb`

## 数据文件 / Data File
`journal_entries/cape_town.txt` 包含了餐厅及其特色菜的描述，可在notebook中加载。
