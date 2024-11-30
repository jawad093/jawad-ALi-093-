class Multi_Reflex_Agent:
    def __init__(self, set_temp):
        self.set_temp = set_temp
        self.action_log = {} 

    def percept(self, room, temp):
        self.current_temp = temp 
        self.room = room  

    def act(self):
        
        if self.current_temp > self.set_temp:
            action = "Get the stove"  
        else:
            action = "Get the heater"  
        self.action_log[self.room] = {
            'current_temp': self.current_temp, 
            'action': action  
        }

        return action 

    def report(self):
        
        for room, info in self.action_log.items():
            print(f"In {room}: Current temperature = {info['current_temp']}°C - Action = {info['action']}")


Agent = Multi_Reflex_Agent(22)

room_tem = {
    "Living Room": 26,
    "Bedroom": 16,
    "Kitchen": 30 ,
}

for room, temp in room_tem.items():
    Agent.percept(room, temp)  
    action = Agent.act()  
    print(f"Current temperature in {room} is {temp}°C: {action}")  

Agent.report()  
