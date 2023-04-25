CHANNELS = ("BBC", "Discovery", "TV1000")

class TVController:
    def __init__(self, list_of_channels):
        self.list_of_channels = list_of_channels
        self.current_channel = CHANNELS[0]  # default channel

    def first_channel(self):
        self.current_channel = CHANNELS[0]
        print(f"First channel, {self.current_channel}, is turned on!")

    def last_channel(self):
        self.current_channel = CHANNELS[-1]
        print(f"Last channel, {self.current_channel}, is turned on!")

    def turn_channel(self, n):
        self.current_channel = CHANNELS[n-1]
        print(f"Channel number {n}, {self.current_channel}, is turned on!")

    def next_channel(self):
        if self.current_channel == CHANNELS[-1]:
            self.current_channel = CHANNELS[0]
            print(f"Next channel, {self.current_channel}, is turned on!")
        else:
            index_of_current_channel = CHANNELS.index(self.current_channel)
            self.current_channel = CHANNELS[index_of_current_channel + 1]
            print(f"Next channel, {self.current_channel}, is turned on!")

    def previous_channel(self):
        if self.current_channel == CHANNELS[0]:
            self.current_channel = CHANNELS[-1]
            print(f"The previous channel, {self.current_channel}, is turned on!")
        else:
            index_of_current_channel = CHANNELS.index(self.current_channel)
            self.current_channel = CHANNELS[index_of_current_channel - 1]
            print(f"The previous channel, {self.current_channel}, is turned on!")

    def our_current_channel(self):
        print(f"The current channel, {self.current_channel}, is turned on!")
        return self.current_channel

    def is_exist(self, identifier):
        if identifier in CHANNELS or identifier in range(1, len(CHANNELS)+1):
            print("Yes")
        else:
            print("No")


controller = TVController(CHANNELS)

controller.first_channel()              # == "BBC"
controller.last_channel()               # == "TV1000"
controller.turn_channel(1)              # == "BBC"
controller.next_channel()               # == "Discovery"
controller.previous_channel()           # == "BBC"
controller.our_current_channel()        # == "BBC"
controller.is_exist(4)                  # == "No"
controller.is_exist("BBC")              # == "Yes"
