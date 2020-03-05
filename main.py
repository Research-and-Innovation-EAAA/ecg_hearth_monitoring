import Physionet.DataProcessor as pdp

if __name__ == "__main__":
    print("Main program start!")

    
    pipeline = pdp.setup_pipeline(256)

    pre_processers = []

    to_process = {
        "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\ltafdb.tar",
        "ext_loc": ".\\resources\\physionet\\ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2']
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\nsrdb.tar",
        "ext_loc": ".\\resources\\physionet\\nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "D:\\Praktik Vinter-Forår 2020\\resources\\physionet\\fantasia.tar",
        "ext_loc":".\\resources\\physionet\\fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
    }
    pre_processers.append(pipeline.execute(to_process))

    for pre_proces_elem in pre_processers:
        pre_proces_elem.join()
    