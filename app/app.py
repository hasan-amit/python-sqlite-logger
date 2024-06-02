import json
from .core.handler import Handler
from .logger.logger import CustomLogger
from .repository.database import DataRepository



class App:
    def __init__(self, path) -> None:
        self.repository = DataRepository(f"{path}/sqlite.db")
        self.custom_logger = CustomLogger(path)
        pass

    def start(self):
        employee_data = {
            "name": "John Doe",
            "address": {
                "street": {
                    "number": 123,
                    "name": "Main street"
                },
                "city": "Anytown",
                "zip": "12345"
            }
        }
        entities = [
            (1, 'David', 'Anderson', 'IT', 'Dev', 3000, json.dumps(employee_data['address']), '2020-06-01'),
            (2, 'Tom', 'Roger', 'IT', 'Manager', 3000, json.dumps(employee_data['address']), '2018-03-02'),
            (3, 'Alan', 'Meyer', 'IT', 'Dev', 5000, json.dumps(employee_data['address']), '2019-04-15')
        ]
        Handler(self).run(entities)
