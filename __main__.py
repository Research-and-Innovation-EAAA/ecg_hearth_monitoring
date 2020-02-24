"""
import os

import services.modifiers.Extractor as extractor
import Physionet.ApplyHeadders as applyer
import Physionet.SplitData as splitter


fantasia_path = 'G:\\Praktik Vinter-Forår 2020\\resources\\fantasia.tar'
fantasia_ext_loc = 'G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia'

ltafdb_path = 'G:\\Praktik Vinter-Forår 2020\\resources\\ltafdb.tar'
ltafdb_ext_loc = 'G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf'

nsrdb_path = 'G:\\Praktik Vinter-Forår 2020\\resources\\nsrdb.tar'
nrsdb_ext_loc = 'G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr'

#extractor.extract(fantasia_path, fantasia_ext_loc, True)
#a1 = applyer.Apply_headders(fantasia_ext_loc, 'sample #', 'RESP', 'ECG', daemon=False)
# a1.start()

#extractor.extract(ltafdb_path, ltafdb_ext_loc, True)
#a2 = applyer.Apply_headders(ltafdb_ext_loc, 'sample #', 'ECG 1', 'ECG 2', daemon=False)
#a2.start()

#extractor.extract(nsrdb_path, nrsdb_ext_loc, True)
#a3 = applyer.Apply_headders(nrsdb_ext_loc, 'sample #', 'ECG 1', 'ECG 2', daemon=False)
#a3.start()

target_readings = 7500

#a1.join()
#s1 = splitter.Split_data(fantasia_ext_loc, target_readings)
#s1.start()

#a2.join()
s2 = splitter.Split_data(ltafdb_ext_loc, target_readings)
s2.start()

#a3.join()
#s3 = splitter.Split_data(nrsdb_ext_loc, target_readings)
#s3.start()

#Split workd done
#s1.join()
s2.join()
#s3.join()
"""

import Physionet.MachineLearningModel as mlm

model = mlm.setup_model()

model.compile(optimization='adam', loss='mse', metrics=['accuracy'])