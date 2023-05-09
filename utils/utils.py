
import datetime

from pytube.exceptions import AgeRestrictedError

class AgeRestrictedVideoException(Exception):
    
    def __init__(self, msg : str,*args: object) -> None:
        super().__init__(*args)
        self.msg = msg

def formatDuration(duration) -> str:
    duration_in_seconds = duration
    duration_in_minutes = duration_in_seconds // 60
    duration_in_seconds %= 60
    if duration_in_minutes > 60:
        duration = "%02d:%02d:%02d" % (duration_in_minutes // 60, duration_in_minutes - (duration_in_minutes // 60) * 60 ,duration_in_seconds)
        return duration
    else:
        duration = "%02d:%02d" % (duration_in_minutes ,duration_in_seconds)
        return duration