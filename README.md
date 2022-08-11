# experiments-bsc-thesis-2022

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
