import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def pre_processing(data_frame):
    """
        getting the dataframe and pre processing it
        @param data_frame
        @return dataframe
    """
    read_file = pd.read_csv(data_frame)
    data_frame = pd.DataFrame(read_file)

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
    getting the dataframe and extracting the text of content column
    :param data_frame
    :return dataframe
    """
    data_frame['Content'] = data_frame['Content'].apply(remove_html_tags)
    value = data_frame['Content']
    content_column = ' '.join(value.astype(str))
    return content_column


def filtered_data(data_frame):
    """
    getting the dataframe and cleaning it
    :param data_frame
    :return dataframe
    """
    cleaned_text = re.sub('[^a-zA-Z]', ' ', data_frame)
    cleaned_text = cleaned_text.lower()
    return cleaned_text


def remove_html_tags(text):
    """
    getting the dataframe and removing html tags from it
    :param dataframe
    :return dataframe
    """
    soup = BeautifulSoup(text, 'html.parser')
    cleaned_text = soup.get_text()
    return cleaned_text
