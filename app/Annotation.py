class Annotation:
    CLASSES = ["Notehead", "Staff", "StaffMeasure"]  #TODO: pridat do skriptu obou, kde se vola pro cele pole

    def __init__(
        self, 
        cls: str, 
        x: int, 
        y: int, 
        width: int, 
        height: int
    ):
        self.cls = cls
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def to_json(self) -> dict:
        return {
            "class": self.cls,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }