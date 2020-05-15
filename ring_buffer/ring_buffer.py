class RingBuffer:
    def __init__(self, capacity):
        """
        Creates a Ring Buffer. 
        Passed value "capacity" = static length of desired Ring Buffer.
        """
        self.capacity = capacity
        self.opIndex = 0            # "oldest value" index
        self.buffer = [None] * capacity     # creates the ring buffer structure in mem, 
                                            # for given length; equivalent to using np.zeroes
    def append(self, item):
        """
        Apply passed item to Buffer, overwriting oldest value, tracked by opIndex.
        Increment opIndex counter after application, using mod operand to reset
        counter to 0 upon reaching max capacity of Buffer
        """
        # print statement testing above methodology:
#        print( "index {} :: result of mod calculation {}".format( 
#            self.opIndex, ((self.opIndex + 1) % self.capacity)))

        self.buffer[ self.opIndex] = item
        self.opIndex = (self.opIndex + 1) % self.capacity


    def get(self):
        """
        Iterate over all existing values in Buffer; append each to secondary
        list, controlling for None values; return that list

        *** NOTICE: 'None' values will not be reported with this! ***
        
        If you would like to see 'None' values, access self.buffer directly.
        """
        bufferVals = []

        for entry in self.buffer:
            if entry is not None:
                bufferVals.append( entry)
        return bufferVals


################
#   Testing:   #
################

test = RingBuffer( 5)

test.append( 1)
test.append( 2)
test.append( 4)
test.append( 8)
test.append( 16)
test.append( 24)
test.append( 32)

print( test.get())
#print( test.capacity, test.buffer)