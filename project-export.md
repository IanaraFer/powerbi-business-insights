# 📊 Stakeholder Engagement Dashboard – Power BI

## Project Overview
This Power BI dashboard provides insights into stakeholder engagement across departments and time periods. It’s designed to help organizations monitor performance, identify trends, and make data-driven decisions.

### Project Goals
- Visualize stakeholder activity and feedback
- Track KPIs like engagement frequency, satisfaction, and response time
- Enable drill-through analysis for deeper insights

### Tools Used
- Power BI Desktop
- Excel (for data source simulation)
- DAX for calculated metrics
- GitHub for version control

### Files Included
- `StakeholderDashboard.pbix` – Main Power BI file
- `data.xlsx` – Simulated dataset
- `README.md` – Project overview

### Key Visuals
- Line chart: Engagement over time
- Bar chart: Department comparison
- Card visuals: KPIs
- Slicer: Filter by stakeholder type

### Skills Demonstrated
- Data modeling and transformation
- DAX calculations
- Interactive report design
- Business storytelling through visuals

---

# Data Structure

## Excel Data Tables
### Table 1: Stakeholder_Data
| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| StakeholderID | Text | Unique identifier | STK001, STK002, STK003 |
| StakeholderName | Text | Full name | John Smith, Sarah Johnson, Mike Chen |
| Department | Text | Department/Division | HR, Finance, IT, Marketing, Operations |
| StakeholderType | Text | Category of stakeholder | Internal, External, Partner, Customer |
| ContactEmail | Text | Email address | john.smith@company.com |
| JoinDate | Date | When they became a stakeholder | 01/01/2023, 15/03/2023 |
| Region | Text | Geographic location | North America, Europe, Asia Pacific |
| Priority | Text | Engagement priority | High, Medium, Low |

### Table 2: Engagement_Activities
| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| ActivityID | Text | Unique activity identifier | ACT001, ACT002 |
| StakeholderID | Text | Links to Stakeholder_Data | STK001, STK002 |
| ActivityDate | Date | When activity occurred | 15/01/2024, 22/02/2024 |
| ActivityType | Text | Type of engagement | Meeting, Email, Survey, Workshop |
| Channel | Text | Communication method | Face-to-face, Video Call, Email, Phone |
| Duration_Minutes | Number | Length of engagement | 30, 60, 90, 120 |
| Initiated_By | Text | Who started the engagement | Stakeholder, Internal Team |
| Status | Text | Activity status | Completed, Scheduled, Cancelled |
| Follow_Up_Required | Text | Yes/No | Yes, No |

### Table 3: Feedback_Scores
| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| FeedbackID | Text | Unique feedback identifier | FB001, FB002 |
| ActivityID | Text | Links to Engagement_Activities | ACT001, ACT002 |
| SatisfactionScore | Number | 1-5 rating scale | 1, 2, 3, 4, 5 |
| ResponseTime_Hours | Number | Hours to respond | 2, 4, 8, 24, 48 |
| EngagementQuality | Text | Qualitative assessment | Excellent, Good, Fair, Poor |
| NPS_Score | Number | Net Promoter Score | -100 to 100 |
| Comments | Text | Open feedback | "Great meeting", "Need more details" |
| FeedbackDate | Date | When feedback was given | 16/01/2024, 23/02/2024 |

### Table 4: KPI_Targets
| Column Name | Data Type | Description | Sample Values |
|-------------|-----------|-------------|---------------|
| KPI_Name | Text | Key Performance Indicator | Satisfaction Score, Response Time |
| Target_Value | Number | Goal/benchmark | 4.0, 24 |
| Current_Period | Text | Time period | Q1 2024, Q2 2024 |
| Department | Text | Applicable department | All, HR, Finance |

---

# Sample Data

## Stakeholder_Data
```csv
StakeholderID,StakeholderName,Department,StakeholderType,ContactEmail,JoinDate,Region,Priority
STK001,John Smith,HR,Internal,john.smith@company.com,1/1/2023,North America,High
STK002,Sarah Johnson,Finance,Internal,sarah.johnson@company.com,2/15/2023,Europe,High
STK003,Mike Chen,IT,Internal,mike.chen@company.com,3/10/2023,Asia Pacific,Medium
... (see full CSV for more)
```

## Engagement_Activities
```csv
ActivityID,StakeholderID,ActivityDate,ActivityType,Channel,Duration_Minutes,Initiated_By,Status,Follow_Up_Required
ACT001,STK001,1/15/2024,Meeting,Face-to-face,60,Internal Team,Completed,Yes
ACT002,STK001,1/22/2024,Email,Email,0,Stakeholder,Completed,No
ACT003,STK002,1/18/2024,Survey,Email,0,Internal Team,Completed,Yes
... (see full CSV for more)
```

## Feedback_Scores
```csv
FeedbackID,ActivityID,SatisfactionScore,ResponseTime_Hours,EngagementQuality,NPS_Score,Comments,FeedbackDate
FB001,ACT001,4,2,Excellent,8,Great discussion about Q1 goals,1/16/2024
FB002,ACT003,5,4,Excellent,9,Very comprehensive survey,1/19/2024
FB003,ACT004,3,8,Good,6,Workshop was informative but long,1/21/2024
... (see full CSV for more)
```

## KPI_Targets
```csv
KPI_Name,Target_Value,Current_Period,Department
Satisfaction Score,4.0,Q1 2024,All
Response Time,24,Q1 2024,All
Engagement Frequency,2.5,Q1 2024,All
... (see full CSV for more)
```

---

# DAX Calculations
```dax
// Total Stakeholders
Total Stakeholders = DISTINCTCOUNT(Stakeholder_Data[StakeholderID])

// Average Satisfaction Score
Avg Satisfaction = AVERAGE(Feedback_Scores[SatisfactionScore])

// Average Response Time
Avg Response Time = AVERAGE(Feedback_Scores[ResponseTime_Hours])

// Engagement Frequency (activities per stakeholder)
Engagement Frequency = 
DIVIDE(
    COUNTROWS(Engagement_Activities),
    DISTINCTCOUNT(Engagement_Activities[StakeholderID])
)

// Satisfaction Target Achievement
Satisfaction Achievement = 
VAR CurrentSat = [Avg Satisfaction]
VAR Target = 4.0
RETURN IF(CurrentSat >= Target, "Met", "Not Met")

// Monthly Engagement Trend
Monthly Engagement = 
CALCULATE(
    COUNTROWS(Engagement_Activities),
    DATESMTD(Engagement_Activities[ActivityDate])
)
```

---

# Power BI Dashboard Development Guide

## Dashboard Layout and Design
### Page 1: Executive Summary
- KPI Cards: Total Stakeholders, Average Satisfaction Score, Average Response Time, Engagement Frequency
- Line Chart: Engagement Trends Over Time
- Bar Chart: Department Engagement Comparison
- Donut Chart: Stakeholder Distribution
- Gauge Chart: Satisfaction Score vs Target

### Page 2: Detailed Analysis
- Matrix Table: Stakeholder metrics
- Scatter Plot: Engagement Frequency vs Satisfaction Score
- Heat Map Calendar: Engagement activities by date

### Page 3: Performance Dashboard
- KPI Performance Cards: Current vs Target
- Waterfall Chart: Monthly satisfaction score changes

## Slicers and Filters
- Date Range Slicer
- Department Dropdown
- Stakeholder Type
- Region
- Priority Level
- Activity Type
- Engagement Quality

## Color Scheme
- Corporate Blue: #1f4e79
- Accent Green: #70ad47
- Warning Orange: #ff8c00
- Error Red: #d13438
- Neutral Gray: #595959

## Data Refresh & Publishing
- Daily refresh recommended
- Publish to Power BI Service
- Set up row-level security if needed
- Optimize for mobile viewing

---

# Outputs & Insights

- Use the sample data to build visuals as described
- Apply DAX measures for KPIs and trends
- Validate outputs by comparing calculated KPIs to targets
- Use slicers for interactive analysis

---

# Contact
📧 ianarafer@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ianarafernandes/)
