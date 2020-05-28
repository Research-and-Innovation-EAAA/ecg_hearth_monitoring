import services.pipelines.Pipeline as pipeline

import AppleWatch.tasks.ExtractorTask as et
import AppleWatch.tasks.DataPrepTask as dpt
import AppleWatch.tasks.ReadingsPruneTask as prt
import AppleWatch.tasks.PrepTrainingSourcesTask as ptst
import AppleWatch.tasks.DataNormalizerTask as dnt

def setup():
    tasks = [
        et.ExtractorTask(),
        dpt.DataPrepTask(),
        prt.ReadingsPruneTask(),
        dnt.DataNormalizerTask(),
        ptst.PrepTrainingSourcesTask(),
    ]

    return pipeline.Pipeline(tasks)