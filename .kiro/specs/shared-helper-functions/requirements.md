# Requirements Document

## Introduction

本功能旨在重构当前项目中重复的helper_functions.py文件，创建一个统一的共享模块，让所有课程都可以导入和使用相同的辅助函数。这将减少代码重复，提高维护性，并确保所有课程使用一致的功能。

## Requirements

### Requirement 1

**User Story:** 作为开发者，我希望创建一个统一的共享辅助函数模块，以便所有课程都可以使用相同的功能而不需要重复代码。

#### Acceptance Criteria

1. WHEN 创建共享模块 THEN 系统 SHALL 在项目根目录创建shared_utils包
2. WHEN 移动通用函数 THEN 系统 SHALL 将所有通用的辅助函数移动到共享模块中
3. WHEN 保持功能一致性 THEN 系统 SHALL 确保所有课程的功能保持不变
4. WHEN 更新导入语句 THEN 系统 SHALL 修改所有notebook和helper文件的导入语句

### Requirement 2

**User Story:** 作为开发者，我希望保持智能模型配置功能，以便用户仍然可以灵活地配置ollama模型。

#### Acceptance Criteria

1. WHEN 迁移模型配置 THEN 系统 SHALL 将智能模型配置功能移动到共享模块
2. WHEN 保持配置优先级 THEN 系统 SHALL 维持环境变量、配置文件、自动检测的优先级顺序
3. WHEN 支持全局配置 THEN 系统 SHALL 允许在项目根目录设置全局模型配置
4. WHEN 支持局部配置 THEN 系统 SHALL 允许各课程覆盖全局配置

### Requirement 3

**User Story:** 作为开发者，我希望简化项目结构，以便更容易维护和扩展功能。

#### Acceptance Criteria

1. WHEN 清理重复文件 THEN 系统 SHALL 删除各课程中重复的helper_functions.py文件
2. WHEN 保留课程特定功能 THEN 系统 SHALL 保留各课程特有的辅助函数（如果有）
3. WHEN 更新文档 THEN 系统 SHALL 更新所有相关的README和文档
4. WHEN 更新测试脚本 THEN 系统 SHALL 修改test_model_config.py以适应新结构

### Requirement 4

**User Story:** 作为用户，我希望导入和使用辅助函数更加简单直观，以便更好地学习和使用。

#### Acceptance Criteria

1. WHEN 简化导入语句 THEN 系统 SHALL 提供简洁的导入方式
2. WHEN 保持向后兼容 THEN 系统 SHALL 确保现有的使用方式仍然有效
3. WHEN 提供使用示例 THEN 系统 SHALL 在文档中提供清晰的使用示例
4. WHEN 处理路径问题 THEN 系统 SHALL 自动处理不同课程的相对路径问题

### Requirement 5

**User Story:** 作为维护者，我希望新的结构更容易扩展和维护，以便未来添加新功能或修复问题。

#### Acceptance Criteria

1. WHEN 添加新功能 THEN 系统 SHALL 支持在共享模块中轻松添加新的辅助函数
2. WHEN 修复问题 THEN 系统 SHALL 确保修复一次即可影响所有课程
3. WHEN 版本管理 THEN 系统 SHALL 支持共享模块的版本管理
4. WHEN 模块化设计 THEN 系统 SHALL 将不同功能分离到不同的模块文件中