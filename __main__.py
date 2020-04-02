import ML.Pipeline as clad

if __name__ == '__main__':
    to_process = {
        "name":"Load ML data",
        "training_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training.csv",
        "training_labels_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\training_labels.csv",
        "test_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test.csv",
        "test_labels_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\training\\test_labels.csv",
        "model_loc": "G:\\Praktik Vinter-Forår 2020\\resources\\physionet\\model",
        "log": True,
        "inputs": 7500,
        "epochs": 5,
        "sass": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99],
        "optimizer": "adam",
        "loss":"mse",
        "verbose":0
    }

    pipeline = clad.setup()

    t = pipeline.execute(to_process)

    t.join()