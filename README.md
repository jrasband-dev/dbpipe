# dbpipe

dbpipe is a lightweight and simple way to manage data pipelines. 

```mermaid
graph LR
A(Endpoints)-->B(Pipes)
B-->C(Jobs)
D(Schedules)-->C
C-.->E(Clusters)

```

## Creating Endpoints


```python
from dbpipe import EndPoint


facebook = EndPoint('Facebook','API','https://facebook.com/Posts')
facebook
```




    {'name': 'Facebook', 'type': 'API', 'location': 'https://facebook.com/Posts'}




```python
facebook.save()
```


```python
posttable = EndPoint('DW.Facebook.Posts','Database','ServerName')
posttable
```




    {'name': 'DW.Facebook.Posts', 'type': 'Database', 'location': 'ServerName'}




```python
posttable.save()
```

## Creating a Pipe


```python
from dbpipe import Pipe


pipe = Pipe(
        name='DW',
        sources=[facebook],
        destination=posttable,
        processfile="Test.py"
    )

pipe
```




    {'name': 'DW', 'sources': [{'name': 'Facebook', 'type': 'API', 'location': 'https://facebook.com/Posts'}], 'destination': {'name': 'DW.Facebook.Posts', 'type': 'Database', 'location': 'ServerName'}, 'logfile': None, 'processfile': 'Test.py'}




```python
pipe.to_dict()
```




    {'name': 'DW',
     'sources': [{'name': 'Facebook',
       'type': 'API',
       'location': 'https://facebook.com/Posts'}],
     'destination': {'name': 'DW.Facebook.Posts',
      'type': 'Database',
      'location': 'ServerName'},
     'logfile': None,
     'processfile': 'Test.py'}




```python
pipe.save()
```

## Creating a Schedule


```python
from dbpipe import Schedule

schedule = Schedule(frequency="Daily", start_time="8:00AM")

schedule

```




    {'frequency': 'Daily', 'start_time': '8:00AM', 'end_time': None, 'time_zone': 'UTC'}




```python
schedule.to_dict()
```




    {'frequency': 'Daily',
     'start_time': '8:00AM',
     'end_time': None,
     'time_zone': 'UTC'}



## Creating a Pipe Cluster


```python
from dbpipe.core.pipes import Cluster


clstr = Cluster([pipe,pipe])
clstr
```




    [{'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}, {'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}]



## Creating a Job


```python
from dbpipe import Job


job = Job('My Job',schedule=schedule,jobs=clstr)
job
```




    {'name': 'My Job', 'schedule': {'frequency': 'Daily', 'start_time': '8:00AM', 'end_time': None, 'time_zone': 'UTC'}, 'jobs': [{'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}, {'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}]}




```python
job.save()
```

## Reading a Pipe


```python
from dbpipe import read_pipe


pipe = read_pipe('pipes/DW.json')
pipe
```




    {'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}




```python
pipe.to_dict()
```




    {'name': 'DW',
     'sources': ['AdSpend', 'SocialStats'],
     'destination': 'DW',
     'logfile': None,
     'processfile': 'Test.py'}



## Reading a Job


```python
from dbpipe import read_job

job = read_job('jobs/My Job.json')
job
```




    {'name': 'My Job', 'schedule': {'frequency': 'Daily', 'start_time': '8:00AM', 'end_time': None, 'time_zone': 'UTC'}, 'jobs': [{'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}, {'name': 'DW', 'sources': ['AdSpend', 'SocialStats'], 'destination': 'DW', 'logfile': None, 'processfile': 'Test.py'}]}




```python
job.to_dict()
```




    {'name': 'My Job',
     'schedule': {'frequency': 'Daily',
      'start_time': '8:00AM',
      'end_time': None,
      'time_zone': 'UTC'},
     'jobs': [{'name': 'DW',
       'sources': ['AdSpend', 'SocialStats'],
       'destination': 'DW',
       'logfile': None,
       'processfile': 'Test.py'},
      {'name': 'DW',
       'sources': ['AdSpend', 'SocialStats'],
       'destination': 'DW',
       'logfile': None,
       'processfile': 'Test.py'}]}



## Lineage


```python
from dbpipe.lineage.mermaid import generate_mermaid_markdown_file


generate_mermaid_markdown_file('pipes','test.md')
```

