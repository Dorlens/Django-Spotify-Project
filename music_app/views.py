from django.shortcuts import render
from .spotifyApi_Info import sp
from .models import Music_tracks
import random



# Create your views here.
def home(request):
    return render(request,"frontend/home.html")

def random_track(request):

    track_id = ["72TFWvU3wUYdUuxejTTIzt",
                "7qiZfU4dY1lWllzX7mPBI3",
                "0tgVpDi06FyKpA1z0VMD4v",
                "6sy3LkhNFjJWlaeSMNwQ62",
                "0nrRP2bk19rLc0orkWPQk2",
                "4P0osvTXoSYZZC2n8IFH3c",
                "45J4avUb9Ni0bnETYaYFVJ",
                "2u9S9JJ6hTZS3Vf22HOZKg",
                "4HlFJV71xXKIGcU3kRyttv",
                "2igwFfvr1OAGX9SKDCPBwO",
                "4PTG3Z6ehGkBFwjybzWkR8",
                "3U4isOIWM3VvDubwSI3y7a",
                "7BqBn9nzAq8spo5e7cZ0dJ",
                "1MtUq6Wp1eQ8PC6BbPCj8P",
                "4kGlAkGC58crFvxfegBhNs",
                "3dfjuBGJVTCrMy1jwCzWV9", 
                "6dOtVTDdiauQNBQEDOtlAB",
                "6jg5SRvdGxvJ0DzNV0UqEK",

                ]
    

    track_id = random.choice(track_id)

    
    
    results = sp.track(track_id)
    track_title = results.get('name')
    artist_name = results.get("artists",[{"name": "unknown artist"}])[0]["name"]
    preview_url = results.get("preview_url",None)
    cover_image = results.get("album",{}).get("images",[{}])[0].get("url",None)
    
    print({preview_url})
    # Rest of your code...

   
    Music_tracks.objects.create(
        title=track_title,
        artist=artist_name,
        preview_url=preview_url,
        cover_image=cover_image,
        
        
        )

    
    context= {
        "track_name": track_title,
        "artist_name": artist_name,
        "preview_url": preview_url,
        "album_image": cover_image,
        "track_id": track_id
       }
    return render(request, "Frontend/base.html",{'track_id': track_id, **context})
            
                