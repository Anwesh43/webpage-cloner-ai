from services.save_html_service import SaveHTMLService

html = """
<!DOCTYPE html>
<html>
<head>
  <title>Amazon.in Homepage</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header>
    <!-- Header elements (logo, search, etc.) -->
  </header>

  <main>
    <!-- Banner Carousel -->
    <div class="banner-carousel">
      <!-- Carousel Items -->
    </div>

    <!-- Category Highlights -->
    <section class="category-highlights">
      <!-- Appliance Section -->
      <div class="category-item">
        <img src="air-conditioner.jpg" alt="Air Conditioners">
        <h3>Air Conditioners</h3>
      </div>
      <!-- ... other category items -->
    </section>

    <!-- Product Grids -->
    <section class="product-grid">
      <!-- Product Card 1 -->
      <div class="product-card">
        <img src="refrigerator.jpg" alt="Refrigerator">
        <h3>Refrigerator</h3>
        <p>₹15,000</p>
      </div>
      <!-- Product Card 2 -->
       <div class="product-card">
        <img src="washing-machine.jpg" alt="Washing Machine">
        <h3>Washing Machine</h3>
        <p>₹20,000</p>
      </div>
       <!-- ... other product cards -->
    </section>

    <!--Secondary Promotions-->
    <section class="secondary-promotions">
      <!-- ... various promo sections -->
    </section>
  </main>

  <footer>
    <!-- Footer elements -->
  </footer>

</body>
</html>
"""
if __name__ == "__main__":
    SaveHTMLService.saveHTML(html, fileName="test.html")