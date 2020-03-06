import Physionet.DataProcessor as pdp

if __name__ == "__main__":
    print("Main program start!")
    
    pipeline = pdp.setup_pipeline(7500, 0.8, 0.2)

    pre_processers = []

    to_process = {
        "comp_res_loc": ".\\resources\\physionet\\ltafdb.tar",
        "ext_loc": ".\\resources\\physionet\\ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "name":"LTAF"
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": ".\\resources\\physionet\\nsrdb.tar",
        "ext_loc": ".\\resources\\physionet\\nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True,
        "name":"NSR"
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": ".\\resources\\physionet\\fantasia.tar",
        "ext_loc":".\\resources\\physionet\\fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
        "name":"Fantasia",
        "readings":7500
    }
    pre_processers.append(pipeline.execute(to_process))

    for pre_proces_elem in pre_processers:
        pre_proces_elem.join()
    