"""
🎬 YT2Blog AI - Utility Functions
Made with 💜 by Vivi ✨
"""

import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ==========================================
# 1️⃣ EXTRACT VIDEO ID FROM URL
# ==========================================
def extract_video_id(url: str) -> str | None:
    """
    Extracts the YouTube video ID from various URL formats.
    
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://www.youtube.com/shorts/VIDEO_ID
    """
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"(?:embed\/)([0-9A-Za-z_-]{11})",
        r"(?:shorts\/)([0-9A-Za-z_-]{11})",
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


# ==========================================
# 2️⃣ FETCH YOUTUBE TRANSCRIPT
# ==========================================
def get_transcript(video_id: str) -> tuple[str | None, str | None]:
    """
    Fetches the transcript for a YouTube video.
    Returns: (transcript_text, error_message)
    """
    try:
        # New API (v1.x+) - create instance and call fetch()
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(
            video_id,
            languages=['en', 'en-US', 'en-GB']
        )
        
        # Combine all transcript snippets into one text
        full_text = " ".join([snippet.text for snippet in fetched_transcript])
        return full_text, None
        
    except TranscriptsDisabled:
        return None, "❌ Transcripts are disabled for this video."
    except NoTranscriptFound:
        return None, "❌ No English transcript found for this video."
    except Exception as e:
        return None, f"❌ Error fetching transcript: {str(e)}"


# ==========================================
# 3️⃣ INITIALIZE GROQ LLM
# ==========================================
def get_llm(temperature: float = 0.7):
    """
    Initializes the Groq LLM.
    Using llama-3.3-70b-versatile - FREE & POWERFUL! 💜
    """
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=temperature,
        api_key=os.getenv("GROQ_API_KEY"),
    )


# ==========================================
# 4️⃣ GENERATE BLOG POST
# ==========================================
def generate_blog_post(
    transcript: str, 
    tone: str = "Professional",
    length: str = "Medium"
) -> str:
    """
    Transforms a YouTube transcript into a beautiful blog post.
    
    Args:
        transcript: The video transcript text
        tone: Professional | Casual | Technical | Storytelling
        length: Short (~500 words) | Medium (~1000 words) | Detailed (~1500+ words)
    """
    
    # Length guide for the LLM
    length_guide = {
        "Short": "approximately 500 words",
        "Medium": "approximately 1000 words",
        "Detailed": "approximately 1500-2000 words"
    }
    
    # Tone descriptions
    tone_guide = {
        "Professional": "polished, authoritative, and business-appropriate",
        "Casual": "friendly, conversational, and approachable",
        "Technical": "detailed, precise, with technical depth",
        "Storytelling": "narrative-driven, engaging, with vivid descriptions"
    }
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are an expert content writer who transforms YouTube video transcripts 
into engaging, well-structured blog posts.

Your blog post must:
1. Have a catchy, SEO-friendly title (use # for H1)
2. Include an engaging introduction that hooks the reader
3. Use clear section headers (## for H2, ### for H3)
4. Include bullet points and numbered lists where appropriate
5. End with a strong conclusion and key takeaways
6. Use Markdown formatting throughout
7. Be {length_guide}
8. Have a {tone_guide} tone

Make it scannable, valuable, and shareable!"""),
        
        ("human", """Transform this YouTube transcript into a complete blog post:

TRANSCRIPT:
{transcript}

Generate the full blog post in Markdown format now:""")
    ])
    
    # Create the chain
    llm = get_llm(temperature=0.7)
    chain = prompt_template | llm
    
    # Generate the blog
    response = chain.invoke({
        "transcript": transcript,
        "length_guide": length_guide[length],
        "tone_guide": tone_guide[tone]
    })
    
    return response.content


# ==========================================
# 5️⃣ GENERATE SEO METADATA
# ==========================================
def generate_seo_metadata(blog_content: str) -> dict:
    """
    Generates SEO-friendly title and meta description for the blog.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an SEO expert. Generate SEO metadata for the given blog post.
Return ONLY in this exact format:

TITLE: <60-character SEO title>
META: <150-character meta description>
TAGS: <5 comma-separated tags>"""),
        ("human", "Blog post:\n\n{blog}")
    ])
    
    llm = get_llm(temperature=0.5)
    chain = prompt | llm
    response = chain.invoke({"blog": blog_content[:2000]})  # Use first 2000 chars
    
    # Parse the response
    result = {"title": "", "meta": "", "tags": ""}
    for line in response.content.split("\n"):
        if line.startswith("TITLE:"):
            result["title"] = line.replace("TITLE:", "").strip()
        elif line.startswith("META:"):
            result["meta"] = line.replace("META:", "").strip()
        elif line.startswith("TAGS:"):
            result["tags"] = line.replace("TAGS:", "").strip()
    
    return result

# ==========================================
# 6️⃣ GENERATE TWITTER THREAD 🐦
# ==========================================
def generate_twitter_thread(blog_content: str) -> str:
    """
    Converts the blog post into a viral Twitter/X thread.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a viral Twitter content creator.
Convert the blog post into a Twitter thread with these rules:

1. Start with a HOOK tweet that grabs attention (use emojis!)
2. Create 5-8 tweets total
3. Each tweet must be UNDER 280 characters
4. Number each tweet like: 1/ 2/ 3/ etc.
5. End with a CTA tweet asking for likes/retweets
6. Use line breaks within tweets for readability
7. Separate each tweet with a blank line and "---"

Format:
1/ [Hook tweet]

---

2/ [Tweet content]

---

(continue...)"""),
        ("human", "Blog post:\n\n{blog}")
    ])
    
    llm = get_llm(temperature=0.8)
    chain = prompt | llm
    response = chain.invoke({"blog": blog_content})
    return response.content


# ==========================================
# 7️⃣ GENERATE LINKEDIN POST 💼
# ==========================================
def generate_linkedin_post(blog_content: str) -> str:
    """
    Creates a professional LinkedIn post from the blog.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a LinkedIn content strategist.
Convert the blog post into an engaging LinkedIn post with:

1. A powerful HOOK in the first line (curiosity gap)
2. Short, punchy paragraphs (1-2 sentences each)
3. Use line breaks generously for readability
4. Include 3-5 key insights as bullet points
5. End with a thought-provoking question
6. Add 5 relevant hashtags at the bottom
7. Keep total length under 1300 characters
8. Use emojis strategically (not overdone)

Make it feel personal, valuable, and shareable!"""),
        ("human", "Blog post:\n\n{blog}")
    ])
    
    llm = get_llm(temperature=0.7)
    chain = prompt | llm
    response = chain.invoke({"blog": blog_content})
    return response.content