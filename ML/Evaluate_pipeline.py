import ML.tasks.LoadModelTask as lmt
import ML.tasks.AppleDataEvaluateTask as adet

import services.pipelines.Pipeline as pipeline

def setup():
    tasks = [
        lmt.LoadModelTask(),
        adet.AppleDataEvaluateTask()
    ]

    return pipeline.Pipeline(tasks)