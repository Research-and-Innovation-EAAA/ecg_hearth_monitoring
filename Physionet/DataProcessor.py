import services.pipelines.Pipeline as Pipeline

import Physionet.tasks.ExtractTask as et
import Physionet.tasks.NormalizeFantasiaTask as nft
import Physionet.tasks.PadReadingsTask as prt
import Physionet.tasks.HeaddersTask as ht
import Physionet.tasks.SplitTask as st
import Physionet.tasks.TrainingTask as tt
import Physionet.tasks.SplitTestTask as stt
import Physionet.tasks.LabelTask as lt

def setup_pipeline(readings, train_split, test_split):
    tasks = [
        et.ExtractTask(),
        nft.NormalizeFantasiaTask(),
        prt.PadReadingsTask(),
        ht.HeaddersTask(),
        st.SplitTask(readings),
        tt.TrainingTask(),
        stt.SplitTestTask(train_split,test_split),
        lt.LabelTask()
    ]

    return Pipeline.Pipeline(tasks)