"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.



"""


def rot13(message):
    #your code here
    tupla = ('a', 'e', 'i', 'o' , 'u', 'g')
    x = ""
    """
    a - i                   o - g
    e - o                   u - a
    i - u                   g - e
    iago - uieg

    """

    for c, k in enumerate(message):
        if k in tupla:
        
         print(c) # é o index   
         print(k) # é o valor 


