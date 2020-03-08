import Physionet.DataProcessor as pdp

if __name__ == "__main__":
    pipeline = pdp.setup_pipeline(7500, 0.8, 0.2)

    pre_processers = []

    to_process = {
        "comp_res_loc": "/data/physionet/ltafdb.tar",
        "ext_loc": "/data/physionet/ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "name":"LTAF",
        "target_label": 1,
        "sampled_frequency":128,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "/data/physionet/nsrdb.tar",
        "ext_loc": "/data/physionet/nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True,
        "name":"NSR",
        "target_label": 0,
        "sampled_frequency":128,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "/data/physionet/fantasia.tar",
        "ext_loc":"/data/physionet/fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
        "name":"Fantasia",
        "target_label": 0,
        "sampled_frequency":250,
        "target_frequency":256
    }
    pre_processers.append(pipeline.execute(to_process))

    for pre_proces_elem in pre_processers:
        pre_proces_elem.join()
    