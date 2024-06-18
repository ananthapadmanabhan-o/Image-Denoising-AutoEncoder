from dataclasses import dataclass
from pathlib import Path



@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir:Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    local_data_source_path:Path
    local_input_feature_file: str
    local_output_feature_file: str
    image_height: int
    image_width: int 
    image_channel: int
    


@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int


