from src.content_column.pre_processing.processing import pre_processing
from src.utils.constant import file_path


class Content_Column:
    def __init__(self):
        """
        getting data from preprocessing function and calculating the accuracy of k-means
         @param dataframe
        @type list
        """
        self.dataset = file_path
        self.pipeline()

    def pipeline(self):
        """
        getting the dataframe and calling all the steps of pre processing
        @return: array
        """
        processed_dataframe = pre_processing(self.dataset)
        print(processed_dataframe)