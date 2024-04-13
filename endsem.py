class Product:
  def __init__(self, name, category):
    self.name = name
    self.category = category

  def __str__(self):
    return self.name

class HairCareProduct(Product):
  def __init__(self, name):
    Product.__init__(self, name, "Hair Care")  

class SkinCareProduct(Product):
  def __init__(self, name):
    Product.__init__(self, name, "Skin Care")

class HealthCareProduct(Product):
  def __init__(self, name):
    Product.__init__(self, name, "Health Care")

product_recommendations = {
  "hair": {
    "dry_hair": [HairCareProduct("Moisturizing shampoo"), HairCareProduct("Deep conditioner")],
    "oily_hair": [HairCareProduct("Clarifying shampoo"), HairCareProduct("Scalp scrub")],
    "dandruff": [HairCareProduct("Anti-dandruff shampoo")],
    "hair_loss": [HairCareProduct("Hair loss prevention shampoo"), HairCareProduct("Scalp serum")]
  },
  "skin": {
    "dry_skin": [SkinCareProduct("Hydrating cleanser"), SkinCareProduct("Rich moisturizer")],
    "oily_skin": [SkinCareProduct("Oil-free cleanser"), SkinCareProduct("Mattifying moisturizer")],
    "acne": [SkinCareProduct("Salicylic acid cleanser"), SkinCareProduct("Acne spot treatment")],
    "wrinkles": [SkinCareProduct("Retinol serum"), SkinCareProduct("Moisturizer with SPF")]
  },
  "health": {
    "cold": [HealthCareProduct("Decongestant"), HealthCareProduct("Pain reliever")],
    "allergies": [HealthCareProduct("Antihistamine"), HealthCareProduct("Nasal spray")],
    "digestive_issues": [HealthCareProduct("Probiotics"), HealthCareProduct("Dietary fiber supplement")],
    "sleep_problems": [HealthCareProduct("Melatonin"), HealthCareProduct("Relaxation tea")]
  }
}

def get_user_needs():
  print("Welcome to the Health & Beauty Recommendation System!")
  needs = []
  category = input("Select a category (hair, skin, health): ").lower()

  if category in product_recommendations:
    print("\n", category.capitalize(), "Concerns:")
    for need in product_recommendations[category].keys():
      print(f"- {need}")
    needs_input = input("Enter your concerns (separated by commas): ").lower()
    needs = needs_input.split(",")
  else:
    print("Invalid category. Please try again.")

  return category, needs

def recommend_products(category, needs):
  recommended_products = []
  if category in product_recommendations:
    for need in needs:
      recommended_products.extend(product_recommendations[category].get(need, []))
  return recommended_products

def display_recommendations():
  category, needs = get_user_needs()
  recommended_products = recommend_products(category, needs)
  if recommended_products:
    print("\nRecommended Products:")
    for product in recommended_products:
      print(f"- {product.category}: {product}")
  else:
    print("No recommendations found for your needs. Please consult a healthcare professional for specific advice.")

display_recommendations()  
