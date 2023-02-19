#! /usr/bin/env python

import sys
from optparse import OptionParser
import random
import math

def mustbepowerof2(bits, size, msg):
    if math.pow(2,bits) != size:
        print ('Error in argument: %s' % msg)
        sys.exit(1)

def mustbemultipleof(bignum, num, msg):
    if (int(float(bignum)/float(num)) != (int(bignum) / int(num))):
        print ('Error in argument: %s' % msg)
        sys.exit(1)

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
parser.add_option('-A', '--addresses', default='-1',
                  help='a set of comma-separated pages to access; -1(one) means randomly generate', 
                  action='store', type='string', dest='addresses')
parser.add_option('-s', '--seed',    default=0,     help='the random seed',                               action='store', type='int', dest='seed')
parser.add_option('-a', '--asize',   default='32k', help='address space size (e.g., 16, 32k, 64m, 1g)',   action='store', type='string', dest='asize')
parser.add_option('-r', '--realmem', default='128k', help='real memory size (e.g., 16, 128k, 32m, 1g)', action='store', type='string', dest='rsize')
parser.add_option('-p', '--pagesize', default='4k', help='page size (e.g., 4k, 8k, ... etc.)',            action='store', type='string', dest='pagesize')
parser.add_option('-n', '--numaddrs',  default=5,  help='no. virtual addresses to generate',       action='store', type='int', dest='num')
parser.add_option('-u', '--used',       default=50, help='percent of virtual address space used', action='store', type='int', dest='used')
parser.add_option('-v',                             help='verbose mode',                                  action='store_true', default=True, dest='verbose')


(options, args) = parser.parse_args()

print ('ARG seed',               options.seed)
print ('ARG address space size', options.asize)
print ('ARG real memory size',   options.rsize)
print ('ARG page size',          options.pagesize)
print ('ARG verbose',            options.verbose)
print ('ARG addresses',          options.addresses)
print ('')

random.seed(options.seed)

asize    = convert(options.asize)
rsize    = convert(options.rsize)
pagesize = convert(options.pagesize)
addresses = str(options.addresses)

if rsize <= 1:
    print ('Error: must specify a non-zero real memory size.')
    exit(1)

if asize < 1:
    print ('Error: must specify a non-zero address-space size.')
    exit(1)

if rsize <= asize:
    print ('Error: real memory size must be GREATER than address space size (for this simulation)')
    exit(1)

if rsize >= convert('1g') or asize >= convert('1g'):
    print ('Error: must use smaller sizes (less than 1 GB) for this simulation.')
    exit(1)

mustbemultipleof(asize, pagesize, 'address space must be a multiple of the pagesize')
mustbemultipleof(rsize, pagesize, 'real memory must be a multiple of the pagesize')

# print some useful info, like the darn page table 
pages = rsize // pagesize;
import array
used = array.array('i')
pt   = array.array('i')
for i in range(0,pages):
    used.insert(i,0)
vpages = asize // pagesize

# now, assign some pages of the VA
vabits   = int(math.log(float(asize))/math.log(2.0))
mustbepowerof2(vabits, asize, 'address space must be a power of 2')
pagebits = int(math.log(float(pagesize))/math.log(2.0))
mustbepowerof2(pagebits, pagesize, 'page size must be a power of 2')
vpnbits  = vabits - pagebits
pagemask = (1 << pagebits) - 1

# import ctypes
# vpnmask  = ctypes.c_uint32(~pagemask).value
vpnmask = 0xFFFFFFFF & ~pagemask
#if vpnmask2 != vpnmask:
#    print ('ERROR')
#    exit(1)
# print ('va:%d page:%d vpn:%d -- %08x %08x' % (vabits, pagebits, vpnbits, vpnmask, pagemask))

print ('')
print ('The format of the page table is simple:')
print ('The high-order (left-most) bit is the VALID bit.')
print ('  If the bit is 1, the rest of the entry is the PFN.')
print ('  If the bit is 0, the page is not valid.')
##print ('Use verbose mode (-v) if you want to print the VPN # by')
##print ('each entry of the page table.')
print ('')

print ('Page Table (from entry 0 down to the max size)')
for v in range(0,vpages):
    done = 0
    while done == 0:
        if ((random.random() * 100.0) > (100.0 - float(options.used))):
            u = int(pages * random.random())
            if used[u] == 0:
                done = 1
                # print ('%8d - %d' % (v, u))
                if options.verbose == True:
                    print ('  [%8d]  ' % v, end='')
                else:
                    print ('  ', end='')
                print ('0x%08x' % (0x80000000 | u))
                pt.insert(v,u)
        else:
            # print ('%8d - not valid' % v)
            if options.verbose == True:
                print ('  [%8d]  ' % v, end='')
            else:
                print ('  ', end='')
            print ('0x%08x' % 0)
            pt.insert(v,-1)
            done = 1
print ('')            


#
# now, need to generate virtual address trace
#

addrList = []
if addresses == '-1':
    # need to generate addresses
    for i in range(0, options.num):
        n = int(asize * random.random())
        addrList.append(n)
else:
    addrList = addresses.split(',')


print ('Virtual Address Trace')
for vStr in addrList:
    # vaddr = int(asize * random.random())
    vaddr = int(vStr)
    print ('  VA 0x%08x (decimal: %8d) --> RA or invalid address? ____________\n\n' % (vaddr, vaddr))
print ('')

print ('For each virtual address, write down the real address it translates to')
print ('OR write down that it is an out-of-bounds address (e.g., Not Valid).')
print ('')







