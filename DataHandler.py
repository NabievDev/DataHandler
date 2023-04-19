import csv
import numpy as np
from numpy import ndarray

class DataHandler:
    def __init__(self, name: str) -> None:
        '''
        name:str - имя файла, например test.csv
        '''
        self.name = name
        self.data_array = None

        try:
            with open(self.name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                data = []
                for row in reader:
                    data.append(row)
                self.data_array = np.array(data)
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден")
        except Exception as e:
            raise Exception(f"Ошибка при чтении файла: {str(e)}")

    def get_data_array(self) -> ndarray:
        '''
        get_data_array() возвращает данные из CSV файла в виде np.array (ndarray)
        '''
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
    
