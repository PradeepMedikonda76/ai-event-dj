from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Event:
    event_type: str
    location: str
    audience_size: int
    languages: List[str]


@dataclass
class Audience:
    mood: str
    energy: float
    preferred_language: str


@dataclass
class DJState:
    event: Event
    audience: Audience
    current_song: Optional[str] = None
    recently_played: List[str] = field(default_factory=list)
