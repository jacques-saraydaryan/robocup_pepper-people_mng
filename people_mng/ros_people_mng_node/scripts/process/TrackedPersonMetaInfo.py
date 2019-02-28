import time
from PersonMetaInfo import PersonMetaInfo


class TrackedPersonMetaInfo(PersonMetaInfo):
    ROLE_NONE = "NONE"
    ROLE_OPERATOR = "OPERATOR"
    ROLE_PERSON_OF_INTEREST = "PERSON_OF_INTEREST"
    role = 0
    last_update_time = 0
    current_x = 0
    current_y = 0
    current_z = 0
    weight = 0

    def __init__(self, id, label_id, score, body_bounding_box, shirt_bounding_box, trouser_bounding_box,
                 shirt_color_list, trouser_color_list):
        PersonMetaInfo.__init__(self, id)

        self.label_id = label_id
        self.score = score
        self.setBoundingBox(PersonMetaInfo.PERSON_RECT, body_bounding_box)
        self.setBoundingBox(PersonMetaInfo.SHIRT_RECT, shirt_bounding_box)
        self.setBoundingBox(PersonMetaInfo.TROUSER_RECT, trouser_bounding_box)
        self.setColorList(PersonMetaInfo.SHIRT_RECT, shirt_color_list)
        self.setColorList(PersonMetaInfo.TROUSER_RECT, trouser_color_list)
        self.role = self.ROLE_NONE
        self.incWeight()

    def getPose(self):
        return self.current_x, self.current_y, self.current_z

    def setPose(self, x, y, z):
        self.current_x = x
        self.current_y = y
        self.current_z = z
        self.last_update_time = time.time()

    def incWeight(self):
        self.weight = self.weight + 1