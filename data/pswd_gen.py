# TEST, NO USE
import random, string

chs = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate(length = 45):
    
	random.shuffle(chs)
	pswsd = []
	for i in range(length):
		pswsd.append(random.choice(chs))
	random.shuffle(pswsd)
	
	return "".join(pswsd)