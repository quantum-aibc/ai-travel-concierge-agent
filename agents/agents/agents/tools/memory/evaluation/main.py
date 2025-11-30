from agents.orchestrator_agent import OrchestratorAgent


def print_plan(result):
    intent = result["intent"]
    print("\n=== TRAVEL PLAN SUMMARY ===")
    print(f"Destination: {intent.destination}")
    print(f"Budget: {intent.budget} {intent.currency}")
    print(f"Interests: {', '.join(intent.interests)}")
    print("\n-- Flights --")
    for f in result["flights"]:
        print(
            f"{f['from']} → {f['to']} | {f['airline']} | "
            f"{f['duration_hours']}h | {f['stops']} stop(s) | "
            f"{f['price']} {f['currency']}"
        )

    print("\n-- Hotels --")
    for h in result["hotels"]:
        print(
            f"{h['name']} in {h['area']} | {h['nightly_rate']} {h['currency']}/night | "
            f"{h['distance_to_center_km']} km from center | rating {h['rating']}"
        )

    print("\n-- Itinerary --")
    for day in result["itinerary"]:
        print(f"\nDay {day['day']}: {day['summary']}")
        for act in day["activities"]:
            print(f"  - [{act['time']}] {act['name']} ({act['type']})")

    print(f"\nItinerary Score: {result['itinerary_score']}")


def main():
    user_input = input("Describe your trip (destination, budget, interests, etc.):\n> ")
    orchestrator = OrchestratorAgent()
    result = orchestrator.run(user_input)
    print_plan(result)


if __name__ == "__main__":
    main()
