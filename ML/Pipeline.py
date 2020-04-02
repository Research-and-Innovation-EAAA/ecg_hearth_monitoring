import services.pipelines.Pipeline as pipe

import ML.tasks.FetchDataTask as fdt
import ML.tasks.TrainingTask as tt
import ML.tasks.ModelStatisticsTask as ms
import ML.tasks.SaveTask as st

def setup():
    tasks = [
        fdt.FetchDataTask(),
        tt.TrainingTask(),
        ms.ModelStatisticsTask(),
        st.ModelSaveTask()
    ]

    return pipe.Pipeline(tasks)