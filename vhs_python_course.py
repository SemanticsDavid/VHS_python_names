 #!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import generators
import numpy as np
import random
import unicodedata
import codecs


# Knuth-Morris-Pratt string matching
# David Eppstein, UC Irvine, 1 Mar 2002

def KnuthMorrisPratt(text, pattern):

    '''Yields all starting positions of copies of the pattern in the text.
Calling conventions are similar to string.find, but its arguments can be
lists or iterators, not just strings, it returns all matches, not just
the first one, and it does not need the whole text in memory at once.
Whenever it yields, it will have read the text exactly up to and including
the match that caused the yield.'''
    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)

    # build table of shift amounts
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift

    # do the actual search
    startPos = 0
    matchLen = 0
    for c in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != c:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            yield startPos

def fibonacci(n):
    i0 = 1
    i1 = 1
    i_new = 2
    fibo_list = np.zeros(n)
    for i in xrange(n):
        i0 = i1
        i1 = i_new
        i_new += i0
        fibo_list[i] = i_new
    return fibo_list

def MillerRabin(n, k):

    # write n - 1 as a product of an odd number and a power of 2:

    m = n - 1
    c = 0

    while m % 2 == 0:
        c = c + 1
        m = m/2

    # now m is odd and n - 1 = (2^c) * m.

    #print "%d - 1 = (2^%d) * %d \n" % (n, c, m)

    #print "c = %d, m = %d \n" %(c, m)

    # generate and test k random samples:

    for i in range(k):
        #print n
        a = random.randint(2, n-2)

        #print "Sample %d of %d: a = %d" % (i+1, k, a)

        x = pow(a, m, n)
        #print "\t a^m = %d^%d = %d (mod %d)" % (a, m, x, n)

        # if a^m = 1 or -1 (mod n), then the Miller-Rabin condition is satisfied for the current sample a.
        # then we've learned that this a doesn't rule out primality of n, so we're done with this sample.

        if x == 1 or x == n - 1:
            #print "    ---> a = %d satisfies the Miller-Rabin condition \n" % a
            return 1

        elif c == 1:

            # if c = 1 then a^m was our only chance to satisfy the condition. since we ended up here, a^m didn't satisfy.

            #print "    ---> a = %d does not satisfy the Miller-Rabin condition \n" % a
            #return "definitely composite"
            return 0

         # otherwise, repeatedly square x until we get one of several informative results.
        # this loop will check a^(2*m), a^(4*m), .... ,a^(2^(c-1)*m) until either:
        # one of them is congruent to -1 (mod n) (so that the sample a DOESN'T rule out primality of n), OR
        # it's shown that none of them are congruent to -1 (mod n) (so that the sample a DOES rule out primality).

        else:
            for j in range(1, c):

                # reassign x to its square (mod n)

                x = pow(x, 2, n)
                #print "\t a^((2^%d) * m) = %d^%d = %d (mod %d)" % (j, a, (2**j) * m, x, n)

                # if the new x is congruent to -1 (mod n), then the Miller-Rabin condition is satisfied for a, so
                # the sample a DOESN'T rule out primality of n. now we're done with this sample.

                if x == n - 1:
                    #print "    ---> a = %d satisfies the Miller-Rabin condition \n" % a
                    break

                # if the new x is congruent to 1 (mod n), then we've found some number (the previous value of x)
                # which is NOT congruent to 1 or -1 (mod n), but whose square IS congruent to 1 (mod n),
                # so a DOES rule out primality of n.

                if x == 1:
                    #print "    ---> a = %d does not satisfy the Miller-Rabin condition \n" % a
                    #return "definitely composite"
                    return 0

                # if we get to j = c - 1 without finding some a^((2^j) * m) congruent to -1 (mod n), then
                # the sample a does NOT satisfy the Miller-Rabin condition, so a DOES rule out primality of n.

                if j == c - 1:
                    #print "    ---> a = %d does not satisfy the Miller-Rabin condition\n" % a
                    #return "definitely composite"
                    return 1

    # if we go through all k samples without ruling out primality, then declare that n is probably prime.

    return "probably prime"
def primes(n):
  nums = list(xrange(3, n+1, 2))
  nums_len = (n // 2) - 1 + (n % 2)
  idx = 0
  idx_sqrtn = (int(n**0.5) - 3) // 2
  while idx <= idx_sqrtn:
      nums_idx = (idx << 1) + 3
      for j in xrange(idx*(nums_idx+3)+3, nums_len, nums_idx):
          nums[j] = 0
      idx += 1
      while idx <= idx_sqrtn:
          if nums[idx] != 0:
              break
          idx += 1
  return [2] + [x for x in nums if x != 0]

def prime_names(name_list):
    prime_name_list = []
    for name in name_list:
        super_num = all_dict[name]
        #print name, super_num
        if MillerRabin(super_num, 12)==1:
            prime_name_list.append(name)
    return prime_name_list


def fibo_names(name_list, mod_num):
    fibo_name_list = []
    fibo_list = fibonacci(100)
    for name in name_list:
        super_num = all_dict[name]
        if super_num%mod_num in fibo_list:
            fibo_name_list.append(name)
    return fibo_name_list

def names_to_numbers(names_set, all_dict={}):
    lets = list('abcdefghijklmnopqrstuvwxyz')
    lets_index = {}
    for index, letter in enumerate(lets):
        lets_index[letter] = index
            #all_dict = {}
    for name in names_set:
        num_name = []
        for letter in list(name):
            letter = letter.lower()
            if letter in lets:
                num_name.append(str(lets_index[letter]))
        all_dict[name] = int(''.join(num_name))
    return all_dict

def prefi_freqs(name_list):
    start_freqs = {}
    for name in name_list:
        if len(name) > 2:
            prefi = name[:3]
            if prefi not in start_freqs.keys():
                start_freqs[prefi] = [1, name]
            else:
                start_freqs[prefi][0] += 1
                start_freqs[prefi].append(name)
    return start_freqs

def full_prefi_freqs(name_list):
    start_freqs = {}
    for line in name_list:
        name = line[0]
        #if (len(name) > 2) & (line[1]=='m'):
        if (len(name) > 2):
            prefi = name[:3]
            if prefi not in start_freqs.keys():
                if line[2]:
                    start_freqs[prefi] = [1, set(line[2][0]), name]
                else:
                    start_freqs[prefi] = [1, set(), name]
            else:
                start_freqs[prefi][0] += 1
                if line[2]:
                    start_freqs[prefi][1].add(line[2][0])
                start_freqs[prefi].append(name)

    for pref in start_freqs:
        start_freqs[pref][1] = ''.join(list(start_freqs[pref][1]))
    return start_freqs

def remove_accents(data):
    #data2 = unicode(data, errors='replace')
    return unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
    #return ''.join(x for x in unicodedata.normalize('NFKD', unicode(data2)) if x in data2.ascii_letters).lower()


if __name__ == "__main__":

    names_set = set()
    all_list = []

    Pi = ''
    Pi_open = open('pi_10_million.txt', 'r')
    Pi_lines = Pi_open.readlines()
    for i in Pi_lines:
        Pi += i[:-1]
    #names_set.add('nori')
    #a = names_to_numbers(names_set)
    #print Pi.index(str(a['nori']))

    prenoms_list = []
    prenoms_open = codecs.open('Prenoms.csv','r','utf-8')
    prenoms = prenoms_open.readlines()
    for line in prenoms[:]:
        #line = [x.lower() for x in line]
        line = line.lower()
        name = remove_accents(line.split(',')[:3][0])
        if name not in names_set:
            names_set.add(name)
            prenoms_list.append(line.split(',')[:3])
            all_list.append(line.split(',')[:3])
    #for name in prenoms_list:
        #names_set.add(name[0])

    counter = 0
    prefis = full_prefi_freqs(prenoms_list)
    for prefi in prefis.keys():
        #if prefis[prefi][0] > 5:
        if len(prefis[prefi][1]) >= 1:
            names = ''
            for name in prefis[prefi][2:]:
                names += name+', '
            print prefi, prefis[prefi][1],
            print names
            print '\n'
            counter +=  1
    print 'total = ', counter
    print remove_accents(prefis[prefi][2])
