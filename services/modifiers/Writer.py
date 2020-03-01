def save(datasets=None, path=None):
    with open(path, 'w') as file:
        for x in range(0, len(datasets)):
            file.write(f'x_{x}')
                
            if x < len(datasets):
                file.write(',')
        
        file.write('\n')
        file.write(datasets)
        
        """
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
        """