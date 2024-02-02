from dataclasses import dataclass, field
from typing import List, Optional, Literal
import json
import os

@dataclass
class Pipe:
    sourceType:str
    sources: List[str]
    destinationType: Optional[str]
    destination: Optional[str]
    frequency: Optional[str]
    logfile: Optional[str]
    filepath: str 

    def __str__(self):
        pipe_dict = {
            "sourceType": self.sourceType,
            "sources": self.sources,
            "destinationType": self.destinationType,
            "destination": self.destination,
            "frequency": self.frequency,
            "logfile": self.logfile,
            "filepath": self.filepath
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
            "filepath": self.filepath
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







