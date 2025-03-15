import os
import fastf1
from fastf1.ergast import Ergast

# Create a cache dir
CACHE_DIR = "./cache_fast_f1"
if not os.path.exists(CACHE_DIR):
    os.mkdir(CACHE_DIR)

# Enable cache
fastf1.Cache.enable_cache(CACHE_DIR)

# # Load session
session = fastf1.get_session(
    year=2024, gp=12, identifier="Race"
)  # https://docs.fastf1.dev/events.html#sessionidentifier
session.load(telemetry=True, laps=True, weather=True)

# https://docs.fastf1.dev/core.html#fastf1.core.Session


# session name
session_results = session.results

# session date
session_date = session.date

# telemetry
car_telemetry = session.car_data

# Get lap information
lap_data = session.laps

# planned laps
planned_laps = session.total_laps

# Get Drivers (numbers)
drivers = session.drivers

# Get weather
weather = session.weather_data

# Positional Data
pos = session.pos_data

# session status
session_status = session.session_status

# session info
session_info = session.session_info

# results
session_results = session.results

# track status
track_status = session.track_status

# race control messages
race_control_messages = session.race_control_messages

# get driver
drivers_specific = session.get_driver(identifier="44")

# Circuit information
track_information = session.get_circuit_info()

# List event schedule
events = fastf1.get_event_schedule(year=2024)
event_specific_detail = events.get_event_by_round(12)


print(drivers_specific)
