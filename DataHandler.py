import pandas as pd
import numpy as np
from numpy import ndarray

class DataHandler:
    def __init__(self, name: str, rows:int = 0) -> None:
        '''
        name:str - имя файла, например test.csv
        rows:int - количество строк, читаемых из файла
        Если rows не указывается, читается весь файл
        '''
        self.name = name
        self.data_array = None

        try:
            if rows != 0:
                data_frame = pd.read_csv(self.name, nrows=rows)
            else:
                data_frame = pd.read_csv(self.name)

            self.data_array = data_frame.values
        except Exception as e:
            raise Exception(f"Ошибка загрузки данных: {e}")


    def get_data_array(self) -> ndarray:
        '''
        get_data_array() возвращает данные из CSV файла в виде np.array (ndarray)
        '''
        if self.data_array is None:
            raise Exception("Данные не загружены")

        return self.data_array
    
    def get_optimal_coordinates(self) -> ndarray:
        '''
        get_optimal_coordinates() - получить оптимальные координаты
        По другому, функция, решающая поставленную задачу
        Возвращает данные в виде np.array (ndarray) [uuid, lotitude, longitude]
        '''
        if self.data_array is None:
            raise Exception("Данные не загружены")

        latitudes = self.data_array[:, 1].astype(float)
        longitudes = self.data_array[:, 2].astype(float)
        shipments = self.data_array[:, 3].astype(float)

        distances = np.sqrt((latitudes[:, np.newaxis] - latitudes) ** 2 + (longitudes[:, np.newaxis] - longitudes) ** 2)

        resulted_distances = 2 * distances * shipments

        sums = np.sum(resulted_distances, axis=1)

        optimal_index = np.argmin(sums)

        optimal_coordinates = self.data_array[optimal_index, :3]

        return optimal_coordinates