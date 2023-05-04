try: 
    from google.colab import drive    
    drive.mount('/content/gdrive/', force_remount=True)   
    %mkdir ./gdrive/MyDrive/osom3d/    
    %mkdir ./gdrive/MyDrive/osom3d/grid-data/    
    %mkdir ./gdrive/MyDrive/osom3d/configurations/   
    %mkdir ./gdrive/MyDrive/osom3d/osom-data/    
    %mkdir ./gdrive/MyDrive/osom3d/results/
except ModuleNotFoundError:   
    import os.  
    parent_dir = "."       
    osom_dir = "osom3d"  
    grid_dir = "grid-data"  
    config_dir = "configurations"  
    data_dir = "osom-data"  
    results_dir = "results"  
    osom_path =  os.path.join(parent_dir, osom_dir)   
    grid_path = os.path.join(parent_dir, osom_dir, grid_dir)  
    config_path = os.path.join(parent_dir, osom_dir, config_dir)  
    data_path = os.path.join(parent_dir, osom_dir, data_dir)  
    results_path = os.path.join(parent_dir, osom_dir, results_dir)  
    os.mkdir(osom_path)  
    os.mkdir(grid_path)  
    os.mkdir(config_path)  
    os.mkdir(data_path)  
    os.mkdir(results_path)