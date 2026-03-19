from typing import ClassVar, Dict, List
from BaseClasses import Item, ItemClassification, Location, Region
from worlds.AutoWorld import World, WebWorld
from .Options import Options


# ===== BASE ID =====
viewfinder_base_id = 9000000


class ViewfinderWeb(WebWorld):
    tutorials = []


class ViewfinderWorld(World):
    game: ClassVar[str] = "Viewfinder"
    web: ClassVar[WebWorld] = ViewfinderWeb()

    options_dataclass = Options
    options: Options

    topology_present: ClassVar[bool] = False

    # ===== ITEMS =====
    item_name_to_id: ClassVar[Dict[str, int]] = {
        "Camera": viewfinder_base_id + 2,
        "Chapter 1 Level 1-1": viewfinder_base_id + 3,
        "Chapter 1 Level 1-2": viewfinder_base_id + 4,
        "Chapter 1 Level 1-3": viewfinder_base_id + 5,
        "Chapter 1 Level 2-1": viewfinder_base_id + 6,
        "Chapter 1 Level 2-2": viewfinder_base_id + 7,
        "Chapter 1 Level 2-3": viewfinder_base_id + 8,
        "Chapter 1 Level 2-4": viewfinder_base_id + 8,
        "Chapter 1 Level 3-1": viewfinder_base_id + 9,
        "Chapter 1 Level 3-2": viewfinder_base_id + 10,
        "Chapter 2 Level 1-1": viewfinder_base_id + 11,
        "Chapter 2 Level 1-3": viewfinder_base_id + 12,
        "Chapter 2 Level 2-1": viewfinder_base_id + 13,
        "Chapter 2 Level 2-2": viewfinder_base_id + 14,
        "Chapter 2 Level 2-3": viewfinder_base_id + 15,
        "Chapter 2 Level 3-1": viewfinder_base_id + 16,
        "Chapter 2 Level 3-2": viewfinder_base_id + 17,
        "Chapter 3 Level 1-1": viewfinder_base_id + 18,
        "Chapter 3 Level 2-1": viewfinder_base_id + 19,
        "Chapter 3 Level 2-2": viewfinder_base_id + 20,
        "Chapter 3 Level 2-3": viewfinder_base_id + 21,
        "Chapter 3 Level 2-4": viewfinder_base_id + 22,
        "Chapter 3 Level 2-5": viewfinder_base_id + 23,
        "Chapter 3 Level 3-1": viewfinder_base_id + 24,
        "Chapter 3 Level 3-2": viewfinder_base_id + 25,
        "Chapter 3 Level 3-3": viewfinder_base_id + 26,
        "Chapter 3 Level 4-1": viewfinder_base_id + 27,
        "Chapter 3 Level 4-2": viewfinder_base_id + 28,
        "Chapter 3 Level 4-3": viewfinder_base_id + 29,
        "Chapter 3 Level 4-4": viewfinder_base_id + 30,
        "Chapter 3 Level 5-1": viewfinder_base_id + 31,
        "Chapter 3 Level 5-2": viewfinder_base_id + 32,
        "Chapter 3 Level 5-3": viewfinder_base_id + 33,
        "Chapter 3 Level 5-4": viewfinder_base_id + 34,
        "Chapter 3 Level 5-5": viewfinder_base_id + 35,
        "Chapter 4 Level 1-1": viewfinder_base_id + 36,
        "Chapter 4 Level 1-2": viewfinder_base_id + 37,
        "Chapter 4 Level 1-3": viewfinder_base_id + 38,
        "Chapter 4 Level 2-1": viewfinder_base_id + 39,
        "Chapter 4 Level 2-2": viewfinder_base_id + 40,
        "Chapter 4 Level 2-3": viewfinder_base_id + 41,
        "Chapter 4 Level 2-4": viewfinder_base_id + 42,
        "Chapter 4 Level 3-1": viewfinder_base_id + 43,
        "Chapter 4 Level 3-2": viewfinder_base_id + 44,
        "Chapter 4 Level 3-3": viewfinder_base_id + 45,
        "Chapter 4 Level 3-4": viewfinder_base_id + 46,
        "Chapter 4 Level 3-5": viewfinder_base_id + 47,
        "Chapter 4 Level 3-6": viewfinder_base_id + 48,
        "Chapter 4 Level 4-1": viewfinder_base_id + 49,
        "Chapter 4 Level 4-2": viewfinder_base_id + 50,
        "Chapter 4 Level 4-3": viewfinder_base_id + 51,
        "Chapter 4 Level 4-4": viewfinder_base_id + 52,
        "Chapter 5 Level 1-1": viewfinder_base_id + 53,
        "Chapter 5 Level 1-2": viewfinder_base_id + 54,
        "Chapter 5 Level 1-3": viewfinder_base_id + 55,
        "Chapter 5 Level 1-4": viewfinder_base_id + 56,
        "Chapter 5 Level 1-5": viewfinder_base_id + 57,
        "Chapter 5 Level 2-1": viewfinder_base_id + 58,
        "Chapter 5 Level 2-2": viewfinder_base_id + 59,
        "Chapter 5 Level 2-3": viewfinder_base_id + 60,
        "Chapter 5 Level 2-4": viewfinder_base_id + 61,
        "Chapter 5 Level 3-1": viewfinder_base_id + 62,
        "Chapter 5 Level 3-2": viewfinder_base_id + 63,
        "Chapter 5 Level 4-1": viewfinder_base_id + 64,
        "Chapter 5 Level 4-2": viewfinder_base_id + 65,
        "Chapter 5 Level 4-3": viewfinder_base_id + 66,
        "Chapter 5 Level 4-4": viewfinder_base_id + 67,
        "Chapter 5 Level 4-5": viewfinder_base_id + 68,
        "Chapter 5 Level 4-6": viewfinder_base_id + 69,
        "Chapter 5 Level 4-7": viewfinder_base_id + 70,
        "Chapter 5 Level 4-8": viewfinder_base_id + 71,
        "Chapter 5 Level 4-9": viewfinder_base_id + 72,
        "Chapter 2 Unlock": viewfinder_base_id + 73,
        "Chapter 3 Unlock": viewfinder_base_id + 74,
        "Chapter 4 Unlock": viewfinder_base_id + 75,
        "Chapter 5 Unlock": viewfinder_base_id + 76,
    }

    # ===== LOCATIONS =====
    location_name_to_id: ClassVar[Dict[str, int]] = {
        "Chapter 1 Level 1-1": viewfinder_base_id + 103,
        "Chapter 1 Level 1-2": viewfinder_base_id + 104,
        "Chapter 1 Level 1-3": viewfinder_base_id + 105,
        "Chapter 1 Level 2-1": viewfinder_base_id + 106,
        "Chapter 1 Level 2-2": viewfinder_base_id + 107,
        "Chapter 1 Level 2-3": viewfinder_base_id + 108,
        "Chapter 1 Level 2-4": viewfinder_base_id + 108,
        "Chapter 1 Level 3-1": viewfinder_base_id + 109,
        "Chapter 1 Level 3-2": viewfinder_base_id + 110,
        "Chapter 2 Level 1-1": viewfinder_base_id + 111,
        "Chapter 2 Level 1-3": viewfinder_base_id + 112,
        "Chapter 2 Level 2-1": viewfinder_base_id + 113,
        "Chapter 2 Level 2-2": viewfinder_base_id + 114,
        "Chapter 2 Level 2-3": viewfinder_base_id + 115,
        "Chapter 2 Level 3-1": viewfinder_base_id + 116,
        "Chapter 2 Level 3-2": viewfinder_base_id + 117,
        "Chapter 3 Level 1-1": viewfinder_base_id + 118,
        "Chapter 3 Level 2-1": viewfinder_base_id + 119,
        "Chapter 3 Level 2-2": viewfinder_base_id + 120,
        "Chapter 3 Level 2-3": viewfinder_base_id + 121,
        "Chapter 3 Level 2-4": viewfinder_base_id + 122,
        "Chapter 3 Level 2-5": viewfinder_base_id + 123,
        "Chapter 3 Level 3-1": viewfinder_base_id + 124,
        "Chapter 3 Level 3-2": viewfinder_base_id + 125,
        "Chapter 3 Level 3-3": viewfinder_base_id + 126,
        "Chapter 3 Level 4-1": viewfinder_base_id + 127,
        "Chapter 3 Level 4-2": viewfinder_base_id + 128,
        "Chapter 3 Level 4-3": viewfinder_base_id + 129,
        "Chapter 3 Level 4-4": viewfinder_base_id + 130,
        "Chapter 3 Level 5-1": viewfinder_base_id + 131,
        "Chapter 3 Level 5-2": viewfinder_base_id + 132,
        "Chapter 3 Level 5-3": viewfinder_base_id + 133,
        "Chapter 3 Level 5-4": viewfinder_base_id + 134,
        "Chapter 3 Level 5-5": viewfinder_base_id + 135,
        "Chapter 4 Level 1-1": viewfinder_base_id + 136,
        "Chapter 4 Level 1-2": viewfinder_base_id + 137,
        "Chapter 4 Level 1-3": viewfinder_base_id + 138,
        "Chapter 4 Level 2-1": viewfinder_base_id + 139,
        "Chapter 4 Level 2-2": viewfinder_base_id + 140,
        "Chapter 4 Level 2-3": viewfinder_base_id + 141,
        "Chapter 4 Level 2-4": viewfinder_base_id + 142,
        "Chapter 4 Level 3-1": viewfinder_base_id + 143,
        "Chapter 4 Level 3-2": viewfinder_base_id + 144,
        "Chapter 4 Level 3-3": viewfinder_base_id + 145,
        "Chapter 4 Level 3-4": viewfinder_base_id + 146,
        "Chapter 4 Level 3-5": viewfinder_base_id + 147,
        "Chapter 4 Level 3-6": viewfinder_base_id + 148,
        "Chapter 4 Level 4-1": viewfinder_base_id + 149,
        "Chapter 4 Level 4-2": viewfinder_base_id + 150,
        "Chapter 4 Level 4-3": viewfinder_base_id + 151,
        "Chapter 4 Level 4-4": viewfinder_base_id + 152,
        "Chapter 5 Level 1-1": viewfinder_base_id + 153,
        "Chapter 5 Level 1-2": viewfinder_base_id + 154,
        "Chapter 5 Level 1-3": viewfinder_base_id + 155,
        "Chapter 5 Level 1-4": viewfinder_base_id + 156,
        "Chapter 5 Level 1-5": viewfinder_base_id + 157,
        "Chapter 5 Level 2-1": viewfinder_base_id + 158,
        "Chapter 5 Level 2-2": viewfinder_base_id + 159,
        "Chapter 5 Level 2-3": viewfinder_base_id + 160,
        "Chapter 5 Level 2-4": viewfinder_base_id + 161,
        "Chapter 5 Level 3-1": viewfinder_base_id + 162,
        "Chapter 5 Level 3-2": viewfinder_base_id + 163,
        "Chapter 5 Level 4-1": viewfinder_base_id + 164,
        "Chapter 5 Level 4-2": viewfinder_base_id + 165,
        "Chapter 5 Level 4-3": viewfinder_base_id + 166,
        "Chapter 5 Level 4-4": viewfinder_base_id + 167,
        "Chapter 5 Level 4-5": viewfinder_base_id + 168,
        "Chapter 5 Level 4-6": viewfinder_base_id + 169,
        "Chapter 5 Level 4-7": viewfinder_base_id + 170,
        "Chapter 5 Level 4-8": viewfinder_base_id + 171,
        "Chapter 5 Level 4-9": viewfinder_base_id + 172,
        "Chapter 2 Completed": viewfinder_base_id + 173,
        "Chapter 3 Completed": viewfinder_base_id + 174,
        "Chapter 4 Completed": viewfinder_base_id + 175,
        "Chapter 5 Completed": viewfinder_base_id + 176,
        "Chapter 1 Completed": viewfinder_base_id + 177,
    }

    # ===== ITEM CREATION =====
    def create_item(self, name: str) -> Item:
        return Item(
            name,
            ItemClassification.progression,
            self.item_name_to_id[name],
            self.player
        )

    # ===== LOCATION CREATION =====
    def create_location(self, name: str, region: Region) -> Location:
        return Location(
            self.player,
            name,
            self.location_name_to_id[name],
            region
        )

    # ===== REGIONS =====
    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        hub = Region("Hub", self.player, self.multiworld)

        self.multiworld.regions += [menu, hub]
        menu.connect(hub)

        for name in self.location_name_to_id:
            loc = self.create_location(name, hub)
            hub.locations.append(loc)

    # ===== ITEMS =====
    def create_items(self):
        itempool: List[Item] = []

        for name in self.item_name_to_id:
            itempool.append(self.create_item(name))

        self.multiworld.itempool += itempool

    # ===== RULES =====
    def set_rules(self):
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has("Chapter 5 ", self.player)

    # ===== SLOT DATA =====
    def fill_slot_data(self):
        return self.options.as_dict(
            "progressive_camera",
            "world",
            "goal",
            "filter",
        )