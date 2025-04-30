class NolaAgent:
    def __init__(self):
        self.commands = {
            "create_folder": self.create_folder,
            "log_thought": self.log_thought
        }

    def handle(self, command):
        if command in self.commands:
            return self.commands[command]()
        return f"Команда '{command}' не распознана."

    def create_folder(self):
        import os
        folder = "nola_agent_folder"
        os.makedirs(folder, exist_ok=True)
        return f"Папка '{folder}' создана."

    def log_thought(self):
        from datetime import datetime
        with open("thought_log.txt", "a") as f:
            f.write(f"{datetime.now()}: Временной импульс зафиксирован.\n")
        return "Мысль записана."