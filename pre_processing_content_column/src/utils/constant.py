import pathlib

path = pathlib.Path(__file__).resolve().parent.parent
dataset_path = path / "dataset"
file_path = dataset_path / "extracted_blog_content - extracted_blog_content.csv"
