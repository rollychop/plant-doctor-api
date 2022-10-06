from dataclasses import dataclass


@dataclass()
class PlantModel():
    id: int
    name: str
    imageUrl: str
    diseaseName: str | None = None
    tagLine: str | None = None
    tags: set | None = None

    def set_disease(self, name: str):
        self.diseaseName = name
        return self


plants = [
    PlantModel(
        1,
        "Apple",
        "https://images.unsplash.com/photo-1640193272671-5f9c81ac92ac?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
    ),
    PlantModel(
        2, "Blueberry",
        "https://images.unsplash.com/photo-1566400628146-ae8f27849e90?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
    ),
    PlantModel(
        3, "Cherry",
        "https://images.unsplash.com/photo-1621763668206-b9a47fc8727a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80"
    ),
    PlantModel(
        4, "Corn",
        "https://images.unsplash.com/photo-1601593768799-7433c2447c29?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",

    ),
    PlantModel(5, "Grape",
               "https://images.unsplash.com/photo-1602330102257-04c00af50c1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=327&q=80"),
    PlantModel(6, "Orange",
               "https://images.unsplash.com/photo-1583063339941-694e94523a66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80",
               ),
    PlantModel(7, "Peach",
               "https://images.unsplash.com/photo-1595743825637-cdafc8ad4173?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80",
               ),
    PlantModel(8, "Pepper",
               "https://images.unsplash.com/photo-1606374067068-2d031aed64e1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80",
               ),
    PlantModel(9, "Potato",
               "https://images.unsplash.com/photo-1593708697557-f2feca483132?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80",
               ),
    PlantModel(10, "Raspberry",
               "https://images.unsplash.com/photo-1596591868231-05e852efc96f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=396&q=80",
               ),
    PlantModel(11, "Soybean",
               "https://images.unsplash.com/photo-1630097000524-cb08aff59426?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"),
    PlantModel(12, "Squash",
               "https://images.unsplash.com/photo-1570142056130-9f6b59c6287a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"),
    PlantModel(13, "Strawberry",
               "https://images.unsplash.com/photo-1588165171080-c89acfa5ee83?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80",
               ),
    PlantModel(14, "Tomato",
               "https://images.unsplash.com/photo-1471194402529-8e0f5a675de6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
               )
]
