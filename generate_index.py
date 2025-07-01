
# import required libraries

import json
import random
import pandas as pd
from datetime import datetime
from random import randint, uniform, random


# define products json
### products.json

products_json = [
    {
        "product_id": "P001",
        "name": "Nivia Graffiti Basketball",
        "category": "Sports Equipment",
        "price": 518,
        "mrp": 849,
        "discount": "39%",
        "rating": 4.1,
        "image_url": "static/images/product_1.png"
    },
    {
        "product_id": "P002",
        "name": "Cosco Volleyball",
        "category": "Sports Equipment",
        "price": 615,
        "mrp": 799,
        "discount": "23%",
        "rating": 4.7,
        "image_url": "static/images/product_2.png"
    },
    {
        "product_id": "P003",
        "name": "SG Cricket Bat (KLR Edition)",
        "category": "Sports Equipment",
        "price": 1334,
        "mrp": 1499,
        "discount": "11%",
        "rating": 4.5,
        "image_url": "static/images/product_3.png"
    },
    {
        "product_id": "P004",
        "name": "Spartan Tennis Ball",
        "category": "Sports Equipment",
        "price": 242,
        "mrp": 299,
        "discount": "19%",
        "rating": 4.9,
        "image_url": "static/images/product_4.png"
    },
    {
        "product_id": "P005",
        "name": "Yonex Badminton Racket GR-303",
        "category": "Sports Equipment",
        "price": 724,
        "mrp": 1149,
        "discount": "37%",
        "rating": 3.8,
        "image_url": "static/images/product_5.png"
    },
    {
        "product_id": "P006",
        "name": "Strauss Adjustable Dumbbells 5kg",
        "category": "Fitness & Training",
        "price": 545,
        "mrp": 1049,
        "discount": "48%",
        "rating": 4.4,
        "image_url": "static/images/product_6.png"
    },
    {
        "product_id": "P007",
        "name": "Adidas Yoga Mat (Anti-Slip)",
        "category": "Swimming & Yoga",
        "price": 769,
        "mrp": 999,
        "discount": "23%",
        "rating": 4.1,
        "image_url": "static/images/product_7.png"
    },
    {
        "product_id": "P008",
        "name": "Puma Sports T-shirt (Dryfit)",
        "category": "Apparel & Footwear",
        "price": 494,
        "mrp": 749,
        "discount": "34%",
        "rating": 4.9,
        "image_url": "static/images/product_8.png"
    },
    {
        "product_id": "P009",
        "name": "Nike Training Shoes Men",
        "category": "Apparel & Footwear",
        "price": 1781,
        "mrp": 3299,
        "discount": "46%",
        "rating": 4.6,
        "image_url": "static/images/product_9.png"
    },
    {
        "product_id": "P010",
        "name": "Fitbit Charge 5",
        "category": "Fitness & Training",
        "price": 11999,
        "mrp": 14999,
        "discount": "20%",
        "rating": 4.9,
        "image_url": "static/images/product_10.png"
    },
    {
        "product_id": "P011",
        "name": "Reebok Skipping Rope",
        "category": "Fitness & Training",
        "price": 215,
        "mrp": 499,
        "discount": "57%",
        "rating": 3.7,
        "image_url": "static/images/product_11.png"
    },
    {
        "product_id": "P012",
        "name": "Spalding Marble Basketball",
        "category": "Sports Equipment",
        "price": 1264,
        "mrp": 1405,
        "discount": "10%",
        "rating": 4.5,
        "image_url": "static/images/product_12.png"
    },
    {
        "product_id": "P013",
        "name": "DSC Wicket Keeping Gloves",
        "category": "Sports Equipment",
        "price": 559,
        "mrp": 1299,
        "discount": "57%",
        "rating": 4.7,
        "image_url": "static/images/product_13.png"
    },
    {
        "product_id": "P014",
        "name": "Speedo Swim Goggles",
        "category": "Swimming & Yoga",
        "price": 396,
        "mrp": 899,
        "discount": "56%",
        "rating": 4.5,
        "image_url": "static/images/product_14.png"
    },
    {
        "product_id": "P015",
        "name": "Wildcraft Gym Bag",
        "category": "Accessories",
        "price": 743,
        "mrp": 1199,
        "discount": "38%",
        "rating": 4.0,
        "image_url": "static/images/product_15.png"
    },
    {
        "product_id": "P016",
        "name": "Adjustable Hand Grip Strengthener",
        "category": "Fitness & Training",
        "price": 545,
        "mrp": 699,
        "discount": "22%",
        "rating": 4.0,
        "image_url": "static/images/product_16.png"
    },
    {
        "product_id": "P017",
        "name": "Vector X Shin Guard",
        "category": "Accessories",
        "price": 396,
        "mrp": 649,
        "discount": "39%",
        "rating": 4.3,
        "image_url": "static/images/product_17.png"
    },
    {
        "product_id": "P018",
        "name": "Butterfly TT Bat Wakaba",
        "category": "Sports Equipment",
        "price": 819,
        "mrp": 999,
        "discount": "18%",
        "rating": 4.9,
        "image_url": "static/images/product_18.png"
    },
    {
        "product_id": "P019",
        "name": "Nivia Football Size 5",
        "category": "Sports Equipment",
        "price": 779,
        "mrp": 999,
        "discount": "22%",
        "rating": 3.6,
        "image_url": "static/images/product_19.png"
    },
    {
        "product_id": "P020",
        "name": "Li-Ning Badminton Kitbag",
        "category": "Sports Equipment",
        "price": 870,
        "mrp": 1299,
        "discount": "33%",
        "rating": 4.2,
        "image_url": "static/images/product_20.png"
    }
]

# Read JSON file
df_products_json = pd.DataFrame(products_json)

# Get updated prices
df_products_json_new_prices = df_products_json.copy()

for index, product in df_products_json_new_prices.iterrows():
    mrp = product['mrp']
    
    # Simulate a flash sale chance
    flash_sale_chance = random()
    if flash_sale_chance < 0.1:  # 10% chance
        discount = randint(45, 65)
    elif flash_sale_chance < 0.25:  # 15% chance for clearance
        discount = randint(35, 50)
    else:  # Normal behavior
        discount = randint(10, 30)

    # Final price calculation
    new_price = round(mrp * (1 - discount / 100))

    # Update fields
    df_products_json_new_prices.at[index, 'price'] = new_price
    df_products_json_new_prices.at[index, 'discount'] = f"{discount}%"



# Define HTML Template for index
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Mechatlon Sports Store</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    html, body {
      height: 100%;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
    }

    body {
      background-color: #f8f9fa;
    }

    main {
      flex: 1;
    }

    .product-card {
      background-color: #fff;
      border: 1px solid #e0e0e0;
      border-radius: 8px;
      padding: 15px;
      height: 100%;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
    }

    .product-image {
      width: 100%;
      height: 180px;
      object-fit: contain;
    }

    .price { color: #B12704; font-weight: bold; }
    .mrp { text-decoration: line-through; color: #888; }

    footer {
      background-color: #343a40;
      color: white;
      padding: 15px 0;
      text-align: center;
    }
  </style>
</head>
<body>

<main class="container mt-4">

  <div class="d-flex justify-content-between align-items-center mb-4">
    <img src="static/images/mecathlon_logo.png" alt="Mecathlon Logo" style="height: 90px;">
    <h2 class="text-center flex-grow-1">🏋️ Mechatlon Sports</h2>
  </div>

  <div class="row mb-3">
    <div class="col-md-6">
      <select id="categoryFilter" class="form-select">
        <option value="all">Filter by Category</option>
      </select>
    </div>
    <div class="col-md-6">
      <select id="ratingSort" class="form-select">
        <option value="default">Sort by Rating</option>
        <option value="asc">Low to High</option>
        <option value="desc">High to Low</option>
      </select>
    </div>
  </div>

  <!-- Product cards -->
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-5 g-4" id="productContainer">
    <!--PRODUCT_CARDS-->
  </div>

  <!-- Pagination Buttons -->
  <div class="d-flex justify-content-center mt-4">
    <button id="prevBtn" class="btn btn-outline-secondary me-2" disabled>Previous</button>
    <button id="nextBtn" class="btn btn-outline-primary">Next</button>
  </div>

</main>

<footer>
  <div class="container">
    <p class="mb-0">© 2025 Mechatlon Sports. All Rights Reserved.</p>
  </div>
</footer>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".product-card");
    const container = document.getElementById("productContainer");
    const categoryFilter = document.getElementById("categoryFilter");
    const ratingSort = document.getElementById("ratingSort");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");

    const PRODUCTS_PER_PAGE = 10;
    let currentPage = 1;
    let filteredData = [];

    const productData = Array.from(cards).map(card => ({
      element: card.parentElement,
      name: card.querySelector(".product-name").textContent,
      rating: parseFloat(card.querySelector(".rating").textContent),
      category: card.getAttribute("data-category")
    }));

    const uniqueCategories = [...new Set(productData.map(p => p.category))];
    uniqueCategories.forEach(cat => {
      const option = document.createElement("option");
      option.value = cat;
      option.textContent = cat;
      categoryFilter.appendChild(option);
    });

    function renderFiltered() {
      const selectedCat = categoryFilter.value;
      const sortVal = ratingSort.value;

      filteredData = [...productData];
      if (selectedCat !== "all") {
        filteredData = filteredData.filter(p => p.category === selectedCat);
      }

      if (sortVal === "asc") {
        filteredData.sort((a, b) => a.rating - b.rating);
      } else if (sortVal === "desc") {
        filteredData.sort((a, b) => b.rating - a.rating);
      }

      currentPage = 1;
      renderPage();
    }

    function renderPage() {
      const startIndex = (currentPage - 1) * PRODUCTS_PER_PAGE;
      const endIndex = startIndex + PRODUCTS_PER_PAGE;
      const currentItems = filteredData.slice(startIndex, endIndex);

      container.innerHTML = "";
      currentItems.forEach(p => container.appendChild(p.element));

      prevBtn.disabled = currentPage === 1;
      nextBtn.disabled = endIndex >= filteredData.length;
    }

    categoryFilter.addEventListener("change", renderFiltered);
    ratingSort.addEventListener("change", renderFiltered);
    prevBtn.addEventListener("click", () => {
      if (currentPage > 1) {
        currentPage--;
        renderPage();
      }
    });
    nextBtn.addEventListener("click", () => {
      if ((currentPage * PRODUCTS_PER_PAGE) < filteredData.length) {
        currentPage++;
        renderPage();
      }
    });

    // Initial Load
    filteredData = productData;
    renderPage();
  });
</script>

</body>
</html>
"""

# 3. HTML card block for each product
card_template = """
  <div class="col">
    <div class="product-card h-100" data-category="{category}">
      <img src="{image_url}" alt="{name}" class="product-image mb-2">
      <h6 class="product-name">{name}</h6>
      <p class="mb-1">
        <span class="price">₹{price}</span>
        <span class="mrp">₹{mrp}</span>
        <small class="text-success">({discount} OFF)</small>
      </p>
      <p class="mb-1">⭐ <span class="rating">{rating}</span></p>
    </div>
  </div>
"""

product_html_blocks = ""
for index, product in df_products_json_new_prices.iterrows():
    product_html_blocks += card_template.format(
        name=product["name"],
        image_url=product["image_url"],
        price=product["price"],
        mrp=product["mrp"],
        discount=product["discount"],
        rating=product["rating"],
        category = product['category']
    )

# Step 5: Replace placeholder and save
updated_html = html_template.replace("<!--PRODUCT_CARDS-->", product_html_blocks)

# Step 6: Save to file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print("✅ index.html generated successfully.")












