# 辅助函数文件 - Helper Functions
# 这个文件包含了课程中使用的辅助函数

def print_llm_response(prompt):
    """
    模拟LLM响应的函数，用于演示目的
    在实际环境中，这里会调用真实的LLM API
    
    Args:
        prompt (str): 要发送给LLM的提示词
        
    Returns:
        str: LLM的响应
    """
    # 模拟LLM响应
    responses = {
        "What is the capital of France": "The capital of France is Paris.",
        "What is 2+2": "2 + 2 = 4",
        "Hello": "Hello! How can I help you today?",
        "default": f"这是对'{prompt}'的模拟响应。在实际环境中，这里会调用真实的LLM API。"
    }
    
    response = responses.get(prompt, responses["default"])
    print(f"LLM Response: {response}")
    return response

def get_llm_response(prompt):
    """
    获取LLM响应的函数，返回响应字符串而不是打印
    
    Args:
        prompt (str): 要发送给LLM的提示词
        
    Returns:
        str: LLM的响应
    """
    # 模拟LLM响应
    responses = {
        "Create a three bullet point summary": "• 这是一个模拟的要点总结\n• 在实际环境中会生成真实的总结\n• 用于演示函数的使用",
        "What is the weather": "The weather is sunny today.",
        "default": f"这是对'{prompt}'的模拟响应。在实际环境中，这里会调用真实的LLM API。"
    }
    
    response = responses.get(prompt, responses["default"])
    return response 