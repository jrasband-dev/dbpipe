# dbpipe

A lightweight and easy way to manage data pipelines.

# Getting Started
```cmd
pip install dbpipe
```


# Creating a Pipe
```python
from dbpipe import Pipe

pipe = Pipe(
        name='DW',
        sources=["AdSpend","SocialStats"],
        destination="DW",
        processfile="Test.py"
    )

pipe
```

# Saving a Pipe
```python
pipe.save()
```

# Creating a Schedule

```python
from dbpipe import Schedule

schedule = Schedule(frequency="Daily", start_time="8:00AM")

schedule
```

# Creating a Job

```python
from dbpipe import Job

job = Job('My Job',schedule=schedule,jobs=[pipe])
job
```
# Saving a Job
```python
job.save()
```

# Reading a Pipe
```python
from dbpipe import read_pipe

pipe = read_pipe('pipes/DW.json')
pipe
```

# Reading a Job

```python
from dbpipe import read_job

job = read_job('jobs/My Job.json')
job
```



