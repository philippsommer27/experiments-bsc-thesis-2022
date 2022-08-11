from eesr import interface
from pandas import Timestamp, DataFrame
import os
import warnings
warnings.filterwarnings("ignore")


dc_trace = "Input\opendc_out.csv"
key_path = "Input\entsoe_token.txt"
results_pre_path = "Results"


def run_experiment(name, start: Timestamp, country="NL", tz="Europe/Amsterdam", caching=True, green_ratio=None, subname=None, make_out=True):
    if subname is None:
        path = os.path.join(results_pre_path, name)
    else:
        path = os.path.join(results_pre_path, name, subname)
    exists = os.path.exists(path)
    if not exists:
        os.makedirs(path)
    
    def store_df(df: DataFrame):
        pickle_path = os.path.join(path, "df.pkl")
        df.to_pickle(pickle_path)

    results = os.path.join(path, "results.json")
    df = interface.opendc_grid_analysis(dc_trace, key_path, start, country, results, tz, caching, green_ratio)

    if make_out:
        store_df(df)

        report_path = os.path.join(path, "report.html")
        report = interface.generate_compact_profile(results, "sus_prof", report_path, True)
        interface.to_image(report)


start = Timestamp(year=2020, month=9, day=4, hour=15, tz="Europe/Amsterdam")
run_experiment("mem_profile", start, make_out=False)