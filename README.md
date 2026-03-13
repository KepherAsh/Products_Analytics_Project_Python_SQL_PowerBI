## Problem Statement

### Business Context

NordicFlow CRM is a European B2B SaaS company that provides a subscription-based customer relationship management platform designed for small and mid-sized businesses. The product supports sales teams by enabling lead management, deal tracking, pipeline configuration, and workflow automation within a centralized system.

In a competitive CRM market, NordicFlow differentiates itself through usability, workflow-driven design, and a strong focus on **GDPR-first data privacy and compliance**. However, as the company has grown across the Nordic and European markets, leadership has encountered several **data-driven challenges related to product adoption, activation, and customer retention**. :contentReference[oaicite:0]{index=0}

---

### Core Business Problem

While trial signups for NordicFlow have steadily increased, **activation and long-term product adoption remain inconsistent**. Many users create accounts but fail to reach the stage where the CRM becomes embedded in their daily workflow. In addition, surface-level activity such as logins can be mistaken for meaningful engagement, making it difficult to accurately measure whether the product is delivering real value to customers. :contentReference[oaicite:1]{index=1}

This lack of clarity creates several operational challenges:

- Difficulty identifying **which behaviors indicate successful product adoption**
- Inability to distinguish between **superficial usage and true engagement**
- Early customer churn among small and mid-sized businesses
- Conflicting dashboards and metrics across teams, leading to **inconsistent decision-making**

Without a unified analytical framework, product, growth, and customer success teams struggle to determine **why users fail to activate and how to improve time-to-value for new customers**.

---

### Analytical Objective

The objective of this project is to **build a structured product analytics pipeline** that transforms raw product event data into actionable insights about user behavior, activation, and engagement.

This involves:

1. **Integrating product event data and operational data sources**
2. **Designing a clean analytical data model**
3. **Defining trusted metrics for product usage and activation**
4. **Building dashboards that provide consistent insights across teams**

The goal is to move from fragmented reporting toward **evidence-based decision-making that helps NordicFlow improve onboarding, increase activation rates, and reduce early-stage churn**.

---

### Technical Approach

To address this problem, the project implements an end-to-end analytics workflow using the following tools:

**Python**
- Data ingestion and transformation
- Data cleaning and feature engineering
- Implementation of the Raw → Bronze → Silver data processing stages

**PostgreSQL**
- Centralized storage of processed analytical datasets
- Data modeling for scalable querying and metric calculation
- Serving as the single source of truth for downstream analytics

**Power BI**
- Development of interactive dashboards
- Visualization of key product analytics metrics
- Enabling stakeholders across Product, Growth, and Customer Success teams to explore user behavior and engagement trends

---

### Expected Outcome

By implementing a structured analytics workflow and unified reporting layer, this project aims to:

- Clarify **what behaviors indicate meaningful product adoption**
- Identify **early signals of successful user activation**
- Provide leadership with **consistent and trustworthy product metrics**
- Enable data-driven initiatives to improve onboarding and reduce churn

Ultimately, the analysis helps transform raw product usage data into **actionable insights that support product-led growth and long-term customer value creation**.
