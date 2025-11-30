# ai-travel-concierge-agent
A multi-agent travel planning system using Gemini, custom MCP tools and memory. Automates itinerary creation, flight/hotel search, cost estimation and scheduling. Capstone project for Google AI Agents Intensive.
# AI Travel Concierge Agent 🧳🤖

A multi-agent AI system that automates end-to-end trip planning using Gemini, tools, memory, and agent orchestration.

This project is submitted as part of the **5-Day AI Agents Intensive Course with Google – Capstone Project (Concierge Agents Track)**.

---

## ✨ Overview

The AI Travel Concierge Agent takes a natural language request like:

> "Plan a 5-day budget trip to Japan in February under $1200. I like culture, anime, and local food."

and automatically:

- understands the user's intent and constraints
- searches for flights and transport options
- finds hotels that fit budget and location preferences
- plans a day-wise itinerary of activities, food, and experiences
- estimates costs and commute times
- outputs a final optimized travel plan

The system is built as a **multi-agent architecture** with:

- Sequential, parallel, and loop agents
- Built-in tools (search, code execution)
- Custom tools (distance, currency, weather)
- Session memory and long-term memory
- Basic logging and evaluation

---

## 🧠 Architecture

Core components:

- `TravelIntentAgent` — parse user query → structured travel request
- `FlightsAgent` — search flights and transport options
- `HotelsAgent` — find suitable stays
- `ActivitiesAgent` — build a daily itinerary
- `OrchestratorAgent` — coordinate all agents and build the final plan

Each agent is implemented in the `agents/` package and interacts via a simple Python orchestration layer.

Tools are defined in the `tools/` package and include:

- `DistanceTool` — approximate distance / travel time
- `CurrencyTool` — rough currency conversion
- `WeatherTool` — basic weather lookup (stub/mock)

Memory is handled in the `memory/` package:

- `SessionService` — per-conversation state
- `MemoryBank` — long-term preference storage

---

## 📂 Project Layout

```text
agents/         # Agent definitions (intent, flights, hotels, activities, orchestrator)
tools/          # Tools (distance, currency, weather)
memory/         # Session & long-term memory helpers
evaluation/     # Itinerary evaluation helpers
config/         # Settings & constants
main.py         # Entry point script
requirements.txt
README.md
