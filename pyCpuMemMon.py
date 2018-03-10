import psutil as pu
import platform as pf

def print_prompt():
	print ("=" * 50)

hostname = pf.uname()[1]
cpu = pu.cpu_percent(interval=1)
mem = pu.virtual_memory().percent
swap = pu.swap_memory().percent
disk = pu.disk_usage('/').percent

print_prompt()
print ('%s \t %s \t %s \t %s \t %s' % ("HOSTNAME", "CPU", "MEM", "SWAP", "DISK"))
print ('%s \t %.2f \t %.2f \t %.2f \t %.2f' % (hostname, cpu, mem, swap, disk))
print_prompt()
