from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Video(BaseModel):
    video_id: int
    video_name: str
    video_type: str
    video_url: str

video_list = [
    Video(video_id=1, video_name="ep1", video_type="episode", video_url="https://example.com/ep1"),
    Video(video_id=2, video_name="ep2", video_type="episode", video_url="https://example.com/ep2"),
    Video(video_id=3, video_name="ep3", video_type="episode", video_url="https://example.com/ep3"),
    Video(video_id=4, video_name="avatar", video_type="movie", video_url="https://example.com/avatar"),
    Video(video_id=5, video_name="titanic", video_type="movie", video_url="https://example.com/titanic"),
    Video(video_id=6, video_name="limitless", video_type="movie", video_url="https://example.com/limitless"),
]


@app.get("/")
def home():
    return {"message": "Welcome! Go for what you want to do."}


@app.get("/videos")
def get_videos():
    return {
        "message": "Here are your videos",
        "videos": video_list
    }


@app.post("/videos")
def add_video(video_name: str, video_type: str, video_url: str):

    # Check whether the video already exists
    for video in video_list:
        if (
            video.video_name == video_name
            and video.video_type == video_type
            and video.video_url == video_url
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This video already exists"
            )

    new_video = Video(
        video_id=len(video_list) + 1,
        video_name=video_name,
        video_type=video_type,
        video_url=video_url
    )
    video_list.append(new_video)
    return {
        "message": "Video added successfully",
        "video": new_video
    }


@app.get("/videos/{video_id}")
def get_video_by_id(video_id: int):

    for video in video_list:
        if video.video_id == video_id:
            return {
                "message": "Here is your video",
                "video": video
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Video with id {video_id} not found"
    )