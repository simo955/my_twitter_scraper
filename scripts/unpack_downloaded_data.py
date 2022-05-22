import os
import shutil

data_path='../data'
destination_name='destination'
destination_path= data_path+'/'+destination_name

def unpack_downloaded_data(dirs):
    for d in dirs:
        dir_path= data_path+'/'+d
        error_flag=0
        files = [f.split('.csv')[0] for f in os.listdir(dir_path) if '.csv' in f]
    
        print('In directory {} found files: {}'.format(dir_path, files))
        for f in files:
            original_path = dir_path+'/'+f+'.csv'
            new_path = destination_path+'/'+f+'_'+d+'.csv'
            try:
                #Move file to new path
                os.rename(original_path, new_path)
            except Exception as e:
                print('Unable to move file. Exception', e)
                error_flag=1
        
        if error_flag==0:
        #Delete repository
            try:
                print('Removing {} directory'.format(dir_path))
                shutil.rmtree(dir_path)
            except OSError as e:
                print("Error: %s : %s" % (d, e.strerror))

if __name__ == "__main__":
    dirs = [d for d in os.listdir(data_path) if '.' not in d and destination_name not in d]

    try: 
        os.mkdir(destination_path) 
        print('Created destination repo {}!'.format(destination_path))
    except OSError as error: 
        print(error)

    unpack_downloaded_data(dirs)
