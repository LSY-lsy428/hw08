《人工智能导论》期末综合项目：基于RAG的课程知识库问答助手
项目简介
本项目为单人独立开发的轻量化Web端RAG知识库问答系统，基于大模型+检索增强生成技术，实现PDF课程文档上传、文本向量化存储、语义检索、基于文档约束的智能问答。
并非简单调用单次模型接口，具备完整文档解析、分块、向量存储、召回、Prompt约束、对话交互全链路AI逻辑，满足作业可演示、真实AI能力要求。

目录结构
hw08/
├── src/ # 全部源代码
│ ├── file_loader.py # PDF 解析、文本切分
│ ├── vector_db.py # 向量数据库持久化、检索
│ ├── llm_agent.py # Prompt 构造、大模型 API 调用
│ ├── main_server.py # FastAPI 服务启动入口
│ └── static/index.html # 前端交互页面
├── chroma_store/ # 自动生成：向量持久化存储目录
├── requirements.txt # 项目依赖清单
├── .env # 本地环境变量配置（不上传仓库）
├── report.md # 项目完整结题报告
├── demo_video_link.txt # 存放演示视频网盘公开链接
└── test_docs/ # 测试用示例 PDF 课件
