from .models import Event, Audience, DJState
from .agent import DJAgent


def get_required_input(prompt: str) -> str:
    """Prompt until the user supplies a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def get_energy() -> float:
    """Prompt for an audience-energy value between 0 and 1."""
    while True:
        try:
            energy = float(input("Audience energy (0-1): ").strip())
            if 0 <= energy <= 1:
                return energy
        except ValueError:
            pass
        print("Energy must be a number between 0 and 1.")


def main():
    print("Enter event details")
    event_type = get_required_input("Event type: ")
    location = get_required_input("Location: ")
    mood = get_required_input("Audience mood: ").lower()
    energy = get_energy()
    preferred_language = get_required_input("Preferred language: ").title()

    event = Event(
        event_type=event_type,
        location=location,
        audience_size=200,
        languages=["Telugu", "Hindi", "English"],
    )

    audience = Audience(
        mood=mood,
        energy=energy,
        preferred_language=preferred_language,
    )

    state = DJState(
        event=event,
        audience=audience,
    )
    agent = DJAgent(state)

    agent.observe()
    agent.act()

    print("\n--- FINAL STATE ---")
    print(f"Current song: {state.current_song}")
    print(f"Recently played: {state.recently_played}")


if __name__ == "__main__":
    main()
