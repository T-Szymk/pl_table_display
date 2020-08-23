# pl_table_display

## [Git Link](https://github.com/T-Szymk/pl_table_display) 

## Overview
Self-contained display driven by MCU to show real-time status of the English Premier League (should be easily configurable to show other league tables).

## Architecture
- Raspberry Pi to host Flask web server.
- Pi to hold logic to retrieve and process data from the internet. 
- Pi will transmit data to MCU over UART (_this will become a wireless  protocol in the next phase_).
- MCU update a ~6" display to show data.
- Audio/Visual prompts will be driven by the MCU when a change is detected.
