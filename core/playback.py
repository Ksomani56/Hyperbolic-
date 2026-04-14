class PlaybackSystem:
    def __init__(self):
        self.actions = []
        self.is_playing = False
        self.is_paused = False
        self.play_index = 0
        self.animating_action = None
        self.anim_speed = 0.03 # Progress step per frame
        
    def add_action(self, action_type, **kwargs):
        if not self.is_playing:
            self.actions.append({"type": action_type, **kwargs})
            
    def start_playback(self):
        self.is_playing = True
        self.is_paused = False
        self.play_index = 0
        self.animating_action = None
        
    def toggle_pause(self):
        if self.is_playing:
            self.is_paused = not self.is_paused
            
    def stop_playback(self):
        self.is_playing = False
        self.is_paused = False
        self.animating_action = None
        
    def clear(self):
        self.actions = []
