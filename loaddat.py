##
## Copyright (c), EVolution v1.5.0, 2016-2019, Baudouin DENIS de SENNEVILLE (b.desenneville@gmail.com) 
## & Luc LAFITTE (luclafitte@gmail.com), Institut de Mathématiques de Bordeaux UMR5251, 
## Université de Bordeaux, 351, cours de la Libération - F33405 Talence
##
## The author underlines that this code has been developped for academic purpose only. 
## The authors disclaim any responsability for any potential damage caused by this code.
##
## All rights reserved.
##
## Redistribution and use in source and binary forms, with or without modification, are not permitted.
##
import struct
import numpy as np

def loaddat(filename):

    f = open(filename, "rb")
    content = f.read()
    f.close()

    seed = 0

    # Extract the header size
    header_size = struct.unpack("i", content[seed:seed+4])
    header_size = int(header_size[0])
    seed = seed + 4

    # Extract the header data
    header = []
    for i in range(0, header_size): 
        tmp = struct.unpack("i", content[seed:seed+4])
        tmp = int(tmp[0])
        header.append(tmp)
        seed = seed + 4
    
    # Store image resolution parameters
    dimx = header[0]
    dimy = header[1]
    dimz = 1
    no_dyn = 1
    if header_size == 3:
      dimz   = 1
      no_dyn = header[2]
    if header_size == 4:
      dimz   = header[2]
      no_dyn = header[3]

    size = dimx * dimy * dimz * no_dyn
    shape = [dimx, dimy, dimz, no_dyn]

    # Extract data from file
    arr = np.zeros(size, dtype=np.float, order='F')
    for i in range(0, size): 
        tmp = struct.unpack("f", content[seed:seed+4])
        arr[i] = float(tmp[0])
        seed = seed + 4
    
    arr = np.reshape(arr, shape, order='F')
    return arr
