from fastapi import FastAPI, UploadFile, File, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import tempfile
import os
from file_loader import load_pdf_text, split_text
from vector_db import add_text_chunks, search_similar_text
from llm_agent import generate_answer

app = FastAPI(title="课程知识库问答助手")
# 挂载前端静态页面
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("src/static/index.html", "r", encoding="utf-8") as f:
        return f.read()

# 上传PDF文档接口
@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # 临时存储上传文件
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    try:
        text = load_pdf_text(tmp_path)
        chunks = split_text(text)
        add_text_chunks(chunks)
        return {"code": 200, "msg": f"文档解析完成，共分块{len(chunks)}段，已存入知识库"}
    finally:
        os.unlink(tmp_path)

# 问答对话接口
@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    question = data.get("question", "")
    if not question:
        return {"code": 400, "msg": "问题不能为空"}
    # 检索上下文
    context = search_similar_text(question)
    answer = generate_answer(question, context)
    return {"code": 200, "answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
