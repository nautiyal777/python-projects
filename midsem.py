def recommend_products():
    print("Welcome to the Skin Care Product Recommender!")
    print("Please select your skin type:")
    print("1. Oily")
    print("2. Dry")
    print("3. Combination")
    print("4. Sensitive")
    skin_type = input("Enter the number corresponding to your skin type: ")

    print("\nDo you have any specific skin concerns?")
    specific_needs = input("Enter your specific needs (separated by commas if multiple): ").split(',')

    # Decision making
    recommended_products = []
    if skin_type == '1':  # Oily skin
        recommended_products.append("Oil-free cleanser")
        recommended_products.append("Salicylic acid-based toner")
        recommended_products.append("Oil-free moisturizer")
        if 'acne-prone' in specific_needs:
            recommended_products.append("Acne spot treatment")
    elif skin_type == '2':  # Dry skin
        recommended_products.append("Hydrating cleanser")
        recommended_products.append("Alcohol-free toner")
        recommended_products.append("Rich moisturizer")
        if 'anti-aging' in specific_needs:
            recommended_products.append("Hydrating serum with hyaluronic acid")
    elif skin_type == '3':  # Combination skin
        recommended_products.append("Gentle foaming cleanser")
        recommended_products.append("Balancing toner")
        recommended_products.append("Lightweight moisturizer")
    elif skin_type == '4':  # Sensitive skin
        recommended_products.append("Fragrance-free cleanser")
        recommended_products.append("Hypoallergenic toner")
        recommended_products.append("Gentle moisturizer")

    # Output
    print("\nRecommended products for your skin type and needs:")
    for product in recommended_products:
        print("- " + product)

recommend_products()