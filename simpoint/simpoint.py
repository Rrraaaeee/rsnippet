def get_bm_from_bmsp(bm_sp):
    return "_".join(bm_sp.split("_")[:-1])

def weighted(x, weight_dict, weight_on):
    sum_weight = 0.0
    sum_cycles = 0.0
    for idx, row in x.iterrows():
        bm     = row["bm"]
        xth    = row["bm_name"].split("_")[-1]
        cycles = row[weight_on]
        for xth_, weight in weight_dict[bm]:
            if (xth == xth_):
                sum_cycles += cycles * float(weight)
                sum_weight += float(weight)
    if sum_weight == 0:
        return None
    return sum_cycles / sum_weight

def get_simpoint_weighted_average(df, weight_dict, weight_on, rename):
    # strip bm from bm_sp
    df["bm"] = df["bm_name"].map(get_bm_from_bmsp)
    df_bm = df.groupby("bm")[df.columns]\
              .apply(lambda x: weighted(x,weight_dict, weight_on))\
              .rename(rename)
    return df_bm
