# 1. config

llm_config = {
    'model': 'Qwen1.5-14B-Chat-GPTQ-Int4',
    'base_url': 'http://127.0.0.1:7777/v1',
    'api_type': 'open_ai',
    'api_key': 'NULL'
}

# 2-1. init agent

def init_agent():
    import os
    from autogen import AssistantAgent, UserProxyAgent
    from autogen.coding import LocalCommandLineCodeExecutor

    # create an AssistantAgent instance named "assistant" with the LLM configuration.
    assistant = AssistantAgent(name="assistant", llm_config=llm_config)

    # create a UserProxyAgent instance named "user_proxy" with code execution.
    code_executor = LocalCommandLineCodeExecutor(work_dir="./autogen")
    user_proxy = UserProxyAgent(name="user_proxy", code_execution_config={"executor": code_executor})

    return user_proxy, assistant


# 2-2. init agent with another way

def init_agent_better():
    import os
    from autogen import AssistantAgent, UserProxyAgent

    # create an AssistantAgent instance named "assistant" with the LLM configuration.
    assistant = AssistantAgent(name="assistant", llm_config=llm_config)

    # create a UserProxyAgent instance named "user_proxy"
    user_proxy = UserProxyAgent(name="user_proxy",
                                code_execution_config={
                                    "work_dir": "./autogen",
                                    "use_docker": False
                                },
                                llm_config=llm_config)
    return user_proxy, assistant

# 3. initiate chat

# the assistant receives a message from the user, which contains the task description

user_proxy, assistant = init_agent() # or use init_agent_better()

user_proxy.initiate_chat(
    assistant,
    message="""Write python code to output numbers 1 to 100, and then store it in a file""",
)
