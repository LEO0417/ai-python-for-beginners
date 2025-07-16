# 更新日志 / Changelog

本文件记录了AI Python双语课程项目的所有重要更改。

All notable changes to the AI Python Bilingual Course project will be documented in this file.

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [未发布] / [Unreleased]

### 新增 / Added
- 项目开源文件结构 / Open source project file structure
- 完整的README文档 / Complete README documentation
- 贡献指南和行为准则 / Contributing guidelines and code of conduct
- 智能模型配置机制 / Smart model configuration mechanism
- 环境变量支持 (OLLAMA_MODEL) / Environment variable support (OLLAMA_MODEL)
- 自动模型检测功能 / Automatic model detection feature
- 配置文件支持 (ollama_config.json) / Configuration file support (ollama_config.json)
- 统一的helper_functions包 / Unified helper_functions package
- 模块化的代码结构 / Modular code structure

### 改进 / Improved
- 模型配置从硬编码改为智能选择 / Model configuration changed from hardcoded to smart selection
- 用户可以更灵活地自定义模型 / Users can customize models more flexibly
- 支持多种模型配置方式 / Support multiple model configuration methods
- 消除了90%的重复代码 / Eliminated 90% of duplicate code
- 统一的辅助函数管理 / Unified helper function management
- 保持与吴恩达课程的兼容性 / Maintained compatibility with Andrew Ng's courses

### 重构 / Refactored
- 将分散的helper_functions.py文件合并为统一的包 / Merged scattered helper_functions.py files into unified package
- 创建模块化的代码结构 (llm_utils, model_config, common_utils) / Created modular code structure
- 自动路径处理，支持从任意课程导入 / Automatic path handling for imports from any lesson

## [1.0.0] - 2025-01-15

### 新增 / Added
- **C1L6**: Python基础语法和数据类型课程 / Basic Python syntax and data types lesson
- **C1L7**: 控制流程和循环课程 / Control flow and loops lesson
- **C1L9**: 数据结构和文件操作课程 / Data structures and file operations lesson
- **C1L10**: 错误处理和调试课程 / Error handling and debugging lesson
- **C3L6**: 函数定义和重用课程 / Function definition and reuse lesson
- 双语Jupyter notebook支持 / Bilingual Jupyter notebook support
- ollama LLM集成 / ollama LLM integration
- 完整的项目结构和辅助函数 / Complete project structure and helper functions
- 每课程独立的README文档 / Independent README documentation for each lesson

### 特性 / Features
- 中英文对照教学内容 / Chinese-English parallel teaching content
- 实践导向的学习方法 / Practice-oriented learning approach
- AI集成的编程练习 / AI-integrated programming exercises
- 渐进式课程设计 / Progressive course design

---

## 版本说明 / Version Notes

### 版本命名规则 / Version Naming Convention
- **主版本号** / **Major**: 不兼容的API修改 / Incompatible API changes
- **次版本号** / **Minor**: 向下兼容的功能性新增 / Backwards compatible functionality additions
- **修订号** / **Patch**: 向下兼容的问题修正 / Backwards compatible bug fixes

### 更改类型 / Types of Changes
- **新增** / **Added**: 新功能 / New features
- **更改** / **Changed**: 对现有功能的更改 / Changes to existing functionality
- **弃用** / **Deprecated**: 即将移除的功能 / Soon-to-be removed features
- **移除** / **Removed**: 已移除的功能 / Removed features
- **修复** / **Fixed**: 任何bug修复 / Any bug fixes
- **安全** / **Security**: 安全相关的修复 / Security related fixes