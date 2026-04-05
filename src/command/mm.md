### MM - Predefined System Variables

The `MM` namespace provides access to predefined read-only system variables and information functions that return information about the MMBasic environment, display, system resources, and device status.

## Display and Resolution Variables

- **MM.HRES**: Horizontal resolution of the display in pixels
- **MM.VRES**: Vertical resolution of the display in pixels
- **MM.HEIGHT**: Number of characters down the display with current font
- **MM.WIDTH**: Number of characters across the display with current font
- **MM.HPOS**: Horizontal position (pixels) after last graphics/print command
- **MM.VPOS**: Vertical position (pixels) after last graphics/print command

## System Information Functions

### MM.INFO() and MM.INFO$()

Returns various system information. Use `MM.INFO()` for integer results and `MM.INFO$()` for string results.

**Common queries:**
- `MM.INFO$(AUTORUN)` - OPTION AUTORUN setting
- `MM.INFO(ADC)` - Current ADC buffer ready to read (1 or 2, or 0 if none)
- `MM.INFO(ADC DMA)` - Whether ADC DMA is active (1 or 0)
- `MM.INFO(BOOT)` - Reason for last restart
- `MM.INFO(BOOT COUNT)` - Number of device restarts
- `MM.INFO(CPUSPEED)` - CPU speed in MHz
- `MM.INFO(DEVICE$)` - Device type string
- `MM.INFO(DISKSIZE)` - Total disk size
- `MM.INFO(DRIVE)` - Current drive letter
- `MM.INFO(ERRNO)` - Last error number
- `MM.INFO(EXISTS DIR ...)` - Whether directory exists
- `MM.INFO(EXISTS FILE ...)` - Whether file exists
- `MM.INFO(FREESPACE)` - Free disk space
- `MM.INFO(IP ADDRESS)` - Current IP address
- `MM.INFO(PATH)` - Current file path
- `MM.INFO(PINCOUNT)` - Number of GPIO pins

## System Subroutines

The following special subroutine names are recognized by MMBasic:

- **MM.STARTUP** - Called automatically when firmware starts or after reset
- **MM.WATCHDOG** - Indicates watchdog timeout restart
- **MM.PROMPT** - Called when command prompt is displayed
- **MM.END** - Called when program ends

## Example Usage

```basic
PRINT "Display: " MM.HRES "x" MM.VRES " pixels"
PRINT "Free space: " MM.INFO(FREESPACE) " bytes"
PRINT "Device: " MM.INFO$(DEVICE$)
```

## Cross-References

See [predefined_read_only_variables.md](../predefined_read_only_variables.md) for complete documentation of all MM.* predefined variables and functions.