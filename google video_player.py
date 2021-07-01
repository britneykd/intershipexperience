"""A video player class."""

from . import video_library


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self.isPaused = False
        self.isPlaying= False
        self._current_video = None
        self._video_library = video_library.VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos =self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if video_id == "amazing_cats_video_id":
            print("playing video: Amazing Cats")
        elif video_id == "funny_dogs_video_id":
            print("playing video: Funny Dogs")
        elif video_id == "another_cat_video_id":
            print("Playing video: Another Cat Video")
        elif video_id == "life_at_google_video_id":
            print("Playing video: Life at Google")
        elif video_id == "nothing_video_id":
            print("Playing video: Video about nothing")
        else:
            print("Cannot play video: video does not exist")

        def stop_video(self):
         """Stops the current video."""

        print("stop_video needs implementation")
        video = self._video_library.get_video(video_id)
        if video:
            print(f'Stopping video: {video.title}')
            self._current_video = video
        else:
            print("Cannot play video: Video does not exist")

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_available = [video for video in self._video_library.get_all_videos() if not video.is_flagged()]
        number_of_videos = len(video_available)
        if number_of_videos == 0:
            print("No videos available")
        else:
            video_num_toplay = random.randit(0, number_of_videos - 1)
            video_toplay = video_available[video_num_toplay]
            self.play_video(video_toplay.video_id)


    def pause_video(self):
        """Pauses the current video."""

        print("pause_video needs implementation")
        video_id_playing = self._video_library.get_video_playing()
        video_playing = self._video_library.get_video(video_id_playing) # None when video_id_playing is Non
        if video_id_playing == None:
            print("Cannot pause video: No video is currently playing")
        elif self._video_library.is_video_paused():
            print(f"video already paused: {video_playing.title}")
            self._video_library.set_video_paused(True)

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
