from dataclasses import dataclass


@dataclass
class UniqueEntity:
    id: str
    created_at: int
    modified_at: int
