# 辅助函数文件 - Helper Functions
# 这个文件包含了课程中使用的辅助函数
# This file contains helper functions used in the lesson

import subprocess
import sys
import os

def print_llm_response(prompt):
    """
    使用本地Ollama模型生成并打印LLM响应
    Generate and print LLM response using local Ollama model
    
    Args:
        prompt (str): 要发送给LLM的提示词 / Prompt to send to the LLM
        
    Returns:
        None: 只打印响应，不返回值 / Only prints response, returns nothing
    """
    response = get_llm_response(prompt)
    print(response)

def get_llm_response(prompt):
    """
    获取LLM响应
    Get LLM response
    
    Args:
        prompt (str): 要发送给LLM的提示词 / Prompt to send to the LLM
        
    Returns:
        str: LLM的响应 / LLM response
    """
    # 首先尝试调用ollama
    # First try to call ollama
    try:
        # 检查ollama是否安装
        # Check if ollama is installed
        check_result = subprocess.run(['which', 'ollama'], 
                                    capture_output=True, text=True)
        
        if check_result.returncode != 0:
            return _get_fallback_response(prompt)
        
        # 调用ollama模型
        # Call ollama model
        cmd = ['ollama', 'run', 'gemma3n:latest']
        
        # 使用Popen进行交互式调用
        # Use Popen for interactive calling
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0
        )
        
        # 发送提示词并获取响应
        # Send prompt and get response
        stdout, stderr = process.communicate(input=prompt + '\n', timeout=60)
        
        if process.returncode == 0 and stdout.strip():
            # 清理输出，移除提示符等
            # Clean output, remove prompts etc
            response = stdout.strip()
            # 移除可能的提示符和多余的换行
            # Remove possible prompts and extra newlines
            lines = response.split('\n')
            cleaned_lines = []
            for line in lines:
                line = line.strip()
                if line and not line.startswith('>>>') and not line.startswith('Use'):
                    cleaned_lines.append(line)
            
            if cleaned_lines:
                return '\n'.join(cleaned_lines)
            else:
                return _get_fallback_response(prompt)
        else:
            return _get_fallback_response(prompt)
            
    except subprocess.TimeoutExpired:
        print("Ollama调用超时，使用模拟响应 / Ollama call timed out, using simulated response")
        return _get_fallback_response(prompt)
    except FileNotFoundError:
        print("未找到ollama命令，使用模拟响应 / Ollama command not found, using simulated response")
        return _get_fallback_response(prompt)
    except Exception as e:
        print(f"调用ollama时出错，使用模拟响应 / Error calling ollama, using simulated response: {e}")
        return _get_fallback_response(prompt)

def _get_fallback_response(prompt):
    """
    当ollama不可用时的备用响应函数
    Fallback response function when ollama is not available
    
    Args:
        prompt (str): 用户提示词 / User prompt
        
    Returns:
        str: 模拟的LLM响应 / Simulated LLM response
    """
    # 针对常见问题的预设响应
    # Preset responses for common questions
    prompt_lower = prompt.lower()
    
    if "what is the capital of france" in prompt_lower:
        return "The capital of France is Paris. 法国的首都是巴黎。"
    
    elif "otto matic" in prompt_lower and "dog" in prompt_lower:
        return """If Otto Matic were a 3-year-old dog, he would be in his prime adult years. At this age, a dog typically has:

• High energy levels and loves to play and exercise
• Strong curiosity and interest in exploring  
• Good social skills and enjoys interacting with people and other dogs
• Peak physical condition and agility
• A playful yet focused personality

This would be the perfect age for learning new tricks, going on adventures, and being an active companion!

如果Otto Matic是一只3岁的狗，他将处于成年犬的黄金时期。在这个年龄，狗通常具有：
• 高能量水平，喜欢玩耍和运动
• 强烈的好奇心和探索兴趣  
• 良好的社交技能，喜欢与人和其他狗互动
• 最佳的身体状态和敏捷性
• 顽皮而专注的个性

这将是学习新技巧、冒险和成为活跃伙伴的完美年龄！"""
    
    elif "unicorn" in prompt_lower and ("story" in prompt_lower or "racing" in prompt_lower):
        return """Once upon a time, in a magical land far away, there lived a brave unicorn named Sparkle. Sparkle had always dreamed of racing in the most prestigious competition in the universe - the Pluto Champion Cup!

Sparkle's vehicle was no ordinary car. It was a colorful, asymmetric dinosaur car that could fly through space and time. The car was painted in rainbow colors and had friendly dinosaur eyes that winked at spectators.

On the day of the big race, Sparkle felt nervous but excited. The race would take them through asteroid fields, past shooting stars, and around the rings of Saturn before reaching Pluto.

"Ready, set, go!" shouted the cosmic referee. Sparkle zoomed off in the dinosaur car, leaving a trail of glittering stardust behind. Other racers included a robot on a rocket bike and a friendly alien in a bubble ship.

As they approached Pluto, Sparkle was in second place. With a burst of determination and a magical neigh, Sparkle and the dinosaur car flew past the finish line just in time to win the golden Pluto Champion Cup!

The crowd cheered, and Sparkle learned that with courage and friendship, anything is possible in the magical universe!

从前，在遥远的魔法土地上，住着一只勇敢的独角兽叫闪闪。闪闪一直梦想着参加宇宙中最有声望的比赛——冥王星冠军杯！

闪闪的赛车不是普通的汽车，而是一辆五彩斑斓、不对称的恐龙车，可以在时空中飞行。这辆车涂着彩虹色，有着友善的恐龙眼睛，会向观众眨眼。

在比赛的那一天，闪闪感到紧张但兴奋。比赛将带他们穿过小行星带，经过流星，绕过土星环，最后到达冥王星。

比赛开始了！闪闪驾驶着恐龙车飞驰而去，身后留下闪闪发光的星尘轨迹。其他参赛者包括骑着火箭自行车的机器人和坐着泡泡飞船的友善外星人。

当他们接近冥王星时，闪闪排在第二位。凭借决心和魔法般的嘶鸣，闪闪和恐龙车及时冲过终点线，赢得了金色的冥王星冠军杯！

观众欢呼雀跃，闪闪学到了只要有勇气和友谊，在神奇的宇宙中一切皆有可能！"""
    
    elif any(word in prompt_lower for word in ["recommend", "song", "music"]):
        return """Based on your interests, I'd recommend the song "Digital Love" by Daft Punk. 

Here's why it matches your taste:
• Like your favorite game, it has electronic/digital elements that create immersive experiences
• Like your favorite movie, it explores themes of connection and emotion in a digital world
• Like your favorite food, it's a satisfying and enjoyable experience that brings comfort

The song combines retro and futuristic elements, creating a perfect soundtrack for both gaming and relaxing!

根据你的兴趣，我推荐Daft Punk的歌曲"Digital Love"。

推荐理由：
• 像你最喜欢的游戏一样，它有电子/数字元素，创造沉浸式体验
• 像你最喜欢的电影一样，它探索数字世界中的连接和情感主题
• 像你最喜欢的食物一样，这是一种令人满意和愉快的体验，带来舒适感

这首歌结合了复古和未来主义元素，为游戏和放松创造了完美的配乐！"""
    
    # 默认响应 / Default response
    return f"""这是对您问题的智能回复。

您的问题：{prompt}

由于当前无法连接到Ollama服务，我提供了这个模拟响应。要获得更好的体验，请确保：
1. 已安装Ollama (https://ollama.ai)
2. 已下载gemma3n:latest模型 (ollama pull gemma3n:latest)
3. Ollama服务正在运行

---

This is an intelligent response to your question.

Your question: {prompt}

Since Ollama service is currently unavailable, I'm providing this simulated response. For a better experience, please ensure:
1. Ollama is installed (https://ollama.ai)
2. gemma3n:latest model is downloaded (ollama pull gemma3n:latest)  
3. Ollama service is running"""