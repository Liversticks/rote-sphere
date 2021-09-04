# Powerups

## What are powerups?
Our game tracks power and water usage over time for households/buildings. As we accumulate data over time from sensor readings, our game will detect usage patterns. If these patterns stand out in some way, we will send notifications to the end user.

Note: each sensor has a type and an UUID

## How would we actually measure usage?
This is a "big data" problem. Currently, our records are stored in a SQLite "database". In production, we would use more appropriate DBs and tools such as Apache Spark to periodically query and aggregate usage for each building/household and cache average usage per capita.

## Powerup list

### General
- All: Detect when usage per household/building is above/below the monthly mean by 20% (implemented in notifications.py)
- All: Seed the initial average water and power usage per capita over a time period, then compare each building's usage per capita throughout
- All: If the address has a unit number, it is likely a tenant and will not have access to some notifications (ie external renovations)

### Kitchen
Adapted from (Uswitch energy efficient cooking guide)[https://www.uswitch.com/energy-saving/guides/energy-efficient-cooking/]
- Type: oven --> if frequently used, encourage users to use a microwave or batch usage over a shorter period of time (so less energy needed to reheat the oven)
- Type: oven --> detect the type of the oven and recommend a convection/fan-based oven if not already present
- Type: stove --> if used for a prolonged period of time, recommend a pressure cooker or slow cooker instead

### Bathroom
- Type: sink --> if reporting frequent readings, recommend checking for leaks
- Type: toilet --> if reporting frequent readings, recommend checking for leaks
- Type: shower/bath --> if reporting a large volume of water consumed at once, recommend taking a shower instead
- Type: shower --> if reporting over a too-long time period, recommend taking shorter showers

### Laundry
- Type: dryer --> if used, recommend air-drying
- Type: washer --> if energy usage is beyond that of cool water, recommend using cooler water
- Type: washer --> if used too frequently (based on number of occupants), recommend less frequent but fuller loads

### Shared
- Type: hot water tank --> if exceeding mean energy use per capita, recommend using cooler water
- Type: thermostat --> if temperature is set too high/low leading to elevated energy use, recommend gradually adjusting temperature towards a level that reduces energy use
- Type: lights --> if during daylight hours (calculated by location), recommend opening curtains/blinds to maximize natural light

### Electronics
- Type: all --> If reporting sustained low energy usage, recommend unplugging (curb phantom power use)

### Outside the house
- All: Based on the provided location, recommend a rain barrel if located in an area with frequent rainfall
- Type: hose --> recommend watering in the morning if high usage detected during the rest of day (source)[https://www.scotts.com/en-ca/library/watering/lawn-watering-tips-when-best-time-water-your-lawn]
- Type: hose --> recommend using drip irrigation if water usage is consistently high (less water lost to evaporation)
- Type: special --> based on location, if there are no negative readings for power, recommend installing solar panels (can feed power back into the grid)