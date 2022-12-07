from dataclasses import dataclass


@dataclass()
class PlantModel():
    id: int
    name: str
    imageUrl: str
    status: str | None = None
    tagLine: str | None = None
    tags: set | None = None

    def set_disease(self, name: str):
        self.status = name
        return self


plants = [
    PlantModel(
        1,
        "Apple",
        "https://images.unsplash.com/photo-1640193272671-5f9c81ac92ac?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
        ,
        tagLine="An apple is an edible fruit produced by an apple tree (Malus domestica). Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today. Apples have been grown for thousands of years in Asia and Europe and were brought to North America by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek, and European Christian tradition."),
    PlantModel(
        2, "Blueberry",
        "https://images.unsplash.com/photo-1566400628146-ae8f27849e90?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        tagLine="Blueberries are a widely distributed and widespread group of perennial flowering plants with blue or purple berries. They are classified in the section Cyanococcus within the genus Vaccinium. Vaccinium also includes cranberries, bilberries, huckleberries and Madeira blueberries. Commercial blueberries—both wild (lowbush) and cultivated (highbush)—are all native to North America. The highbush varieties were introduced into Europe during the 1930s."
    ),
    PlantModel(
        3, "Cherry",
        "https://images.unsplash.com/photo-1621763668206-b9a47fc8727a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80"
        ,
        tagLine="A cherry is the fruit of many plants of the genus Prunus, and is a fleshy drupe (stone fruit). Red cherries with stems Prunus avium, sweet cherry (a true cherry species) Commercial cherries are obtained from cultivars of several species, such as the sweet Prunus avium and the sour Prunus cerasus. The name 'cherry' also refers to the cherry tree and its wood, and is sometimes applied to almonds and visually similar flowering trees in the genus Prunus, as in 'ornamental cherry" or "cherry blossom'. Wild cherry may refer to any of the cherry species growing outside cultivation, although Prunus avium is often referred to specifically by the name wild cherry in the British Isles."
    ),
    PlantModel(
        4, "Corn",
        "https://images.unsplash.com/photo-1601593768799-7433c2447c29?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
        tagLine="Sweet corn (Zea mays convar. saccharata var. rugosa), also called sugar corn and pole corn, is a variety of maize grown for human consumption with a high sugar content. Sweet corn is the result of a naturally occurring recessive mutation in the genes which control conversion of sugar to starch inside the endosperm of the corn kernel. Sweet corn is picked when still in the immature (milk stage) and prepared and eaten as a vegetable, rather than field corn, which is harvested when the kernels are dry and mature (dent stage). Since the process of maturation involves converting sugar to starch, sweet corn stores poorly and must be eaten fresh, canned, or frozen, before the kernels become tough and starchy."
    ),
    PlantModel(
        5, "Grape",
        "https://images.unsplash.com/photo-1602330102257-04c00af50c1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=327&q=80"
        ,
        tagLine="A grape is a fruit, botanically a berry, of the deciduous woody vines of the flowering plant genus Vitis. Grapes are a non-climacteric type of fruit, generally occurring in clusters. The cultivation of grapes began perhaps 8,000 years ago, and the fruit has been used as human food over history. Eaten fresh or in dried form (as raisins, currants and sultanas), grapes also hold cultural significance in many parts of the world, particularly for their role in winemaking. Other grape-derived products include various types of jam, juice, vinegar and oil."),
    PlantModel(6, "Orange",
               "https://images.unsplash.com/photo-1583063339941-694e94523a66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80",
               tagLine="An orange is a fruit of various citrus species in the family Rutaceae (see list of plants known as orange); it primarily refers to Citrus × sinensis, which is also called sweet orange, to distinguish it from the related Citrus × aurantium, referred to as bitter orange. The sweet orange reproduces asexually (apomixis through nucellar embryony); varieties of sweet orange arise through mutations."
               ),
    PlantModel(7, "Peach",
               "https://images.unsplash.com/photo-1595743825637-cdafc8ad4173?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80",
               tagLine="The peach (Prunus persica) is a deciduous tree first domesticated and cultivated in Zhejiang province of Eastern China. It bears edible juicy fruits with various characteristics, most called peaches and others (the glossy-skinned, non-fuzzy varieties), nectarines."
               ),
    PlantModel(8, "Pepper",
               "https://images.unsplash.com/photo-1606374067068-2d031aed64e1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1172&q=80",
               tagLine="The bell pepper (also known as paprika, sweet pepper, pepper, or capsicum /ˈkæpsɪkəm/) is the fruit of plants in the Grossum Group of the species Capsicum annuum. Cultivars of the plant produce fruits in different colors, including red, yellow, orange, green, white, chocolate, candy cane striped, and purple. Bell peppers are sometimes grouped with less pungent chili varieties as 'sweet peppers'. While they are fruits—botanically classified as berries—they are commonly used as a vegetable ingredient or side dish. Other varieties of the genus Capsicum are categorized as chili peppers when they are cultivated for their pungency, including some varieties of Capsicum annuum."
               ),
    PlantModel(9, "Potato",
               "https://images.unsplash.com/photo-1593708697557-f2feca483132?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80",
               tagLine="The potato is a starchy tuber of the plant Solanum tuberosum and is a root vegetable native to the Americas. The plant is a perennial in the nightshade family Solace."
               ),
    PlantModel(10, "Raspberry",
               "https://images.unsplash.com/photo-1596591868231-05e852efc96f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=396&q=80",
               tagLine="The raspberry is the edible fruit of a multitude of plant species in the genus Rubus of the rose family, most of which are in the subgenus Idaeobatus. The name also applies to these plants themselves. Raspberries are perennial with woody stems. World production of raspberries in 2020 was 895,771 tonnes, led by Russia with 20% of the total."
               ),
    PlantModel(11, "Soybean",
               "https://images.unsplash.com/photo-1630097000524-cb08aff59426?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
               ,
               tagLine="The soybean, soy bean, or soya bean (Glycine max) is a species of legume native to East Asia, widely grown for its edible bean, which has numerous uses."

               ),
    PlantModel(12, "Squash",
               "https://images.unsplash.com/photo-1570142056130-9f6b59c6287a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
               ,
               tagLine="Squashes are a kind of vegetables. They originally came from the New World. Gourds are in the same family as squashes. Pumpkins and Zucchini (courgette) are types of squashes. Although squash is a fruit according to its botanical classification, it is generally considered a vegetable in food preparation."
               ),
    PlantModel(13, "Strawberry",
               "https://images.unsplash.com/photo-1588165171080-c89acfa5ee83?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80"
               ,
               tagLine="The garden strawberry (or simply strawberry; Fragaria × ananassa) is a widely grown hybrid species of the genus Fragaria, collectively known as the strawberries, which are cultivated worldwide for their fruit. The fruit is widely appreciated for its characteristic aroma, bright red color, juicy texture, and sweetness. It is consumed in large quantities, either fresh or in such prepared foods as jam, juice, pies, ice cream, milkshakes, and chocolates. Artificial strawberry flavorings and aromas are also widely used in products such as candy, soap, lip gloss, perfume, and many others."
               ),
    PlantModel(14, "Tomato",
               "https://images.unsplash.com/photo-1471194402529-8e0f5a675de6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"
               ,
               tagLine="The tomato is the edible berry of the plant Solanum lycopersicum, commonly known as the tomato plant. The species originated in western South America, Mexico, and Central America."
               )
]
