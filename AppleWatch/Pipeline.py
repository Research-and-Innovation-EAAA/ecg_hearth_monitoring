import services.pipelines.Pipeline as pipeline

import AppleWatch.tasks.ExtractorTask as et
import AppleWatch.tasks.DataPrepTask as dpt
import AppleWatch.tasks.ReadingsPruneTask as prt
import AppleWatch.tasks.PrepTrainingSourcesTask as ptst

import AppleWatch.tasks.PrepLabelsTask as plt

def setup():
    tasks = [
        et.ExtractorTask(),
        dpt.DataPrepTask(),
        prt.ReadingsPruneTask(),
        ptst.PrepTrainingSourcesTask(),
        
        #plt.PrepLabelsTask()
    ]

    return pipeline.Pipeline(tasks)