import services.pipelines.Pipeline as Pipeline
import Physionet.tasks.ExtractTask as et
import Physionet.tasks.HeaddersTask as ht
import Physionet.tasks.SplitTask as st
import Physionet.tasks.TrainingTask as tt
import Physionet.tasks.NormalizeFantasiaTask as nf
import Physionet.tasks.SplitTestTask as stt

def setup_pipeline(readings):
    tasks = [
        et.ExtractTask(),
        nf.NormalizeFantasiaTask(),
        ht.HeaddersTask(),
        st.SplitTask(readings),
        tt.TrainingTask(),
        #stt.SplitTestTask(0.8, 0.2)
    ]

    return Pipeline.Pipeline(tasks)

if __name__ == "__main__":
    print("IS source file")