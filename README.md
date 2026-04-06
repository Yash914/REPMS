# Real Estate Data Intelligence and Transaction Management System

## Overview

The Real Estate Data Intelligence and Transaction Management System is a database-driven application designed to manage real estate operations efficiently. It integrates property management, customer relationship management (CRM), transaction processing, and analytical reporting within a single relational database system.

The project emphasizes strong database design principles, including normalization, data integrity, automation through triggers, and business logic implementation using stored procedures. It simulates a real-world real estate platform similar to commercial systems used by property management companies.

---

## Objectives

* To design a normalized relational database for real estate operations
* To implement database-level business logic using triggers and stored procedures
* To ensure data integrity using constraints and foreign keys
* To provide analytical insights using views and complex queries
* To simulate real-world workflows such as lead management and property transactions

---

## System Architecture

The system is built using MySQL as the core database. All business logic is embedded within the database layer rather than relying on external application logic.

The architecture consists of:

* Data Layer: MySQL database with structured schema
* Logic Layer: Stored procedures and triggers
* Presentation Layer (optional): Streamlit UI for visualization and interaction

---

## Database Design

The database follows normalization principles to reduce redundancy and improve consistency.

### Main Tables

1. Users
   Stores all system users including administrators, agents, property owners, and buyers.

2. Properties
   Contains property listings with details such as location, price, and status.

3. PropertyFeatures
   Stores additional attributes like bedrooms, bathrooms, and area.

4. Leads
   Represents potential buyers and tracks their interaction stages in the sales pipeline.

5. Transactions
   Records completed property sales.

6. Payments
   Stores payment details associated with transactions.

7. Favorites
   Tracks user interest in specific properties.

8. AuditLog
   Maintains logs of important database operations for monitoring and debugging.

---

## Functional Modules

### Property Management

The system allows storing and managing property listings. Each property is linked to an owner and contains attributes such as price, location, and status.

### User Management

Users are categorized into roles such as ADMIN, AGENT, OWNER, and BUYER. This role-based structure helps simulate real-world access and responsibilities.

### Lead Management (CRM)

Leads represent potential buyers. Each lead progresses through different stages:

* NEW
* CONTACTED
* VISITED
* OFFER_MADE
* CLOSED
* LOST

This module helps track customer interactions and conversion rates.

### Transaction Management

Transactions represent successful property sales. Each transaction is associated with a buyer and a property.

### Payment Management

Payments are recorded for each transaction, ensuring financial tracking and validation.

---

## Database Automation

### Triggers

Triggers automate critical operations:

* Property Status Update
  When a transaction is inserted, the corresponding property is automatically marked as SOLD.

* Payment Validation
  Prevents insertion of invalid payment amounts such as zero or negative values.

* Audit Logging
  Important actions are recorded in the AuditLog table for traceability.

### Stored Procedures

Stored procedures encapsulate business logic:

* RecommendProperties
  Returns properties based on city and budget constraints.

* ExecuteTransaction
  Handles complete transaction flow using ACID properties (atomicity, consistency, isolation, durability).

* UpdateLeadStatus
  Updates the status of a lead and logs the change.

---

## Views and Analytics

Views are used to simplify complex queries and provide analytical insights.

* vw_RevenueByCity
  Calculates total revenue generated per city.

* vw_LeadConversion
  Displays the number of leads in each stage.

* vw_AvailableProperties
  Lists properties currently available for sale.

---

## Analytical Queries

The system supports advanced queries such as:

* Revenue aggregation by location
* Lead conversion rate calculation
* Identification of top-performing cities
* Property demand analysis based on leads

These queries help in decision-making and performance evaluation.

---

## Transaction Handling

The system demonstrates transaction management using SQL transactions:

* START TRANSACTION
* COMMIT
* ROLLBACK

This ensures that operations are executed reliably and consistently, especially in cases of errors.

---

## Key Features

* Fully normalized database design
* Strong use of foreign keys and constraints
* Automation using triggers
* Business logic embedded using stored procedures
* Real-world CRM pipeline simulation
* Analytical reporting using views
* Data validation at database level
* Transaction safety using ACID principles

---

## How to Run the Project

1. Open MySQL client
2. Create or open a database
3. Execute the SQL script file:

   ```
   SOURCE path/to/real_estate_dbms.sql;
   ```
4. Verify tables using:

   ```
   SHOW TABLES;
   ```
5. Run sample queries and procedures to test functionality

---

## Conclusion

This project demonstrates a comprehensive database system that goes beyond basic CRUD operations. It integrates data management, automation, analytics, and transaction control within a single platform.

By embedding business logic directly into the database, the system ensures consistency, reduces dependency on external applications, and reflects real-world enterprise-level database design practices.

---

## Future Enhancements

* Integration with a web-based frontend
* Role-based authentication system
* Advanced analytics using machine learning
* Geolocation-based property search
* Performance optimization for large-scale datasets

---
