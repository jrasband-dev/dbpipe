from dataclasses import dataclass, field
from typing import List, Optional, Literal
import json
import os

@dataclass
class Pipe:
    """
    A data structure to document and track data pipelines

    Attributes:
    ----------
    sourceType: str
        Where the data is coming from

    sources: List[str]
        The Physical Location of the data. For APIs, this can be the endpoint. For databases, this can be the tables you are pulling from.

    destinationType: Optional[str]
        The endpoint or table where the data will be loaded.

    frequency: Optional[str]
        How often is the pipeline is running
    
    logfile: Optional[str]
        The location of the log. Used to troubleshoot the pipeline

    filepath: str
        The location of the pipeline process file

    schedule: List[str]
        A list of scheduled Days and Times that the pipeline runs
    
    """
    sourceType: str
    sources: List[str]
    destinationType: Optional[str] = None
    destination: Optional[str] = None 
    frequency: Optional[str] = None
    logfile: Optional[str] = None
    filepath: Optional[str] = None
    schedule: Optional[List[str]] = None

    def __str__(self):
        pipe_dict = {
            "sourceType": self.sourceType,
            "sources": self.sources,
            "destinationType": self.destinationType,
            "destination": self.destination,
            "frequency": self.frequency,
            "logfile": self.logfile,
            "filepath": self.filepath,
            "schedule":self.schedule,
        }
        return json.dumps(pipe_dict, indent=4)


    def __post_init__(self):
        valid_frequencies = {"hourly", "daily", "monthly"}
        if self.frequency is not None and self.frequency not in valid_frequencies:
            raise ValueError("Frequency must be one of 'hourly', 'daily', 'monthly'")
        
    def save(self, file_name: str):
        pipe_dict = {
            "sourceType": self.sourceType,
            "sources": self.sources,
            "destinationType": self.destinationType,
            "destination": self.destination,
            "frequency": self.frequency,
            "logfile": self.logfile,
            "filepath": self.filepath,
            "schedule":self.schedule,
        }

        # Create the "pipes" directory if it doesn't exist
        if not os.path.exists("pipes"):
            os.makedirs("pipes")

        # Construct the file path within the "pipes" directory
        file_path = os.path.join("pipes", file_name)

        # Write the JSON data to the file
        with open(file_path, 'w') as file:
            json.dump(pipe_dict, file, indent=4)

@dataclass
class Pipelines:
    Pipes: List[Pipe]

    def __str__(self):
        pipeline_dict = {
            "Pipelines": [pipe.__dict__ for pipe in self.Pipes]
        }
        return json.dumps(pipeline_dict, indent=4)







