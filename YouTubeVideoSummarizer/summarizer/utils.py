import os
import openai
from typing import Literal
import assemblyai as aai
from pathlib import Path
from pytubefix import YouTube
from pytubefix.cli import on_progress

from dotenv import load_dotenv

from django.conf import settings

from summarizer.constants import (
     BLOG_PROMPT,
     SUMMARY_PROMPT,
     OPENAI_MODEL
)

load_dotenv()


def download_audio_title(link: str):
    yt = YouTube(link, on_progress_callback = on_progress)
    ys = yt.streams.get_audio_only()
    ys.download(mp3=True, output_path=settings.MEDIA_ROOT)
    audio_file = os.path.join(settings.MEDIA_ROOT, f"{yt.title}.mp3")
    # # base, ext = os.path.splitext(audio_file)
    # # os.rename(audio_file, new_file:=f"{base}.mp3")
    # yt_title = yt.title
    return audio_file, yt.title


def audio_to_text(file_path:Path) -> str:
        aai.settings.api_key = os.getenv("ASSEMBLY_API_KEY")
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(file_path)
        return transcript.text
    
def generate_summary(transcript:str, content_type:Literal["blog", "summary"]="summary") -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if content_type == "blog":
        prompt = BLOG_PROMPT.format(transcript=transcript)
    else:
        prompt = SUMMARY_PROMPT.format(transcript=transcript)
    
    response = openai.completions.create(
         model=OPENAI_MODEL,
         prompt=prompt,
         max_tokens=1500
    )

    return response.choices[0].message['content']
         