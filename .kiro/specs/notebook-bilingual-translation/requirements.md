# Requirements Document

## Introduction

本功能旨在创建一个可重复执行的任务，能够处理raw notebook文件夹中的Jupyter notebook文件，将其翻译成双语版本（英文+中文），并创建完整的项目结构。每个notebook将被组织到独立的文件夹中，使用ollama作为大模型后端，并配置为使用base虚拟环境。

## Requirements

### Requirement 1

**User Story:** 作为开发者，我希望将raw notebook中的notebook翻译成双语版本，以便中文用户能够更好地理解内容。

#### Acceptance Criteria

1. WHEN 处理notebook文件 THEN 系统 SHALL 创建包含英文和中文内容的双语版本
2. WHEN 翻译markdown单元格 THEN 系统 SHALL 保持原有英文内容并在下方添加中文翻译
3. WHEN 翻译代码注释 THEN 系统 SHALL 将英文注释翻译为中文
4. WHEN 处理代码单元格 THEN 系统 SHALL 保持代码逻辑不变，仅翻译注释和字符串
5. WHEN 翻译内容 THEN 系统 SHALL 确保原版notebook内容一字不差地保留

### Requirement 2

**User Story:** 作为开发者，我希望为每个notebook创建独立的项目文件夹，以便更好地组织和管理相关文件。

#### Acceptance Criteria

1. WHEN 处理notebook文件 THEN 系统 SHALL 为每个lesson创建独立的文件夹（如C3L6, C3L7等）
2. WHEN 创建项目结构 THEN 系统 SHALL 将双语notebook放置在对应的文件夹中
3. WHEN 完成处理 THEN 系统 SHALL 删除raw notebook文件夹中的原始文件
4. WHEN 创建文件夹 THEN 系统 SHALL 使用标准化的命名约定（C3L{lesson_number}）

### Requirement 3

**User Story:** 作为开发者，我希望根据每个notebook中引用的缺失函数来推断和实现所需的辅助函数，并考虑函数复用性，以便所有notebook能够正常运行。

#### Acceptance Criteria

1. WHEN 分析每个notebook内容 THEN 系统 SHALL 识别该notebook中引用但缺失的函数和模块
2. WHEN 推断函数功能 THEN 系统 SHALL 根据notebook中的使用上下文推断函数的预期行为
3. WHEN 创建新辅助函数 THEN 系统 SHALL 检查已有的helper_functions.py中是否存在可复用的函数
4. WHEN 发现可复用函数 THEN 系统 SHALL 优先使用或扩展现有函数而非创建新函数
5. WHEN 创建辅助函数 THEN 系统 SHALL 使用项目根目录的helper_functions包，并在课程文件夹中创建代理文件
6. WHEN 辅助函数需要大模型功能 THEN 系统 SHALL 配置使用ollama作为后端，选用gemma3n:latest模型
7. WHEN 创建辅助函数 THEN 系统 SHALL 使用统一的helper_functions包结构，避免重复代码
7. WHEN 创建辅助函数 THEN 系统 SHALL 添加适当的中文注释和文档字符串

### Requirement 4

**User Story:** 作为开发者，我希望创建完整的项目配置文件，以便项目能够正确运行。

#### Acceptance Criteria

1. WHEN 创建项目结构 THEN 系统 SHALL 生成requirements.txt文件包含所需依赖
2. WHEN 配置环境 THEN 系统 SHALL 设置notebook使用base虚拟环境
3. WHEN 需要数据文件 THEN 系统 SHALL 创建相应的数据文件（如城市描述文件）
4. WHEN 创建README THEN 系统 SHALL 提供项目说明和使用指南

### Requirement 5

**User Story:** 作为开发者，我希望确保翻译质量和代码功能完整性，以便用户能够正常学习和使用。

#### Acceptance Criteria

1. WHEN 翻译内容 THEN 系统 SHALL 确保翻译准确且符合技术术语规范
2. WHEN 处理代码示例 THEN 系统 SHALL 保持代码的可执行性
3. WHEN 创建练习题 THEN 系统 SHALL 提供中文说明和提示
4. WHEN 完成翻译 THEN 系统 SHALL 验证notebook能够正常运行