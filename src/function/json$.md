### JSON$(array%(), string$)

Returns a string representing a specific item out of the JSON input stored in the
longstring array%(). Note that many JSON data sets are quite large and may be
too big to parse with the memory available.

Examples (taken from api.openweathermap.org):

```basic
JSON$(a%(), “name”)
JSON$(a%(), “coord.lat”)
JSON$(a%(), “weather[0].description”)
JSON$(a%(),”list[4].weather[0].description
```

