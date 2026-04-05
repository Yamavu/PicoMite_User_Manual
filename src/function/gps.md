# GPS Functions

The GPS functions are used to return data from a serial communications channel opened as GPS. The function GPS(VALID) should be checked before any of these functions are used to ensure that the returned value is valid.

## Position Functions

{{#include gps_latitude.md}}

{{#include gps_longitude.md}}

{{#include gps_altitude.md}}

## Time Functions

{{#include gps_date.md}}

{{#include gps_time.md}}

## Navigation Functions

{{#include gps_speed.md}}

{{#include gps_track.md}}

## Quality and Accuracy Functions

{{#include gps_fix.md}}

{{#include gps_satellites.md}}

{{#include gps_dop.md}}

{{#include gps_geoid.md}}

## Status Functions

{{#include gps_valid.md}}
