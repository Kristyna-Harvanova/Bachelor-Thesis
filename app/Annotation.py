from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Annotation:
    CLASSES: ClassVar[List[str]] = ["Notehead", "Staff", "StaffMeasure"]  #TODO: pridat do skriptu obou, kde se vola pro cele pole

    cls: str
    x: int
    y: int 
    width: int
    height: int
    
    def to_json(self) -> dict:
        return {
            "class": self.cls,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }