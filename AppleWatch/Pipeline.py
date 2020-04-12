import services.pipelines.Pipeline as pipeline

import AppleWatch.tasks.ExtractorTask as et
import AppleWatch.tasks.DataPrepTask as dpt

import AppleWatch.tasks.PrepLabelsTask as plt

def setup():
    tasks = [
        et.ExtractorTask(),
        dpt.DataPrepTask(),

        plt.PrepLabelsTask()
    ]

    return pipeline.Pipeline(tasks)