from machine import I2C,Pin
import time
i2c = I2C(1)
s   =b'00000000'#0
m   =b'00000000'#0
hour=b'00100010'#23
day =b'00000111'#7
date=b'00101000'#28
mes =b'00010010'#12
ano =b'00100011'#23
i2c.writeto_mem(104,0,s,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,1,m,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,2,hour,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,3,day,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,4,date,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,5,mes,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,6,ano,addrsize=8)
time.sleep_ms(200)
s1   =b'10000111'#7segundos
m1   =b'10000000'#0
hour1=b'10100010'#23
day1 =b'11000111'#7
i2c.writeto_mem(104,7,s1,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,8,m1,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,9,hour1,addrsize=8)
time.sleep_ms(200)
i2c.writeto_mem(104,10,day1,addrsize=8)
time.sleep_ms(200)
cont_reg=14
in=b'00000101'
i2c.writeto_mem(104,cont_reg,in,addrsize=8)
time.sleep_ms(300)
