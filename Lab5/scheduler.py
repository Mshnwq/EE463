#! /usr/bin/env python

import sys
from optparse import OptionParser
import random

parser = OptionParser()
parser.add_option("-s", "--seed", default=0, help="the random seed", 
                  action="store", type="int", dest="seed")
parser.add_option("-j", "--jobs", default=3, help="number of jobs in the system",
                  action="store", type="int", dest="jobs")
parser.add_option("-l", "--jlist", default="", help="instead of random jobs, provide a comma-separated list of run times",
                  action="store", type="string", dest="jlist")
parser.add_option("-m", "--maxlen", default=10, help="max length of job",
                  action="store", type="int", dest="maxlen")
parser.add_option("-p", "--policy", default="FIFO", help="sched policy to use: SJF, FIFO, RR",
                  action="store", type="string", dest="policy")
parser.add_option("-q", "--quantum", help="length of time slice for RR policy", default=1, 
                  action="store", type="int", dest="quantum")

(options, args) = parser.parse_args()

random.seed(options.seed)

print ('ARG policy', options.policy)
if options.jlist == '':
    print ('ARG jobs', options.jobs)
    print ('ARG maxlen', options.maxlen)
    print ('ARG seed', options.seed)
else:
    print ('ARG jlist', options.jlist)

print ('')

print ('Here is the job list, with the run time of each job: ')

import operator

joblist = []
if options.jlist == '':
    for jobnum in range(0,options.jobs):
        runtime = int(options.maxlen * random.random()) + 1
        joblist.append([jobnum, runtime])
        print ('  Job', jobnum, '( length = ' + str(runtime) + ' )')
else:
    jobnum = 0
    for runtime in options.jlist.split(','):
        joblist.append([jobnum, float(runtime)])
        jobnum += 1
    for job in joblist:
        print ('  Job', job[0], '( length = ' + str(job[1]) + ' )')
print ('\n')

print ('Compute the turnaround time, response time, and wait time for each job.')
print ('You can use -s <somenumber> or your own job list (-l 10,15,20 for example)')
print ('to generate different problems for yourself.')
print ('')



