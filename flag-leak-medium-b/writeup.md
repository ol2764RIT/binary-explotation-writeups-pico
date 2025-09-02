this code leaks flag off stack by doing a size bound read
vulnerable to a printf format string vulnerability

what is our game plan

track far enough where we leak parts of the code

guess and check method for %p 

leaks flag and parse it dynamically

flag!

picoCTF{L34k1ng_Fl4g_0ff_St4ck_rand}