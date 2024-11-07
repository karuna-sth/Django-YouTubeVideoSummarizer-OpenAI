from django.db.models.signals import post_save
from django.dispatch import receiver
from summarizer.models import Summary

from rest_framework import status
from rest_framework.response import Response

from summarizer.utils import (
    download_audio_title,
    audio_to_text,
    generate_summary
)


@receiver(post_save, sender=Summary)
def generator(sender, instance, **kwargs):
    url = instance.url
    content_type = instance.content_type

    audio_file, instance.title = download_audio_title(link=url)
    
    # generating transcription
    transcript = audio_to_text(audio_file)
    print(transcript)
    if not transcript:
        return Response(
            {"error": "No Transcript Generated"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # generating summary
    instance.summary = generate_summary(transcript=transcript, content_type=content_type)
    instance.save(update_fields=["summary", "title"])
