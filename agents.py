from crewai import Agent
from tools import yt_tool

## Agent 1 for blog research from YouTube videos

blog_researcher=Agent(
    role='Channel Researcher',
    goal='Get the relevant video transcription for the topic {topic} from the provided Yt channel',
    verboe=True,
    memory=True,
    backstory=(
       """You are an expert channel researcher who specializes in extracting 
    and analyzing information from YouTube channels. You have a keen eye for detail 
    and can quickly identify key points and insights from video content across an entire channel."""
    ),
    tools=[yt_tool],
    allow_delegation=True
)

## Agent 2 for blog writing based on the research from YouTube videos

blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate a good tech story for the video on {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        """With a flair for simplifying complex topics, you craft
        engaging narratives that captivate and educate, bringing new
        discoveries to light in an accessible manner."""
    ),
    tools=[yt_tool],
    allow_delegation=False


)