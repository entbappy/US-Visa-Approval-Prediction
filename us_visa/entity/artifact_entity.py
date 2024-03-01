from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path:str 
    test_file_path:str 



@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str
 