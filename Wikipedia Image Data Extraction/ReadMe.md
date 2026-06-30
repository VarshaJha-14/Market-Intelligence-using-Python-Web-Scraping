# 🖼️ Wikipedia Image Analytics using Python & BeautifulSoup

> A Python web scraping project that extracts image metadata from a Wikipedia article and analyzes image dimensions to identify the largest visual asset on the page.

---

# 📖 Overview

Images play an important role in digital content, improving readability, engagement, and information delivery.

This project demonstrates how Python and BeautifulSoup can be used to automatically collect image metadata from a Wikipedia page and perform basic analysis on the extracted information.

The project focuses on HTML parsing, metadata extraction, and simple image analysis.

---

# 🎯 Problem Statement

Suppose you're building a content intelligence system.

Before downloading or processing website images, you need to automatically collect metadata such as:

- Image URLs
- Image dimensions
- Largest image on the webpage

Instead of manually inspecting HTML, this project automates the process.

---

# 🚀 Features

✅ Scrapes all image tags from a Wikipedia article

✅ Extracts image source URLs

✅ Retrieves image height and width attributes

✅ Calculates image area

✅ Identifies the largest image on the page

---

# 🛠 Tech Stack

- Python
- BeautifulSoup
- Requests

---

# 📊 Analysis Performed

### Image Extraction

Collects every image available on the selected Wikipedia page.

---

### Metadata Extraction

Extracts:

- Image URL
- Height
- Width

---

### Image Size Analysis

Calculates:

```
Area = Height × Width
```

and identifies the image occupying the largest display area.

---

# 📈 Workflow

```text
Wikipedia Article

↓

HTTP Request

↓

HTML Parsing

↓

Image Extraction

↓

Metadata Collection

↓

Area Calculation

↓

Largest Image Detection
```

# 💡 Potential Applications

The techniques demonstrated in this project can be applied to:

- Web Content Analysis
- Media Asset Management
- Digital Publishing
- SEO Audits
- Website Quality Assessment
- Image Dataset Generation

---

# 📚 Skills Demonstrated

- Web Scraping
- HTML Parsing
- Metadata Extraction
- Python Automation
- Data Processing
- BeautifulSoup
- Requests Library

---

# 🚀 Future Improvements

If I revisit this project today, I would:

- Download image files automatically
- Export image metadata to CSV
- Analyze image formats (PNG, JPG, SVG)
- Visualize image size distribution
- Detect duplicate images
- Build a reusable image crawler

---

# 🎯 Key Learning Outcomes

Through this project I learned how to:

- Parse HTML documents
- Locate image elements using BeautifulSoup
- Extract HTML attributes
- Process metadata programmatically
- Perform simple analytical calculations on scraped data

---

# 📝 Note

This repository represents one of my early Python projects created while learning web scraping and HTML parsing. It has been preserved to showcase foundational web scraping concepts that later contributed to my work in analytics, automation, and product-focused projects.
