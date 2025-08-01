# Data Structure for Stakeholder Engagement Dashboard

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

## Sample Data Rows

### Stakeholder_Data (20 rows)
```
STK001,John Smith,HR,Internal,john.smith@company.com,01/01/2023,North America,High
STK002,Sarah Johnson,Finance,Internal,sarah.johnson@company.com,15/02/2023,Europe,High
STK003,Mike Chen,IT,Internal,mike.chen@company.com,10/03/2023,Asia Pacific,Medium
STK004,Lisa Brown,Marketing,Internal,lisa.brown@company.com,22/04/2023,North America,High
STK005,David Wilson,Operations,Internal,david.wilson@company.com,05/05/2023,Europe,Medium
STK006,Emma Davis,External,Partner,emma.davis@partner.com,18/06/2023,North America,High
STK007,Alex Rodriguez,External,Customer,alex.rodriguez@customer.com,30/07/2023,North America,Medium
STK008,Sophie Martin,HR,Internal,sophie.martin@company.com,12/08/2023,Europe,Low
STK009,James Taylor,Finance,Internal,james.taylor@company.com,25/09/2023,Asia Pacific,Medium
STK010,Rachel Green,IT,Internal,rachel.green@company.com,08/10/2023,North America,High
```

### Engagement_Activities (50 rows sample)
```
ACT001,STK001,15/01/2024,Meeting,Face-to-face,60,Internal Team,Completed,Yes
ACT002,STK001,22/01/2024,Email,Email,0,Stakeholder,Completed,No
ACT003,STK002,18/01/2024,Survey,Email,0,Internal Team,Completed,Yes
ACT004,STK003,20/01/2024,Workshop,Video Call,120,Internal Team,Completed,No
ACT005,STK004,25/01/2024,Meeting,Video Call,45,Stakeholder,Completed,Yes
```

### Feedback_Scores (45 rows sample)
```
FB001,ACT001,4,2,Excellent,8,Great discussion about Q1 goals,16/01/2024
FB002,ACT003,5,4,Excellent,9,Very comprehensive survey,19/01/2024
FB003,ACT004,3,8,Good,6,Workshop was informative but long,21/01/2024
FB004,ACT005,4,1,Excellent,8,Quick and efficient meeting,25/01/2024
```

## Instructions for Creating Excel File

1. **Create a new Excel workbook** named `data.xlsx`
2. **Create 4 worksheets** with the names:
   - Stakeholder_Data
   - Engagement_Activities
   - Feedback_Scores
   - KPI_Targets
3. **Add headers** as specified in each table above
4. **Populate with sample data** - aim for:
   - 20-30 stakeholders
   - 80-100 engagement activities
   - 60-80 feedback records
   - 8-10 KPI targets
5. **Format dates** as DD/MM/YYYY
6. **Save the file** in the project directory

## DAX Calculations to Implement

### Key Measures
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
