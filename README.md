# Yelp Nevada Analysis – Big Data Project (CIS 4560)

**Author:** Ruben Chagollan  
**Course:** Introduction to Big Data – CIS 4560  
**Instructor:** Dr. Woo  
**Dataset Source:** Yelp Open Dataset (8+ GB)

---

### 📌 Project Goal
Analyze business trends and customer satisfaction in the state of Nevada using distributed big data tools including Hadoop, HDFS, and Hive.

---

### 📊 Analysis Questions
This project answers:
1. How many Yelp businesses exist in Nevada?
2. Which Nevada cities have the most businesses?
3. What are the top business categories?
4. Which cities have the highest average ratings?
5. What percentage of businesses are open vs. closed?

---

### 🧠 Tools & Technology
| Component | Usage |
|----------|-------|
| Python | JSON → CSV conversion |
| Hadoop HDFS | Distributed storage |
| Hive | Distributed SQL processing |
| PowerPoint / Excel | Visualizations |
| GitHub | Version control and deliverable hosting |

---

### 📂 Repository Structure
code/ → Python + Hive scripts
results/ → Generated charts & screenshots
tutorial/ → Project Lab Tutorial document
slides/ → Presentation (PPTX + PDF)

---

### 🏗 Project Workflow
1. Download Yelp dataset (JSON)
2. Convert to CSV using Python ETL script
3. Upload CSV to Linux → HDFS storage
4. Create Hive external table
5. Run SQL tempo-spatial analysis queries
6. Visualize results in charts

---

### 🔗 Resources
- Yelp Dataset: https://www.yelp.com/dataset
- GitHub Repo: https://github.com/rchago7/yelp-nevada-analysis

---

### 📈 Key Findings
- Reno + Sparks = majority of Nevada Yelp businesses
- Restaurants are the most common category
- Virginia City has the highest average rating (min 20 listings)
- ~80% of businesses are currently open

---

### 🙌 Acknowledgment
This project was developed as part of the CIS 4560 curriculum at Cal State LA.
