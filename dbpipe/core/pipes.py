from dataclasses import dataclass, field, asdict
from typing import List, Optional, Literal, Type
import json
import os
from datetime import datetime, timedelta


@dataclass
class Schedule:
    frequency: str
    start_time: str
    end_time: Optional[str] = None
    time_zone: str = 'UTC'

    def __repr__(self):
        return str(asdict(self))

    def to_json(self):
        return json.dumps(asdict(self))



    # def __post_init__(self):
    #     valid_frequencies = {"hourly", "daily", "monthly"}
    #     if self.frequency is not None and self.frequency not in valid_frequencies:
    #         raise ValueError("Frequency must be one of 'hourly', 'daily', 'monthly'")



class ScheduleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Schedule):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)




@dataclass
class Pipe:
    """
    A data structure to document and track data pipelines

    Attributes:
    ----------
    name: str
        Name of the pipeline

    sources: List[str]
        The physical Location of the data. For APIs, this can be the endpoint. For databases, this can be the tables you are pulling from.

    destination: Optional[str]
        The endpoint or table where the data will be loaded.

    schedule: Optional[Schedule]
        Add an optional Schedule Object
    
    logfile: Optional[str]
        The location of the log. Used to troubleshoot the pipeline

    processfile: str
        The location of the pipeline process file

    
    """
    name: str
    sources: List[str]
    destination: str
    schedule: Optional[Type[Schedule]] = None
    logfile: Optional[str] = None
    processfile: Optional[str] = None

    def __str__(self):
        pipe_dict = {
            "name": self.name,
            "sources": self.sources,
            "destination": self.destination,
            "schedule": self.schedule,
            "logfile": self.logfile,
            "processfile": self.processfile,
        }
        return json.dumps(pipe_dict, indent=4, cls=ScheduleEncoder)

        
    def save(self, file_name: str):
        pipe_dict = {
            "name": self.name,
            "sources": self.sources,
            "schedule":self.schedule,
            "destination": self.destination,
            "logfile": self.logfile,
            "processfile": self.processfile,
            
        }

        # Create the "pipes" directory if it doesn't exist
        if not os.path.exists("pipes"):
            os.makedirs("pipes")

        # Construct the file path within the "pipes" directory
        file_path = os.path.join("pipes", file_name)

        # Write the JSON data to the file
        with open(file_path, 'w') as file:
            json.dump(pipe_dict, file, indent=4, cls=ScheduleEncoder)



    














@dataclass
class Pipelines:
    Pipes: List[Pipe]

    def __str__(self):
        pipeline_dict = {
            "Pipelines": [pipe.__dict__ for pipe in self.Pipes]
        }
        return json.dumps(pipeline_dict, indent=4)







