import services.pipelines.Pipeline as Pipeline
import Physionet.tasks.ExtractTask as et
import Physionet.tasks.HeaddersTask as ht
import Physionet.tasks.SplitTask as st
import Physionet.tasks.TrainingTask as tt
import Physionet.tasks.NormalizeFantasiaTask as nf
import Physionet.tasks.SplitTestTask as stt

readings = 7500

tasks = [
    et.ExtractTask(),
    nf.NormalizeFantasiaTask(),
    ht.HeaddersTask(),
    st.SplitTask(readings),
    tt.TrainingTask(),
    stt.SplitTestTask(0.8, 0.2)
]

pipeline = Pipeline.Pipeline(tasks)

to_process = {
    "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltafdb.tar",
    "ext_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf",
    "override_policy": True,
    "headders": ['sample #', 'ECG 1', 'ECG 2']
}

#pipeline.execute(to_process)

to_process = {
    "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsrdb.tar",
    "ext_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr",
    #"res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr",
    "headders": ['sample #', 'ECG 1', 'ECG 2'],
    "override_policy": True
}

#pipeline.execute(to_process)

to_process = {
    "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia.tar",
    "ext_loc":"D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia",
    #"res_loc":"D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia",
    "headders": ['sample #', 'RESP', 'ECG'],
    "override_policy": True,
}
pipeline.execute(to_process)