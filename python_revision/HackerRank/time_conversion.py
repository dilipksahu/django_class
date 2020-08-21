'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Sample Input 0

07:05:45PM

Sample Output 0

19:05:45
'''





def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]
    elif s[-2:] == 'AM':
        return s[:-2]
    elif s[-2:] == 'PM' and s[:2] == "12": 
        return s[:-2]
    else:
        return str(int(s[:2])+ 12) + s[2:8]

s = input()

result = timeConversion(s)

print(result)
