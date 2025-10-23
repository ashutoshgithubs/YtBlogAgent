from crewai_tools import YoutubeChannelSearchTool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["CHROMA_OPENAI_API_KEY"] = "dummy_key"

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="llama3.2:1b",
            ),
        ),
        embedder=dict(
            provider="ollama",
            config=dict(
                model="llama3.2:1b",
                task_type="retrieval_document",
            ),
        ),
    )
)
