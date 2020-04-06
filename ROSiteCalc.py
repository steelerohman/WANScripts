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

ip_cameras = 0
int(ip_cameras)

ip_camera_bw = 0
int(ip_camera_bw)

vc_units = 0
int(vc_units)

bw_total = 0
int(bw_total)

vc_bandwidth = 0
int(vc_bandwidth)

vc_units = input('Enter the number of VC units: ')  # Input from CLI

vc_bandwidth = int(vc_units)*2400 # Multiply by 2400Kbps
vc_bandwidth = int(vc_bandwidth)/1000  # Convert from Kbps --> Mbps


ip_cameras = input('Enter the number of IP cameras: ')  # Input from CLI

ip_camera_bw = int(ip_cameras) * .368
#ip_camera_bw = int(ip_camera_bw)/1000  # Convert from Kbps --> Mbps

print ('')
print ('')
print ('')
print ('-------------------Bandwidth Results------------------------')
print ('------------------------------------------------------------')
print ('')
print ('')
print ('')

print ('Total IP camera bandwidth required:',ip_camera_bw,'Mbps')
print ('Total video bandwidth required:',vc_bandwidth,'Mbps')


bw_total = int(vc_bandwidth + ip_camera_bw) / .15  #Video BW considered 15% of total BW


bw_total = round_up(bw_total,1)
bw_total_rounded = round_up(bw_total,-1)

print ('')
print ('Total site bandwidth required(not rounded):',bw_total,'Mbps')
#print (bw_total)


print ('')
print ('Total site bandwidth required(rounded):',bw_total_rounded,'Mbps')
