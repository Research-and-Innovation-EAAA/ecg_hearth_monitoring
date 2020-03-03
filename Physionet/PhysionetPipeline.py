import services.pipelines.Pipeline as Pipeline

import Physionet.tasks.ExtractTask as et
import Physionet.tasks.HeaddersTask as ht
import Physionet.tasks.SplitTask as st
import Physionet.tasks.TrainingTask as tt
import Physionet.tasks.NormalizeFantasiaTask as nf
import Physionet.tasks.SplitTestTask as stt
import Physionet.tasks.LabelTask as lt

readings = 7500

tasks = [
    et.ExtractTask(),
    nf.NormalizeFantasiaTask(),
    ht.HeaddersTask(),
    st.SplitTask(readings),
    tt.TrainingTask(),
    stt.SplitTestTask(0.8, 0.2)
    #lt.LabelTask()
]

pipeline = Pipeline.Pipeline(tasks)

to_process = {
    "name": "Long-term AF",
    "comp_res_loc": ".\\resources\\physionet\\ltafdb.tar",
    "ext_loc": ".\\resources\\physionet\\ltaf",
    "override_policy": True,
    "headders": ['sample #', 'ECG 1', 'ECG 2'],
    "target_label": 1
}

pipeline.execute(to_process)

to_process = {
    "name": "Normal Sinus rythm",
    "comp_res_loc": ".\\resources\\physionet\\nsrdb.tar",
    "ext_loc": ".\\resources\\physionet\\nsr",
    "headders": ['sample #', 'ECG 1', 'ECG 2'],
    "override_policy": True,
    "target_label": 0
}

pipeline.execute(to_process)

to_process = {
    "name": "Fantasia",
    "comp_res_loc": ".\\resources\\physionet\\fantasia.tar",
    "ext_loc":".\\resources\\physionet\\fantasia",
    "headders": ['sample #', 'RESP', 'ECG'],
    "override_policy": True,
    "target_label": 0
}
pipeline.execute(to_process)