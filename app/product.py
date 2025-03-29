from dataclasses import dataclass


@dataclass
class Product:
    title: str = None
    description: str = None
    price: float = None
    rating: int = None
    num_of_reviews: int = None
    additional_info: dict = None
