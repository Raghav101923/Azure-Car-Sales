# Car Sales Data Engineering Project

## 📋 Overview

This project demonstrates an end-to-end data engineering pipeline for processing and analyzing car sales data using Azure technologies. The focus is on building a scalable, efficient workflow for data ingestion, transformation, and analysis to derive actionable insights from the data.

### Technologies and Tools Used

- **Azure Data Factory (ADF)**: For orchestrating data ingestion workflows.
- **Azure Data Lake Gen2**: For efficient storage of raw and transformed data.
- **Azure Databricks**: For data transformation and analytics using Apache Spark.
- **Delta Lake**: For ensuring data consistency and enabling ACID transactions.
- **Power BI**: For creating dashboards and visualizing insights (in progress).

---

## 🛠 Data Architecture

### Workflow Overview

The project workflow comprises the following components:

1. **Data Source**:
   - Data is sourced from a SQL database.
   - The raw data is uploaded and accessed via Azure Data Factory.

2. **Data Ingestion**:
   - Raw data is ingested into Azure Data Lake Gen2 using ADF pipelines.
   - Implemented incremental loading using watermarks to track updates and ensure efficient processing.

3. **Data Transformation**:
   - Performed transformations using Azure Databricks with PySpark.
   - Tasks included cleaning, aggregating, and creating structured dimensional models.

4. **Data Serving**:
   - Finalized data is stored in Delta Lake with a star schema structure, making it analytics-ready.

5. **Reporting**:
   - Power BI is used for creating dashboards to visualize insights like sales trends and dealership performance.

---

## 🔍 Detailed Workflow

### 1. Data Ingestion

- **Pipeline**:
  - Designed pipelines in Azure Data Factory for seamless data ingestion.
  - Incremental loading managed through watermarks to handle updates efficiently.

- **Storage**:
  - Raw data is stored in Azure Data Lake Gen2 in Parquet format for optimized retrieval and analytics.

### 2. Data Transformation

- **Databricks**:
  - Used PySpark for distributed data processing and transformation.
  - Structured the data into silver (cleaned data) and gold (aggregated data) layers for efficient analytics.

- **Real-World Outputs**:
  - Created dimensional tables such as `Dim_Branch`, `Dim_Date`, `Dim_Dealer`, and `Dim_Model`.
  - Built fact tables like `Fact_Sales` to capture transactional data.

### 3. Data Serving

- **Delta Lake**:
  - Leveraged Delta Lake for improved data consistency and performance.
  - Organized the data into a star schema for easier querying and reporting.

### 4. Reporting

- **Power BI Dashboards**:
  - Currently developing interactive dashboards to showcase:
    - This is a serverless SQL report.
    - Sales trends over time.
    - Dealership performance metrics.
    - Customer and sales insights.

---

## 🏆 Highlights of Technologies Used

- **Azure Data Factory**: Simplified data ingestion with visual pipelines and automation.
- **Azure Data Lake Gen2**: Scalable and cost-efficient storage for big data workloads.
- **Azure Databricks**: Enabled efficient data transformations with PySpark and distributed computing.
- **Delta Lake**: Ensured data integrity and optimized querying with ACID transactions.
- **Power BI**: Facilitated insightful visualizations for business intelligence (ongoing).

---

## 💡 Key Learnings

- Implemented incremental data ingestion with watermarks in Azure Data Factory.
- Mastered PySpark transformations for cleaning and aggregating large datasets.
- Designed efficient data models with Delta Lake to support analytical queries.
- Learned to structure data into star schema for advanced reporting needs.

---

## 🚀 Future Enhancements

- Integrate real-time data processing with Azure Event Hub.
- Add predictive modeling capabilities to forecast sales trends.
- Enhance Power BI dashboards for advanced interactivity and performance.
- Implement more robust security measures using Azure Key Vault.

Stay tuned for updates on the Power BI visualization component, which will complete this project!
