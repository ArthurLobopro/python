from time import sleep

second_counter = 0

ONE_SECOND = 1
ONE_MINUTE = 60 * ONE_SECOND
ONE_HOUR = 60 * ONE_MINUTE

def printTime():
    h, m, s = 0, 0, 0

    if second_counter >= ONE_HOUR:
        h = second_counter // ONE_HOUR

    hour_diference = h * ONE_HOUR

    if (second_counter - hour_diference) >= ONE_MINUTE:
        m = (second_counter - hour_diference) // ONE_MINUTE

    minute_diference = (m * ONE_MINUTE) + hour_diference

    if (second_counter - minute_diference) >= ONE_SECOND:
        s = (second_counter - minute_diference) // ONE_SECOND

    s = s if s >= 10 else f"0{s}"
    m = m if m >= 10 else f"0{m}"
    h = h if h >= 10 else f"0{h}"

    print(f"{h}:{m}:{s}",end = "")
    print("\r\r", end="")

while True:
    printTime()
    sleep(1)
    second_counter += 1