from typing import List
from LAS import Converter

c = Converter.Converter() # create converter object

log = c.set_file("Sample.las") #return LogWrapper

# get section
data      = log.data
version   = log.version
curve     = log.curve
parameter = log.parameter
well      = log.well
other     = log.other

#l1=list(curve.items())

#print(curve)

# or get dictionary
log_in_dict = log.get_dict()
#log_in_dict["parameter"] = ""

#print(log_in_dict)
# or print on json format and save to disk
log_in_json = log.get_json("outfile_name")