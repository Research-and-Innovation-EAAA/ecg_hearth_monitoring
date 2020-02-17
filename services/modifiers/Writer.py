def save(datasets=None, path=None, set_length=-1):
    with open(path, 'w') as file:
        for x in range(0, set_length):
            file.write(f'x_{x}')
                
            if x < set_length:
                file.write(',')
        
        for res_elem in datasets:
            index = 0
            file.write('\n')
            
            for val_elem in res_elem.values:
                file.write(f"{val_elem[0]}")
                
                index += 1
                
                if index < len(res_elem.values):
                    file.write(',')
                else:
                    continue
            
            file.write('\n')