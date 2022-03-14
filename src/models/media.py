class Media:
    def __init__(self, media_key, media_type, media_url) -> None:
        self._media_key = media_key
        self._media_type = media_type
        self._media_url = media_url

    def get_media_key(self) -> str:
        return self._media_key

    def get_media_type(self) -> str:
        return self._media_type
    
    def get_media_url(self) -> str:
        return self._media_url

    def __str__(self) -> str:
        return f"{self._media_key} - {self._media_type} - {self._media_url}"
