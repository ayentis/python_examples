def make_readable(seconds):
    sec = seconds % 60
    hour = seconds // 3600
    min = (seconds % 3600) // 60

    print(f"{hour:02}:{min:02}:{sec:02}")


make_readable(0)# "00:00:00")
make_readable(5)# "00:00:05")
make_readable(60)# "00:01:00")
make_readable(86399)# "23:59:59")
make_readable(359999)# "99:59:59")