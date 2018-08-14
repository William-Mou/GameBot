class game:
    def __init__(self, chat_id):
        self.group = {}
        self.chat_id = chat_id
    def input(self, command, msg):
        if command[0] == "join":
            self.join(msg["from"]["id"], msg["from"]["username"])

    def join(self, user_id, username):
        self.group[user_id] = username
    
    def start(self):
        pass
    
    