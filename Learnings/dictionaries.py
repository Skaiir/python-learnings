month_conversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(month_conversions["Nov"])
print(month_conversions.get("Mar"))
print(month_conversions.get("Test", "Unknown"))
print(month_conversions.get("Jan", "Unknown"))