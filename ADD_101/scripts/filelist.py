# Generate a list of filepaths based on database structure at https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.surface.html


import pandas as pd
ftp_dir = "ftp://ftp2.psl.noaa.gov/Datasets/ncep.reanalysis.dailyavgs/surface_gauss/"
variable = "air.2m.gauss."
file_type = ".nc"
time =pd.Series(list(range(1950,1970)))
time = time.apply(str)
filepaths= ftp_dir + variable + time + file_type
filepaths.to_csv("../data/filelist.txt", index=False)
