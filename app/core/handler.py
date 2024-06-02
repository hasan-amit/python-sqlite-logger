class Handler:
    def __init__(self, app) -> None:
        self.app = app
        pass

    def add_entities(self, entities):
        self.app.custom_logger.info("Start Inserting data...")
        self.app.repository.insert(entities)
        self.app.custom_logger.info("Finished Inserting data.")
    
    def display_data(self):
        self.app.custom_logger.info("Getting data list...")
        data_list = self.app.repository.select_all()
        for data in data_list:
            self.app.custom_logger.data(data)
        self.app.custom_logger.info("finish displaying.")

    def run(self, entities):
        self.add_entities(entities)
        self.display_data()
