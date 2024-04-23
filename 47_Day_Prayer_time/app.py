import aladhan

client = aladhan.Client()
prayer = client.get_timings_by_address("London")

print("""
Prayer Times for London:
╔══════════════════════════╗
║ Fajr    : {prayer.fajr.time} ║
║ Dhuhr   : {prayer.dhuhr.time} ║
║ Asr     : {prayer.asr.time} ║
║ Maghrib : {prayer.maghrib.time} ║
║ Isha    : {prayer.isha.time} ║
╚══════════════════════════╝
""".format(prayer=prayer))


