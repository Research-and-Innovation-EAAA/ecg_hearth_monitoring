import services.pipelines.Pipeline as pipeline
import Physionet.tasks.ConcatTrainTask as ctt

def setup_pipeline():
    tasks = [
        ctt.ConcatTrainTask()
    ]

    return pipeline.Pipeline(tasks)