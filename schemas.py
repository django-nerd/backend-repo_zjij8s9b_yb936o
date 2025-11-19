"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

# Example schemas (replace with your own):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Fruit schema for our app
class Fruit(BaseModel):
    """
    Fruits collection schema
    Collection name: "fruit"
    """
    name: str = Field(..., description="Fruit name", min_length=1, max_length=60)
    color: Optional[str] = Field(None, description="Primary color")
    sweetness: Optional[int] = Field(5, ge=1, le=10, description="Sweetness level 1-10")
    origin: Optional[str] = Field(None, description="Where it's commonly grown")
    price: Optional[float] = Field(None, ge=0, description="Approx. price per unit or lb")
    image_url: Optional[HttpUrl] = Field(None, description="Image URL")
    description: Optional[str] = Field(None, description="Short description")

# Note: The Flames database viewer will automatically:
# 1. Read these schemas from GET /schema endpoint
# 2. Use them for document validation when creating/editing
# 3. Handle all database operations (CRUD) directly
# 4. You don't need to create any database endpoints!
