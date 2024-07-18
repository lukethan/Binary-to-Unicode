# CS50 Bulbs to Unicode
##### by: Luke O'Neil

### Description:
While taking CS50x 2024, I would look at a lecture image of the bulbs, record them by hand, group them into sets of 8, convert the bytes from binary to decimal, and then convert from decimal to unicode. 
I decided this was tedious so I started off by writing a program that would take the 64 bits and return a dictionary with 8 byte lists as its values. After that, I challenged myself to iterate through each list and convert the binary to
decimal and print the number (called total). My final change was printing out the corresponding unicode character using chr(total) to print the character rather than the numerical value.

I am new to coding in python so I am sure the code isn't optimized, but I hope it is readable enough. Looking to share with folks who want to double check the conversions they did or have it done automatically 
for them.

Cheers!
