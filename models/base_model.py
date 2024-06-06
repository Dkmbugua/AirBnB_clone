
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
   
        self.created_at = datetime.now()
   
        self.updated_at = datetime.now()

    def __str__(self):
        """provides a readable string representation of the instance"""
        return f'{self.__class__.__name__}({self.id}, {self.__dict__})'


    def save(self):
        """it updates the update_at attribute with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """it returns a dictionary whcich conatin all key values"""
        dk_dict = self.__dict__.copy()
        dk_dict['updated_at'] = self.updated_at.isoformat()
        dk_dict['__class__'] = self.__class__.__name__
        dk_dict['created_at'] =self.create_at.isoformat()

        return dk_dict


