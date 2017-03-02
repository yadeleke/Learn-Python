def print_song():
    for i in range(99, 0, -1):

        if i == 1:
            print str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer."
            print "Take one down and pass it around, no more bottles of beer on the wall."

        elif i == 2:
            print str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer."
            print "Take one down and pass it around, " + str(i - 1) + " bottle of beer on the wall."

        else:
            print str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer."
            print "Take one down and pass it around, " + str(i - 1) + " bottles of beer on the wall."

        print ""

    i = 99

    print "No more bottles of beer on the wall, no more bottles of beer."
    print "Go to the store and buy some more, " + str(i) + " bottles of beer on the wall."

print_song()
