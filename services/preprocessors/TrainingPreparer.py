import os

def prep_data(datasets):
    train_set_path = f"{os.path.join('.', 'resources', 'ecg_data', 'apple_ecgs')}\\training.csv"

    with open(train_set_path, 'w') as train_file:
        max_readings = 15360

        index = 0

        for reading in range(0, max_readings):
            train_file.write(f"x_{reading}")

            index += 1

            if index < max_readings:
                train_file.write(',')

        for res_elem in datasets:
            index = 0
            train_file.write("\n")

            if len(res_elem.values) >= 15360:
                for res_val in res_elem.values:
                    train_file.write(f"{res_val[0]}")

                    index += 1

                    if index < max_readings:
                        train_file.write(',')
                    else:
                        break