#
#  Take input from CLI and compute necessary site bandwidth
#  Video bandwidth will consist of 15% of the total bandwidth per WAN QoS policy
#
from pprint import pprint
import re
import math

def round_up(n, decimals):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

vc_units = 0
int(vc_units)

bw_total = 0
int(bw_total)


vc_bandwidth = 0
int(vc_bandwidth)

vc_units = input('Enter the number of VC units:')  # Input from CLI

vc_bandwidth = int(vc_units)*2400 # Multiply by 2400Kbps

vc_bandwidth = vc_bandwidth/1000  # Convert from Kbps --> Mbps

print ('Total video bandwidth required:',vc_bandwidth,'Mbps')

bw_total = int(vc_bandwidth) / .15  #Video BW considered 15% of total BW

bw_total_rounded = round(bw_total,-1)

print ('')
print (bw_total_rounded)


print ('')
print ('Total site bandwidth required:',bw_total_rounded,'Mbps')
