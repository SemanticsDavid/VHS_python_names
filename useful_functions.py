def load_Pi():
    Pi = ''
    Pi_open = open('pi_10_million.txt', 'r')
    Pi_lines = Pi_open.readlines()
    for i in Pi_lines:
        Pi += i[:-1]
    return Pi

def generate_name_list(filename):
    name_list = []
    f_open = open(filename, 'r')
    f_lines = f_open.readlines()
    for name in f_lines:
        name_list.append(name[:-1].lower())
    return name_list

def number_letter_dict():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    num_let_dict = {}
    for i, let in enumerate(letters):
        num_let_dict[let] = str(i+1)
    return num_let_dict

def remove_symbols(name):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    simplified_name = ''
    for let in name.lower():
        if let in letters:
            simplified_name += let
    return simplified_name

def names_to_numbers(name):
    num_dict = number_letter_dict()
    coded_name = ''
    for let in name.lower():
        #print let
        coded_name += num_dict[let]
    return coded_name

if __name__ == "__main__":
    
    #start by writing your name here (replace tony), and find out if the number version
    #of your name can be found somewhere in the decimals of Pi
    i_num = names_to_numbers('pascale')
    Pi = load_Pi()
    print i_num
    if i_num in Pi:
        print 'yes!', 'position = ', Pi.find(i_num)
    else:
        print 'no....'
        
    # all commented lines start with # (such as this one)
    # the next three lines load the three name files into lists
    boy_list = generate_name_list('vhs_male_names.txt')
    girl_list = generate_name_list('vhs_female_names.txt')
    both_list = generate_name_list('vhs_names.txt')
    
    # We'll now print the first and last 10 names from each list:
    print '\n first ten boy names: ', boy_list[0:10]  # it also works if you do boy_list[:10]
    print '\n last ten boy names: ', boy_list[-10:]
    print '\n first ten girl names: ', girl_list[0:10]  # it also works if you do boy_list[:10]
    print '\n last ten girl names: ', girl_list[-10:]
    print '\n first ten general names: ', both_list[0:10]  # it also works if you do boy_list[:10]
    print '\n last ten general names: ', both_list[-10:]
    
    #the lists are not sorted, we'll sort the girl list and print the first five and the last five
    girl_list.sort()
    print '\n first and last five girl names', girl_list[:5], girl_list[-5:]

    # We'll now combine the three lists into one big list with a great trick
    all_names_list = boy_list + girl_list + both_list   # done!
    
    #let's check that the length of the new list is the sum of the other three
    print '\nlen new list = ', len(all_names_list)
    print 'len boy list = ', len(boy_list)
    print 'len girl list = ', len(girl_list)
    print 'len both list = ', len(both_list)
    print 'sum of three = ', len(boy_list) + len(girl_list) + len(both_list)
    
    # Since there are probably repeated names, we can get a unique list by using sets
    all_names_set = set(all_names_list)
    #now compare the lengths of both
    print '\n number of unique names = ', len(all_names_set)
    
    # We can find the number of repeated names using sets and intersections.
    # The number of repeated names between the boy and girl lists
    girl_set = set(girl_list)
    boy_set = set(boy_list)
    repeated_names = girl_set.intersection(boy_set)
    print '\n number of repeated names = ', len(repeated_names)
    
    #Pi stuff
    #We'll now convert each name to a number (a=1, b=2, etc), and see whether they appear in the 
    #decimals of Pi. We'll do it for the boy list, but it's the exact same thing for the other lists
    Pi_location_dict = {}   # start a dictionary, the location on Pi will be the keys, and the names the
                            # corresponding value
    for name in boy_list:  # this might take a while, it might be a good idea to start with girl_list[:100]
        number_name = names_to_numbers(name)
        location_in_Pi = Pi.find(number_name)
        Pi_location_dict[location_in_Pi] = name
        
    #now, sort the list of keys, remove the -1 value, and find the closest name
    keys = Pi_location_dict.keys()
    keys.sort()
    keys.remove(-1)     # from the names that didn't match anything in Pi
    print '\n closest position = ', keys[0]
    print 'corresponding name = ', Pi_location_dict[keys[0]]
    
    #now, we'll print the 20 closest names (with the corresponding position too)
    for key in keys[:20]:
        print Pi_location_dict[key], key
        
    # To group names by the first three letters they start with, we'll make a dictionary with the
    #3 letter prefixes as the keys, and a list of all names with that particular prefix as the value
    #of the dictionary
    prefix_dict = {}    # initialize dictionary
    for name in all_names_set:  # we can use any list or set here
        prefix_key = name[:3]
        if prefix_key not in prefix_dict:    # if it's the first time we see the prefix, we add a new list
            prefix_dict[prefix_key] = [name]
        else:
            prefix_dict[prefix_key].append(name)    #if the prefix is already there, append the name to the list
            
    #now, we print the first and last 5 prefixes in the dictionary, with the corresponding names
    prefix_keys = prefix_dict.keys()
    prefix_keys.sort()
    for i in range(5):
        print prefix_keys[i], prefix_dict[prefix_keys[i]]
    for i in range(5):
        print prefix_keys[-i-1], prefix_dict[prefix_keys[-i-1]]
        
    #We'll use two methods to find the prefix with the most names
    #method one: start a counter at zero, for each prefix, count the number of names, if it's bigger 
    #than the counter, change the counter to the new number, while keeping track of the prefix too
    len_counter = 0
    winning_prefix = 'zzz'
    for prefix in prefix_dict:
        if len(prefix_dict[prefix]) > len_counter:
            len_counter = len(prefix_dict[prefix])
            winning_prefix = prefix
    print '\n prefix with most names: ', winning_prefix, ', number of names: ', len_counter
    print prefix_dict[winning_prefix]
    
    #method 2: make a dictionary with the length of each list of names as the key, and the prefix as its value
    len_dict = {}
    for prefix in prefix_dict:
        len_dict[len(prefix_dict[prefix])] = prefix
    #now sort the keys and find the largest one (or largest set, this method allows us to find the top 10)
    prefix_lengths = len_dict.keys()
    prefix_lengths.sort()
    print '\n prefixes with the most names: '
    for prefix_len in prefix_lengths[-10:]:
        print len_dict[prefix_len], prefix_len
        
    