class Annotation:
    def __init__(self, cls, x, y, width, height):
        self.cls = cls
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    CLASSES = ["Note"]  #TODO: pridat dalsi mozne tridy

    def to_json(self) -> dict:
        return {
            "class": self.cls,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }