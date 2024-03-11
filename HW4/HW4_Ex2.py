from pathlib import Path

def get_cats_info(path):

    file_path = Path(path)
    if file_path.exists():
        with open(path, 'r') as file_data:
            all_cats = []
            splited_lines = file_data.readlines()
            
            for line in splited_lines:
                cat_info = line.split(',')
                cat_dict = {"id":cat_info[0] , "name":cat_info[1] , "age":cat_info[2].replace('\n', '')} 
                all_cats.append(cat_dict)
            
            print(all_cats)
            return(all_cats)
