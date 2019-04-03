#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import emoji
cont = 0
for n in range(100,0,-1 ):
    print(n)
print(emoji.emojize(':heart:'*10,use_aliases=True).encode('utf-8').strip())
while cont <100:
    cont+=1
    print(cont)