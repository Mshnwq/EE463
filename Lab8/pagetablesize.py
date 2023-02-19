#! /usr/bin/env python

import sys
from optparse import OptionParser
import random
import math

def convert(size):
    length = len(size)
    lastchar = size[length-1]
    if (lastchar == 'k') or (lastchar == 'K'):
        m = 1024
        nsize = int(size[0:length-1]) * m
    elif (lastchar == 'm') or (lastchar == 'M'):
        m = 1024*1024
        nsize = int(size[0:length-1]) * m
    elif (lastchar == 'g') or (lastchar == 'G'):
        m = 1024*1024*1024
        nsize = int(size[0:length-1]) * m
    else:
        nsize = int(size)
    return nsize


#
# main program
#
parser = OptionParser()
parser.add_option("-v", "--vasize", default="32",
                  help="bits in virtual address (e.g., 16, 20, 32)", 
                  action="store", type="string", dest="vsize")
parser.add_option("-e", "--ptesize", default="4",
                  help="size of the page table entry (e.g., 4 bytes)", 
                  action="store", type="string", dest="ptesize")
parser.add_option("-p", "--pagesize", default="4k",
                  help="size of the page (e.g., 4k, 4096, 1m)", 
                  action="store", type="string", dest="pagesize")


(options, args) = parser.parse_args()

print ("ARG bits in virtual address", options.vsize)
print ("ARG page size", options.pagesize)
print ("ARG pte size", options.ptesize)
print ("")

vsize    = int(options.vsize)
ptesize  = int(convert(options.ptesize))
pagesize = int(convert(options.pagesize))

# check: is page size a power of 2?
offbits = int(math.log(float(pagesize))/math.log(2.0))
if math.pow(2,offbits) != pagesize:
    print ('Error in argument -p (pagesize): Must be a power of 2\n')
    sys.exit(1)

print ('Compute how big a linear page table is with the characteristics you see above.\n')
print ('REMEMBER: There is one linear page table *per process*.')
print ('Thus, the more running processes, the more of these tables we will need.')
print ('However, for this problem, we are only concerned about the size of *one* table.\n')

print ('Recall that an address has two components: ')
print ('[ Virtual Page Number (VPN) | Offset ]')
print ('')
print ('The number of bits in the virtual address is: ________ bits\n')
print ('\nThe page size is: ________ bytes\n')
print ('\nThus, the number of bits needed in the offset is: ________ bits\n')
print ('\nWhich leaves this many ________ bits for the VPN\n')
print ('Thus, a virtual address looks like what?')
print ('Write V for a VPN bit and O for an offset bit below:\n\n\n')
print ('\nTo compute the size of the linear page table, we need to know:')
print ('\n  - The # of entries in the table, which is: ________ entry')
print ('\n  - The size of each page table entry, which is: ________ bytes\n')
print ('\nAnd then multiply them together to get the final result:\n')
print ('\n     ________ bytes\n')
print ('\n     ________ in KB\n')
print ('\n     ________ in MB')
    
    
    
    





