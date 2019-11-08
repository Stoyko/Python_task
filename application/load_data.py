import string
import csv
import os
import re


class LoadData:

    def __init__(self):
        self.data = self.__load_data()

    def get_data(self) -> dict:
        return self.data

    def __load_data(self) -> dict:
        if not os.path.isfile(os.path.join('new_records.csv')):
            self.__create_filtered_csv()

        with open(os.path.join('data', 'new_records.csv'), encoding='utf8') as records_csv:
            csv_reader = csv.reader(records_csv)

            data = {}
            first = True
            for row in csv_reader:
                if not first:
                    data[row[0]] = self.__modify_title(row[1])
                else:
                    first = False

        return data

    @staticmethod
    def __create_filtered_csv():
        with open(os.path.join('data', 'records.csv'), encoding='utf8') as records_csv:
            csv_reader = csv.reader(records_csv)

            first = True
            columns_indexes = {}
            needed_rows = []
            for row in csv_reader:
                if first:
                    first = False
                    columns_indexes["record_id"] = [i for i, v in enumerate(row) if v == 'Record ID'][0]
                    columns_indexes["title"] = [i for i, v in enumerate(row) if v == 'Title'][0]
                    columns_indexes["language"] = [i for i, v in enumerate(row) if v == 'Languages'][0]

                if row[columns_indexes['language']] == 'English':
                    needed_rows.append([row[columns_indexes['record_id']], row[columns_indexes['title']],
                                        row[columns_indexes['language']]])

            with open(os.path.join('data', 'new_records.csv'), mode='w', encoding='utf8', newline='') as write_csv:
                csv_writer = csv.writer(write_csv, delimiter=',')

                csv_writer.writerow(['Record ID', 'Title', "Languages"])
                for row in needed_rows:
                    csv_writer.writerow(row)

    def __convert_numbers(self, title):
        numbers = re.findall(r'\d+', title)
        for number in numbers:
            title = str(title).replace(number, 'number')

        return title

    def __remove_punctuation(self, title):
        translator = str.maketrans('', '', string.punctuation)
        return title.translate(translator)


    def __modify_title(self, title):
        title = self.__remove_punctuation(title)
        title = self.__convert_numbers(title)
        title = str(title).lower()

        return title

