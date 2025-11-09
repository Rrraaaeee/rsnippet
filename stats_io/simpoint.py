
def get_simpoint_weight_dict(BASE_DIR):
    weight_dict = {}
    for cluster_dir in BASE_DIR.glob("*"):
        bm = cluster_dir.name
        sp_file = cluster_dir / "simpoints0"
        wt_file = cluster_dir / "weights0"
        if (not sp_file.exists() or not wt_file.exists()):
            continue
    
        sp_file = open(sp_file,"r")
        wt_file = open(wt_file,"r")
    
        weight_dict[bm] = []
        for sp_line, wt_line in zip(sp_file,wt_file):
            xth, sp = sp_line.strip("\n").split()
            wt,  sp_ = wt_line.strip("\n").split()
            assert(sp == sp_) 
            weight_dict[bm].append((xth, wt))
    
        sp_file.close()
        wt_file.close()
    return weight_dict
