#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Python课程自动化设置脚本
AI Python Course Automated Setup Script

这个脚本会自动检查和设置AI Python课程的运行环境
This script automatically checks and sets up the running environment for AI Python course
"""

import os
import sys
import json
import subprocess
import platform
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class CourseSetup:
    """课程设置管理器 / Course Setup Manager"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.project_root = Path(__file__).parent.parent
        self.config_file = self.project_root / "ollama_config.json"
        self.setup_log = []
        
    def log(self, message: str, level: str = "INFO") -> None:
        """记录日志 / Log message"""
        log_entry = f"[{level}] {message}"
        self.setup_log.append(log_entry)
        print(log_entry)
    
    def run_command(self, command: List[str], timeout: int = 60) -> Tuple[int, str, str]:
        """运行命令 / Run command"""
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return 1, "", "Command timeout"
        except Exception as e:
            return 1, "", str(e)
    
    def check_python_version(self) -> bool:
        """检查Python版本 / Check Python version"""
        self.log("检查Python版本 / Checking Python version...")
        
        version_info = sys.version_info
        if version_info.major >= 3 and version_info.minor >= 9:
            self.log(f"✅ Python版本符合要求 / Python version OK: {sys.version}")
            return True
        else:
            self.log(f"❌ Python版本过低 / Python version too low: {sys.version}")
            self.log("需要Python 3.9或更高版本 / Requires Python 3.9 or higher")
            return False
    
    def check_ollama_installation(self) -> bool:
        """检查Ollama安装 / Check Ollama installation"""
        self.log("检查Ollama安装 / Checking Ollama installation...")
        
        returncode, stdout, stderr = self.run_command(["ollama", "--version"])
        
        if returncode == 0:
            self.log(f"✅ Ollama已安装 / Ollama installed: {stdout.strip()}")
            return True
        else:
            self.log("❌ Ollama未安装 / Ollama not installed")
            return False
    
    def install_ollama(self) -> bool:
        """安装Ollama / Install Ollama"""
        self.log("开始安装Ollama / Starting Ollama installation...")
        
        if self.system == "darwin":  # macOS
            # 尝试使用Homebrew安装
            returncode, stdout, stderr = self.run_command(["brew", "--version"])
            if returncode == 0:
                self.log("使用Homebrew安装Ollama / Installing Ollama using Homebrew...")
                returncode, stdout, stderr = self.run_command(["brew", "install", "ollama"])
                if returncode == 0:
                    self.log("✅ Ollama通过Homebrew安装成功 / Ollama installed successfully via Homebrew")
                    return True
            
            # 如果Homebrew失败，使用官方安装脚本
            self.log("使用官方安装脚本 / Using official install script...")
            returncode, stdout, stderr = self.run_command([
                "curl", "-fsSL", "https://ollama.ai/install.sh"
            ])
            if returncode == 0:
                # 运行安装脚本
                returncode, stdout, stderr = self.run_command(["sh", "-c", stdout])
                if returncode == 0:
                    self.log("✅ Ollama安装成功 / Ollama installed successfully")
                    return True
        
        elif self.system == "linux":
            # Linux系统使用官方安装脚本
            self.log("使用官方安装脚本 / Using official install script...")
            returncode, stdout, stderr = self.run_command([
                "curl", "-fsSL", "https://ollama.ai/install.sh"
            ])
            if returncode == 0:
                # 运行安装脚本
                returncode, stdout, stderr = self.run_command(["sh", "-c", stdout])
                if returncode == 0:
                    self.log("✅ Ollama安装成功 / Ollama installed successfully")
                    return True
        
        elif self.system == "windows":
            self.log("Windows系统请手动安装Ollama / Please manually install Ollama on Windows")
            self.log("访问 https://ollama.ai/download 下载Windows版本 / Visit https://ollama.ai/download for Windows version")
            return False
        
        self.log("❌ Ollama安装失败 / Ollama installation failed")
        return False
    
    def check_ollama_service(self) -> bool:
        """检查Ollama服务状态 / Check Ollama service status"""
        self.log("检查Ollama服务状态 / Checking Ollama service status...")
        
        # 检查服务是否运行
        returncode, stdout, stderr = self.run_command(["pgrep", "ollama"])
        
        if returncode == 0:
            self.log("✅ Ollama服务正在运行 / Ollama service is running")
            return True
        else:
            self.log("❌ Ollama服务未运行 / Ollama service is not running")
            return False
    
    def start_ollama_service(self) -> bool:
        """启动Ollama服务 / Start Ollama service"""
        self.log("启动Ollama服务 / Starting Ollama service...")
        
        # 在后台启动服务
        try:
            if self.system in ["darwin", "linux"]:
                subprocess.Popen(
                    ["nohup", "ollama", "serve"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    start_new_session=True
                )
                
                # 等待服务启动
                import time
                time.sleep(3)
                
                # 检查服务是否成功启动
                if self.check_ollama_service():
                    self.log("✅ Ollama服务启动成功 / Ollama service started successfully")
                    return True
                else:
                    self.log("❌ Ollama服务启动失败 / Ollama service failed to start")
                    return False
            
            elif self.system == "windows":
                # Windows系统需要手动启动服务
                self.log("Windows系统请手动启动Ollama服务 / Please manually start Ollama service on Windows")
                self.log("在命令行中运行 / Run in command line: ollama serve")
                return False
        
        except Exception as e:
            self.log(f"❌ 启动Ollama服务时出错 / Error starting Ollama service: {e}")
            return False
    
    def check_models(self) -> List[str]:
        """检查已安装的模型 / Check installed models"""
        self.log("检查已安装的模型 / Checking installed models...")
        
        returncode, stdout, stderr = self.run_command(["ollama", "list"])
        
        if returncode == 0:
            lines = stdout.strip().split('\n')
            models = []
            for line in lines[1:]:  # 跳过标题行
                if line.strip():
                    model_info = line.split()
                    if model_info and ':' in model_info[0]:
                        models.append(model_info[0])
            
            if models:
                self.log(f"✅ 找到已安装模型 / Found installed models: {', '.join(models)}")
            else:
                self.log("❌ 没有找到已安装的模型 / No installed models found")
            
            return models
        else:
            self.log(f"❌ 检查模型失败 / Failed to check models: {stderr}")
            return []
    
    def install_recommended_models(self) -> bool:
        """安装推荐的模型 / Install recommended models"""
        self.log("开始安装推荐模型 / Starting to install recommended models...")
        
        recommended_models = [
            "qwen3:0.6b",      # 轻量级模型
            "gemma3n:latest",  # 平衡模型
        ]
        
        success_count = 0
        
        for model in recommended_models:
            self.log(f"正在安装模型 / Installing model: {model}")
            
            returncode, stdout, stderr = self.run_command(
                ["ollama", "pull", model], 
                timeout=300  # 5分钟超时
            )
            
            if returncode == 0:
                self.log(f"✅ 模型安装成功 / Model installed successfully: {model}")
                success_count += 1
            else:
                self.log(f"❌ 模型安装失败 / Model installation failed: {model}")
                self.log(f"错误信息 / Error message: {stderr}")
        
        if success_count > 0:
            self.log(f"✅ 成功安装 {success_count} 个模型 / Successfully installed {success_count} models")
            return True
        else:
            self.log("❌ 没有成功安装任何模型 / No models installed successfully")
            return False
    
    def create_config_file(self) -> bool:
        """创建配置文件 / Create configuration file"""
        self.log("创建配置文件 / Creating configuration file...")
        
        # 检查已安装的模型
        models = self.check_models()
        
        if not models:
            self.log("❌ 没有可用模型，无法创建配置文件 / No available models, cannot create config file")
            return False
        
        # 选择默认模型
        default_model = "qwen3:0.6b" if "qwen3:0.6b" in models else models[0]
        
        config = {
            "default_model": default_model,
            "fallback_model": models[0] if len(models) > 1 else default_model,
            "timeout": 60,
            "retry_attempts": 3,
            "setup_version": "1.0.0",
            "setup_date": str(Path(__file__).stat().st_mtime)
        }
        
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            self.log(f"✅ 配置文件创建成功 / Configuration file created successfully: {self.config_file}")
            self.log(f"默认模型 / Default model: {default_model}")
            return True
        
        except Exception as e:
            self.log(f"❌ 创建配置文件失败 / Failed to create configuration file: {e}")
            return False
    
    def install_python_dependencies(self) -> bool:
        """安装Python依赖 / Install Python dependencies"""
        self.log("检查Python依赖 / Checking Python dependencies...")
        
        requirements_file = self.project_root / "requirements.txt"
        
        if not requirements_file.exists():
            self.log("❌ 没有找到requirements.txt文件 / requirements.txt file not found")
            return False
        
        self.log("安装Python依赖 / Installing Python dependencies...")
        
        returncode, stdout, stderr = self.run_command([
            sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
        ])
        
        if returncode == 0:
            self.log("✅ Python依赖安装成功 / Python dependencies installed successfully")
            return True
        else:
            self.log(f"❌ Python依赖安装失败 / Python dependencies installation failed: {stderr}")
            return False
    
    def test_setup(self) -> bool:
        """测试设置 / Test setup"""
        self.log("测试设置 / Testing setup...")
        
        try:
            # 测试导入
            sys.path.insert(0, str(self.project_root))
            from helper_functions import get_default_model, test_llm_connection
            
            # 测试模型配置
            current_model = get_default_model()
            self.log(f"当前模型 / Current model: {current_model}")
            
            # 测试连接
            if test_llm_connection():
                self.log("✅ 设置测试成功 / Setup test successful")
                return True
            else:
                self.log("❌ 连接测试失败 / Connection test failed")
                return False
        
        except Exception as e:
            self.log(f"❌ 设置测试失败 / Setup test failed: {e}")
            return False
    
    def run_setup(self) -> bool:
        """运行完整设置 / Run complete setup"""
        self.log("=" * 60)
        self.log("开始AI Python课程自动化设置 / Starting AI Python Course Automated Setup")
        self.log("=" * 60)
        
        steps = [
            ("检查Python版本", self.check_python_version),
            ("检查Ollama安装", self.check_ollama_installation),
            ("安装Python依赖", self.install_python_dependencies),
        ]
        
        # 如果Ollama未安装，尝试安装
        if not self.check_ollama_installation():
            steps.append(("安装Ollama", self.install_ollama))
        
        # 继续其他步骤
        steps.extend([
            ("检查Ollama服务", self.check_ollama_service),
            ("检查模型", self.check_models),
            ("创建配置文件", self.create_config_file),
            ("测试设置", self.test_setup),
        ])
        
        # 如果服务未运行，尝试启动
        if not self.check_ollama_service():
            steps.insert(-3, ("启动Ollama服务", self.start_ollama_service))
        
        # 如果没有模型，安装推荐模型
        if not self.check_models():
            steps.insert(-2, ("安装推荐模型", self.install_recommended_models))
        
        # 执行所有步骤
        failed_steps = []
        for step_name, step_func in steps:
            self.log(f"\n{'='*20} {step_name} {'='*20}")
            try:
                if not step_func():
                    failed_steps.append(step_name)
            except Exception as e:
                self.log(f"❌ 步骤执行异常 / Step execution error: {e}")
                failed_steps.append(step_name)
        
        # 总结结果
        self.log("\n" + "=" * 60)
        if failed_steps:
            self.log(f"❌ 设置完成，但有 {len(failed_steps)} 个步骤失败:")
            self.log(f"❌ Setup completed, but {len(failed_steps)} steps failed:")
            for step in failed_steps:
                self.log(f"   - {step}")
            self.log("\n请查看上述日志信息，手动完成失败的步骤。")
            self.log("Please check the log messages above and manually complete the failed steps.")
            return False
        else:
            self.log("✅ 设置完成！所有步骤都成功执行。")
            self.log("✅ Setup completed! All steps executed successfully.")
            self.log("\n你现在可以开始使用AI Python课程了！")
            self.log("You can now start using the AI Python course!")
            return True
    
    def save_log(self) -> None:
        """保存日志 / Save log"""
        log_file = self.project_root / "setup.log"
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.setup_log))
            self.log(f"日志已保存到 / Log saved to: {log_file}")
        except Exception as e:
            self.log(f"保存日志失败 / Failed to save log: {e}")


def main():
    """主函数 / Main function"""
    setup = CourseSetup()
    
    try:
        success = setup.run_setup()
        setup.save_log()
        
        if success:
            print("\n🎉 设置成功完成！/ Setup completed successfully!")
            print("现在你可以开始学习AI Python课程了。/ You can now start learning the AI Python course.")
            print("运行以下命令开始第一课：/ Run the following command to start the first lesson:")
            print("cd C1L9 && jupyter notebook C1L9_Bilingual.ipynb")
            return 0
        else:
            print("\n⚠️ 设置过程中出现一些问题 / Some issues occurred during setup")
            print("请查看setup.log文件了解详细信息 / Please check setup.log for details")
            print("或者查看TROUBLESHOOTING.md获取帮助 / Or check TROUBLESHOOTING.md for help")
            return 1
    
    except KeyboardInterrupt:
        print("\n用户中断设置 / User interrupted setup")
        return 1
    except Exception as e:
        print(f"\n设置过程中发生未预期的错误 / Unexpected error during setup: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())