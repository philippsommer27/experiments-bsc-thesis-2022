# experiments-bsc-thesis-2022
The experiments are all contained within a jupyter notebook. For running the caching related experiments in section one it is best to comment out all subsequent experiments and vice versa. 

For the bandwidth saving experiment, use wireshark or tcpdump to capture all packets on (at the time of 08/2022:) 62.209.222.10

Graphs and further analysis are contained within a seperate jupyter notebook.
## Performance Experiments
### Memory impact with `memory_profile`
Install the memory profiler through:
```
$ pip install memory_profiler
```

Run memory profiler on **profiled** (see [documentation](https://github.com/pythonprofilers/memory_profiler) on how to profile functions) EESR program:
```
$ mprof run eesr_memory_profile.py
```
Produce graph:
```
$ mprof plot -t 'Memory Footprint of EESR Grid Analysis'
```
