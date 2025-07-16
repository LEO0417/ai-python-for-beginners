# 贡献指南 / Contributing Guide

感谢你对AI Python双语课程项目的关注！我们欢迎各种形式的贡献。

Thank you for your interest in the AI Python Bilingual Course project! We welcome contributions of all kinds.

## 如何贡献 / How to Contribute

### 报告问题 / Reporting Issues

如果你发现了bug或有改进建议，请：

If you find a bug or have suggestions for improvement, please:

1. 检查是否已有相关issue / Check if there's already a related issue
2. 创建新的issue，详细描述问题 / Create a new issue with detailed description
3. 包含复现步骤和环境信息 / Include reproduction steps and environment info

### 提交代码 / Submitting Code

1. **Fork项目** / **Fork the project**
   ```bash
   # 在GitHub上fork项目 / Fork the project on GitHub
   # 克隆你的fork / Clone your fork
   git clone https://github.com/your-username/ai-python-bilingual-course.git
   cd ai-python-bilingual-course
   ```

2. **创建分支** / **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # 或 / or
   git checkout -b fix/your-bug-fix
   ```

3. **进行修改** / **Make changes**
   - 遵循现有的代码风格 / Follow existing code style
   - 添加必要的注释 / Add necessary comments
   - 确保双语内容的一致性 / Ensure bilingual content consistency

4. **测试修改** / **Test changes**
   ```bash
   # 测试相关的notebook / Test relevant notebooks
   jupyter notebook path/to/notebook.ipynb
   
   # 确保代码能正常运行 / Ensure code runs properly
   python helper_functions.py
   ```

5. **提交更改** / **Commit changes**
   ```bash
   git add .
   git commit -m "feat: add new lesson on data visualization"
   # 或 / or
   git commit -m "fix: correct translation in C1L6"
   ```

6. **推送并创建PR** / **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   # 在GitHub上创建Pull Request / Create Pull Request on GitHub
   ```

## 贡献类型 / Types of Contributions

### 新课程 / New Lessons

添加新课程时，请确保：

When adding new lessons, please ensure:

- 遵循现有的文件夹结构 / Follow existing folder structure
- 包含双语内容 / Include bilingual content
- 提供完整的项目文件 / Provide complete project files
- 添加适当的README文档 / Add appropriate README documentation

**新课程文件结构** / **New Lesson File Structure**:
```
CXLx/
├── CXLx_Bilingual.ipynb    # 双语notebook / Bilingual notebook
├── helper_functions.py      # 辅助函数 / Helper functions
├── requirements.txt         # 依赖文件 / Dependencies
├── README.md               # 课程说明 / Lesson documentation
└── [data files]            # 数据文件 / Data files (if needed)
```

### 翻译改进 / Translation Improvements

改进翻译时，请注意：

When improving translations, please note:

- 保持技术术语的一致性 / Maintain consistency in technical terms
- 确保中英文内容的对应关系 / Ensure correspondence between Chinese and English
- 考虑中文学习者的理解习惯 / Consider Chinese learners' understanding habits
- 保持原文的完整性 / Maintain integrity of original content

### 文档更新 / Documentation Updates

更新文档时，请：

When updating documentation:

- 同时更新中英文版本 / Update both Chinese and English versions
- 保持格式的一致性 / Maintain format consistency
- 确保链接和引用的正确性 / Ensure correctness of links and references

### Bug修复 / Bug Fixes

修复bug时，请：

When fixing bugs:

- 清楚描述问题和解决方案 / Clearly describe the problem and solution
- 添加测试用例（如适用）/ Add test cases (if applicable)
- 更新相关文档 / Update relevant documentation

## 代码规范 / Code Standards

### Python代码 / Python Code

- 遵循PEP 8规范 / Follow PEP 8 standards
- 使用有意义的变量名 / Use meaningful variable names
- 添加适当的注释和文档字符串 / Add appropriate comments and docstrings
- 保持函数简洁和单一职责 / Keep functions concise and single-purpose

### Notebook规范 / Notebook Standards

- 每个cell都应该能独立运行 / Each cell should run independently
- 添加清晰的markdown说明 / Add clear markdown explanations
- 保持代码和输出的整洁 / Keep code and output clean
- 确保双语内容的平衡 / Ensure balance of bilingual content

### 注释规范 / Comment Standards

```python
# 中文注释示例 / Chinese comment example
def calculate_temperature(celsius):
    """
    将摄氏度转换为华氏度
    Convert Celsius to Fahrenheit
    
    Args:
        celsius (float): 摄氏度温度 / Temperature in Celsius
        
    Returns:
        float: 华氏度温度 / Temperature in Fahrenheit
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
```

## 提交信息规范 / Commit Message Standards

使用以下格式 / Use the following format:

```
type(scope): description

feat: 新功能 / new feature
fix: bug修复 / bug fix
docs: 文档更新 / documentation update
style: 代码格式 / code formatting
refactor: 代码重构 / code refactoring
test: 测试相关 / test related
chore: 构建过程或辅助工具的变动 / build process or auxiliary tool changes
```

**示例** / **Examples**:
- `feat(C1L6): add temperature conversion exercise`
- `fix(C3L6): correct LLM integration function`
- `docs(README): update installation instructions`
- `style(helper): improve code formatting`

## 审查流程 / Review Process

1. **自动检查** / **Automated Checks**
   - 代码格式检查 / Code format check
   - 基本功能测试 / Basic functionality test

2. **人工审查** / **Manual Review**
   - 代码质量评估 / Code quality assessment
   - 双语内容检查 / Bilingual content check
   - 教学效果评估 / Educational effectiveness assessment

3. **反馈和修改** / **Feedback and Revision**
   - 根据反馈进行修改 / Make changes based on feedback
   - 重新提交审查 / Resubmit for review

## 社区准则 / Community Guidelines

请遵循我们的 [行为准则](CODE_OF_CONDUCT.md)。

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md).

### 核心原则 / Core Principles

- **尊重** / **Respect**: 尊重所有贡献者和学习者
- **包容** / **Inclusivity**: 欢迎不同背景的参与者
- **协作** / **Collaboration**: 鼓励合作和知识分享
- **质量** / **Quality**: 追求高质量的教学内容

## 获取帮助 / Getting Help

如果你需要帮助，可以：

If you need help, you can:

- 查看现有的issue和讨论 / Check existing issues and discussions
- 创建新的issue询问问题 / Create a new issue to ask questions
- 参考项目文档和README / Refer to project documentation and README

## 认可贡献者 / Recognizing Contributors

我们会在项目中认可所有贡献者的努力：

We recognize all contributors' efforts in the project:

- 在README中列出贡献者 / List contributors in README
- 在发布说明中感谢贡献者 / Thank contributors in release notes
- 为重要贡献者提供特殊认可 / Provide special recognition for significant contributors

---

再次感谢你的贡献！你的努力将帮助更多人学习AI和Python编程。

Thank you again for your contribution! Your efforts will help more people learn AI and Python programming.