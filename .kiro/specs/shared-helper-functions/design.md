# Design Document

## Overview

本设计将重构当前项目的辅助函数结构，从每个课程都有独立的helper_functions.py文件，改为使用统一的共享模块。新的结构将提高代码复用性，减少维护成本，并提供更好的用户体验。

## Architecture

### 新的项目结构

```
ai-python-bilingual-course/
├── shared_utils/                    # 共享工具包 / Shared utilities package
│   ├── __init__.py                 # 包初始化文件 / Package initialization
│   ├── llm_utils.py               # LLM相关功能 / LLM related functions
│   ├── model_config.py            # 模型配置管理 / Model configuration management
│   └── common_utils.py            # 通用工具函数 / Common utility functions
├── ollama_config.json             # 全局模型配置 / Global model configuration
├── C1L6/
│   ├── C1L6_Bilingual.ipynb      # 只需导入共享模块 / Only import shared modules
│   └── requirements.txt
├── C1L7/
├── C1L9/
├── C1L10/
└── C3L6/
```

### 模块设计

#### 1. shared_utils/__init__.py
- 提供便捷的导入接口
- 自动处理路径问题
- 向后兼容性支持

#### 2. shared_utils/model_config.py
- 智能模型配置功能
- 环境变量支持
- 配置文件管理
- 自动模型检测

#### 3. shared_utils/llm_utils.py
- LLM调用功能
- 响应处理
- 错误处理和备用机制

#### 4. shared_utils/common_utils.py
- 其他通用工具函数
- 文件操作辅助
- 数据处理工具

## Components and Interfaces

### 导入接口设计

```python
# 方式1：直接导入所有常用函数 / Method 1: Direct import of common functions
from shared_utils import print_llm_response, get_llm_response, get_default_model, set_default_model

# 方式2：导入特定模块 / Method 2: Import specific modules
from shared_utils.llm_utils import print_llm_response, get_llm_response
from shared_utils.model_config import get_default_model, set_default_model

# 方式3：向后兼容方式 / Method 3: Backward compatibility
import shared_utils as helper_functions
helper_functions.print_llm_response("Hello")
```

### 配置管理设计

#### 配置优先级（保持不变）
1. 环境变量 `OLLAMA_MODEL`
2. 课程级配置文件 `{lesson}/ollama_config.json`
3. 全局配置文件 `ollama_config.json`
4. 自动检测第一个可用模型
5. 默认回退 `gemma3n:latest`

#### 配置文件结构
```json
{
  "default_model": "gemma3n:latest",
  "fallback_models": ["llama2:latest", "mistral:latest"],
  "timeout": 60,
  "auto_detect": true
}
```

## Data Models

### ModelConfig类
```python
class ModelConfig:
    def __init__(self):
        self.default_model = None
        self.fallback_models = []
        self.timeout = 60
        self.auto_detect = True
    
    def get_active_model(self):
        # 实现智能模型选择逻辑
        pass
    
    def set_model(self, model_name):
        # 设置模型配置
        pass
```

## Error Handling

### 路径处理
- 自动检测项目根目录
- 处理不同课程的相对路径
- 支持从任意位置导入

### 兼容性处理
- 保持现有导入方式的兼容性
- 渐进式迁移支持
- 错误提示和迁移建议

### 模型配置错误处理
- 配置文件解析错误处理
- 模型不存在时的备用机制
- 网络连接问题的处理

## Testing Strategy

### 单元测试
- 模型配置功能测试
- LLM调用功能测试
- 路径处理测试

### 集成测试
- 各课程导入测试
- 端到端功能测试
- 配置优先级测试

### 兼容性测试
- 现有notebook兼容性
- 不同操作系统兼容性
- 不同Python版本兼容性

## Migration Strategy

### 阶段1：创建共享模块
1. 创建shared_utils包结构
2. 迁移通用函数到共享模块
3. 实现向后兼容接口

### 阶段2：更新课程
1. 更新各课程的导入语句
2. 删除重复的helper_functions.py文件
3. 更新相关文档

### 阶段3：优化和清理
1. 优化共享模块性能
2. 清理临时兼容代码
3. 更新测试和文档

## Benefits

### 代码维护
- 减少90%的重复代码
- 统一的功能实现
- 更容易添加新功能

### 用户体验
- 更简洁的导入方式
- 一致的功能体验
- 更好的错误提示

### 项目管理
- 更清晰的项目结构
- 更容易的版本管理
- 更好的可扩展性