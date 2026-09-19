from .models import DJState


class DJAgent:

    def __init__(self, state: DJState):
        self.state = state

    def observe(self):
        print("\n--- OBSERVATION ---")

        print(f"Event: {self.state.event.event_type}")
        print(f"Location: {self.state.event.location}")
        print(f"Audience: {self.state.event.audience_size}")
        print(f"Mood: {self.state.audience.mood}")
        print(f"Energy: {self.state.audience.energy}")
        print(
            f"Preferred language: "
            f"{self.state.audience.preferred_language}"
        )

    def decide(self):

     mood = self.state.audience.mood
     energy = self.state.audience.energy
     language = self.state.audience.preferred_language

     if language == "Telugu" and energy > 0.75:
        return "High-energy Telugu dance song"

     if language == "Hindi" and energy > 0.75:
        return "High-energy Bollywood dance song"

     if mood.lower() == "nostalgic":
        return "Nostalgic classic song"

     if mood.lower() == "relaxed":
        return "Relaxing melody"

     return "Popular crowd-friendly song"

    def act(self):
        selected_song = self.decide()

        self.state.current_song = selected_song

        self.state.recently_played.append(selected_song)

        print("\n--- ACTION ---")
        print(f"Selected: {selected_song}")