import logging
import unittest
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

from src.content_column.pre_processing.processing import extract_data, filtered_data
from src.utils.constant import file_path


class Testing_Column_Content:
    def __init__(self):
        """
        getting data from preprocessing function and pre processing it
         @param dataframe
        @type dataframe
        """
        self.dataset = file_path
    def test_pre_processing(data_frame):
        """
            getting the dataframe and pre processing it
            @param data_frame
            @return dataframe
        """
        read_file = pd.read_csv(file_path)
        data_frame = pd.DataFrame(read_file)
        if isinstance(data_frame, pd.DataFrame):
            logging.info("This is a Dataframe")
        else:
            logging.info("This is not Dataframe")

        extracting_data = extract_data(data_frame)
        filtering_data = filtered_data(extracting_data)


        tokens = word_tokenize(filtering_data)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]
        processed_array = np.array(filtered_tokens)
        processed_array = processed_array.astype(object)
        return processed_array


    def extract_data(data_frame):
        """
        getting the dataframe and extracting the data of content column
        :return: dataframe
        """
        data_frame['Content'] = data_frame['Content'].apply(remove_html_tags)
        value = data_frame['Content']
        content_column = ' '.join(value.astype(str))
        return content_column


    def filtered_data(data_frame):
        """
        getting the dataframe and filtering the content and lower casing it
        :return: dataframe
        """
        cleaned_text = re.sub('[^a-zA-Z]', ' ', data_frame)
        cleaned_text = cleaned_text.lower()
        return cleaned_text


    def remove_html_tags(text):
        """
        getting the dataframe and remove html tags in it
        :return: dataframe
        """
        soup = BeautifulSoup(text, 'html.parser')
        cleaned_text = soup.get_text()
        return cleaned_text


class Test_class(unittest.TestCase):
    def test_for_dataframe(self):
        with self.assertLogs() as captured:
            df_check = Testing_Column_Content()
            df_check.test_pre_processing()
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "This is a Dataframe")
