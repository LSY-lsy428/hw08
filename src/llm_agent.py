import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    base_url=os.getenv("LLM_BASE_URL"),
    api_key=os.getenv("LLM_API_KEY"),
    model=os.getenv("LLM_MODEL_NAME")
)

SYSTEM_PROMPT = """
你是课程知识库答疑助手，仅允许根据下方参考文档内容回答用户问题。
1. 如果参考文档没有对应信息，直接回复：【文档中未查询到该知识点，无法作答】
2. 禁止编造、臆测任何文档以外的内容
3. 回答条理清晰，贴合课程知识点，简洁易懂
参考文档片段：
{context_content}
"""

def generate_answer(user_query: str, context_list: list) -> str:
    context_content = "\n\n=====文档片段=====\n".join(context_list)
    prompt = SYSTEM_PROMPT.format(context_content=context_content)
    resp = llm.invoke([
        ("system", prompt),
        ("human", user_query)
    ])
    return resp.content
