class Task :
    def __init__(self, content: str , category: str, xp: int) -> None:
        self.content = content
        self.category = category
        self.xp = xp
        self.done = False
    
    def displayTask(self) -> None:
        print(f"content: {self.content}--category: {self.category}--xp: {self.xp}")