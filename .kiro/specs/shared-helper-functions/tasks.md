# Implementation Plan

- [x] 1. 创建共享工具包结构
  - 创建shared_utils文件夹和包结构
  - 创建__init__.py文件提供便捷导入接口
  - 设计模块化的文件结构（model_config.py, llm_utils.py, common_utils.py）
  - 实现自动路径检测和处理机制
  - _Requirements: 1.1, 3.1, 4.4_

- [x] 2. 迁移模型配置功能到共享模块
  - 将智能模型配置功能迁移到shared_utils/model_config.py
  - 实现get_default_model()和set_default_model()函数
  - 保持配置优先级：环境变量 > 局部配置 > 全局配置 > 自动检测 > 默认值
  - 支持全局配置文件ollama_config.json
  - 实现配置文件的读取和写入功能
  - _Requirements: 2.1, 2.2, 2.3, 2.4_

- [x] 3. 迁移LLM功能到共享模块
  - 将print_llm_response()和get_llm_response()函数迁移到shared_utils/llm_utils.py
  - 保持所有现有功能不变（ollama调用、错误处理、备用响应）
  - 实现模块间的依赖关系（llm_utils依赖model_config）
  - 确保备用响应机制正常工作
  - _Requirements: 1.2, 1.3_

- [x] 4. 实现便捷的导入接口
  - 在shared_utils/__init__.py中实现便捷导入
  - 支持from shared_utils import *的方式
  - 提供向后兼容的导入方式
  - 实现自动路径处理，支持从任意课程文件夹导入
  - _Requirements: 4.1, 4.2, 4.4_

- [x] 5. 更新各课程的导入语句
  - 修改所有notebook中的导入语句使用共享模块
  - 确保所有功能调用保持不变
  - 测试每个课程的功能是否正常
  - 处理可能的路径问题
  - _Requirements: 1.4, 4.1, 4.2_

- [x] 6. 清理重复的helper_functions.py文件
  - 删除各课程文件夹中的helper_functions.py文件
  - 保留课程特有的辅助函数（如果存在）
  - 确保没有遗漏任何课程特定的功能
  - _Requirements: 3.1, 3.2_

- [x] 7. 更新配置文件和文档
  - 创建全局ollama_config.json.example文件
  - 更新主README.md文档说明新的导入方式
  - 精简各课程的README.md文档，把共同的内容写进主README.md文档里面。
  - 更新CHANGELOG.md记录重构信息
  - _Requirements: 3.3, 4.3_

- [x] 8. 更新和优化测试脚本
  - 修改test_model_config.py适应新的模块结构
  - 添加共享模块的测试功能
  - 测试从不同位置导入的功能
  - 确保所有测试用例通过
  - _Requirements: 3.4, 5.2_

- [x] 9. 验证和测试整体功能
  - 测试所有课程的notebook是否正常运行
  - 验证模型配置功能在新结构下正常工作
  - 测试不同的导入方式是否都有效
  - 确保向后兼容性
  - 进行端到端的功能测试
  - _Requirements: 1.3, 4.2, 5.2_

- [x] 10. 文档完善和项目优化
  - 完善helper_fuctions模块的文档字符串
  - 添加使用示例和最佳实践
  - 优化错误提示和用户体验
  - 更新贡献指南中关于共享模块的说明
  - _Requirements: 4.3, 5.1, 5.3_