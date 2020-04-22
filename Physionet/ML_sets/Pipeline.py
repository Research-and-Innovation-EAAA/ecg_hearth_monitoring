import services.pipelines.Pipeline as pipeline

import Physionet.ML_sets.tasks.TrainingTask as tt
import Physionet.ML_sets.tasks.TestTask as testT

def setup():
    tasks =[
        tt.TrainingTask(),
        testT.TestTask()
    ]

    return pipeline.Pipeline(tasks)