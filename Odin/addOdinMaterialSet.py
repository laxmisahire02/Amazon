#!/usr/bin/env python
 
import sys
import commands
  
  # Make sure we have enough command line arguments
args = sys.argv[1:]
if len(args) != 2:
        print "Description-Adds all specified material sets to each of the specified host classe"
        sys.exit()
                 
                 # Read material sets & host classes
material_sets = [line.strip() for line in open (args[0], 'r').readlines()]
host_classes = [line.strip() for line in open (args[1], 'r').readlines()]
                  
                  # Template command
odin_cmd = '/apollo/env/OdinTools/bin/odin adminapi AddMSToHost -n %s -h %s/HostClass'
                   
                   # Run commands
print 'Running odin commands, adding material sets one host at a time...'
print '============================================\n'
for host in host_classes:
        for ms in material_sets:        
                print odin_cmd % (ms, host)
                print "TOOL OUTPUT: (blank if successful)"
                print commands.getoutput(odin_cmd % (ms, host))

print '\n\nDone.'
