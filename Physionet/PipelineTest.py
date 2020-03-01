import services.pipelines.Pipeline as Pipeline
import Physionet.tasks.ExtractTask as et
import Physionet.tasks.HeaddersTask as ht
import Physionet.tasks.SplitTask as st
import Physionet.tasks.TrainingTask as tt
import Physionet.tasks.NormalizeFantasiaTask as nf
import Physionet.tasks.SplitTestTask as stt

readings = 7500

tasks = [
    #et.ExtractTask(),
    #ht.HeaddersTask('sample #', 'RESP', 'ECG'),
    #st.SplitTask(readings),
    #tt.TrainingTask(),
    stt.SplitTestTask(0.8, 0.2)
]

normal_pipeline = Pipeline.Pipeline(tasks)

tasks = [
    et.ExtractTask(),
    nf.NormalizeFantasiaTask(),
    ht.HeaddersTask('sample #', 'ECG 1', 'ECG 2'),
    st.SplitTask(readings),
    tt.TrainingTask(),
    stt.SplitTestTask(0.8, 0.2)
]

fantasia_pipeline = Pipeline.Pipeline(tasks)

to_process = {
    "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltafdb.tar",
    "ext_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltaf",
    "override_policy": True,
}

#normal_pipeline.execute(to_process)

to_process["comp_res_loc"] = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsrdb.tar"
to_process["ext_loc"] = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr"
to_process["res_loc"] = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsr"

normal_pipeline.execute(to_process)

to_process["comp_res_loc"] = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia.tar"
to_process["ext_loc"] = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia"
to_process["res_loc"] = "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia"

#fantasia_pipeline.execute(to_process)