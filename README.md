# Architecture

Course work for software architecture and design patterns — focused on the **Observer** pattern via a weather-station demo, plus notes on finite state machines.

## What this repo contains

| File | Purpose |
|------|---------|
| `weather_station.py` | Observer-pattern weather station (runnable) |
| `weather_data1.py` | Tightly coupled “before” sketch (not runnable as-is) |
| `Design Patterns - Observer Pattern.docx` | Lab brief (Weather-O-Rama / Head First style) |
| `Finite State Machine.docx` | FSM lesson and Python exercises |
| `Intro to Software Architecture & Design Patterns.pptx` | Lecture slides |

## Requirements

- Python 3.x (stdlib only — no extra packages)

## Setup

```bash
git clone https://github.com/Joshkaki00/Architecture.git
cd Architecture
```

## Usage

```bash
python3 weather_station.py
```

You should see current conditions, temperature stats (avg/max/min), and a simple forecast for each measurement update. After the current-conditions display unregisters, only stats and forecast print for the final reading.

## How it works

`WeatherData` is the **Subject**. Displays (`CurrentConditionsDisplay`, `StatisticsDisplay`, `ForecastDisplay`) are **Observers**. When measurements change, registered observers update automatically. Displays register themselves on construction; any of them can unregister later.

`weather_data1.py` shows the problem Observer solves: hard-coded updates to each display inside `measurementsChanged`.
