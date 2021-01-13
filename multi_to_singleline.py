#to run the program
#python multi_to_singleline.py file.fasta
import sys
import argparse
parser = argparse.ArgumentParser(description='This program converts multiline fasta to single line fasta without loading the entire file to memory.')
parser.add_argument(dest="infile", help='Multiline fasta file')
try:
 args= parser.parse_args()
 temp=""
 with open(args.infile) as infile:
    for line in infile:
        #if starting with > do nothing to the line but just print the header
        if '>' in line:
            if temp.strip(): #ignoring first empty line
                print(temp) #printing the last concatenated line
            header=line.rstrip()
            print(header) #printing header
            merged=""
        #if doesn't have
        else:

            sequence = line.rstrip()
            merged=merged+sequence
            temp=merged #overwriting after each and every loop
            
            
 print(temp) #printing the last line

except:
#description of program
 pass
