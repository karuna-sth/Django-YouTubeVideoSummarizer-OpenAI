OPENAI_MODEL="gpt-4o-mini"

SUMMARY_PROMPT = """Summarize the following YouTube transcript concisely. Identify and extract key ideas, themes, or main points in the form of bullet points where relevant. Maintain any distinct sections or lists mentioned by the speaker in a clear, bullet-pointed format, while ensuring the language is succinct and easy to understand.

Transcript:{transcript}"""


BLOG_PROMPT = """
Convert the following YouTube transcript into a well-structured blog post. Begin with an engaging introduction that provides context or background on the topic. Break down the content into clear paragraphs that flow logically, each covering a distinct point or section from the video. Conclude with a summary of the key takeaways or final thoughts.

The blog should be engaging and informative, using clear, reader-friendly language.

Transcript: {transcript}
"""