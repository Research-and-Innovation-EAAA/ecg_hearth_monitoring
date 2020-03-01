"""
import os

import Physionet.ExtractData as dex
import Physionet.ApplyHeadders as applyer
import Physionet.SplitData as splitter

fantasia_path = 'G:\\Praktik Vinter-Forår 2020\\resources\\fantasia.tar'
fantasia_ext_loc = 'G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia'

ltafdb_path = 'G:\\Praktik Vinter-Forår 2020\\resources\\ltafdb.tar'
ltafdb_ext_loc = 'G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf'

nsrdb_path = 'G:\\Praktik Vinter-Forår 2020\\resources\\nsrdb.tar'
nrsdb_ext_loc = 'G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr'

ex_fantasia = dex.Extract(fantasia_pathm fantasia_ext_loc, True)
ex_ltaf = dex.Extract(ltafdb_path, ltafdb_ext_loc, True)
ex_nsr = dex.Extract(nsrdb_path, nsrdb_ext_loc, True)

#Extract data done
ex_fantsia.join()
#a1 = applyer.Apply_headders(fantasia_ext_loc, 'sample #', 'RESP', 'ECG', daemon=False)
# a1.start()

ex_ltaf.join()
#a2 = applyer.Apply_headders(ltafdb_ext_loc, 'sample #', 'ECG 1', 'ECG 2', daemon=False)
#a2.start()

ex_nsr.join()
#a3 = applyer.Apply_headders(nrsdb_ext_loc, 'sample #', 'ECG 1', 'ECG 2', daemon=False)
#a3.start()

target_readings = 7500
#Apply headder done
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
fantasia_training_loc = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\fantasia_training.csv"
fantasia_training_ressources = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia"
training_1 = tp.TrainingData(fantasia_training_loc, fantasia_training_ressources, 7501)
training_1.start()

s2.join()
ltaf_training_loc = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\ltaf_training.csv"
ltaf_training_resources = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf"
training_2 = tp.TrainingData(ltaf_training_loc, ltaf_training_resources, 7501)
training_2.start()

#s3.join()
nsr_training_loc = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\nsr_training.csv"
nsr_training_resources = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr"
training_3 = tp.TrainingData(nsr_training_loc, nsr_training_resources, 7501)
training_3.start()

training_1.join()
training_2.join()
training_3.join()



import services.pipelines.Task as task

task_1 = task.Task()"""

import Physionet.PipelineTest