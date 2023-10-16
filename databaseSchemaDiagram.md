```
  +--------------+    +--------------+
  |     User     |    |     Exam     |
  +--------------+    +--------------+
  | user_id (PK) |    | exam_id (PK) |
  | username     |    | title        |
  | email        |    | description  |
  | password     |    | duration     |
  | registration_date | | pass_marks   |
  | last_login   |    | created_by (FK to User) |
  | subscription_status | | creation_date |
  | ...          |    | code         |
  |              |    +--------------+
  +--------------+
        |
        |
        v
  +--------------+
  |  UserExamRole  |
  +--------------+
  | user_exam_role_id (PK) |
  | user_id (FK to User)  |
  | exam_id (FK to Exam)  |
  | role (e.g., teacher, student) |
  +--------------+
        |
        |
        v
  +--------------+
  |  Question    |
  +--------------+
  | question_id (PK) |
  | exam_id (FK to Exam) |
  | category_id (FK to Category) |
  | question_text   |
  | question_type   |
  | options         |
  | correct_answer  |
  | ...             |
  +--------------+
        |
        |
        v
  +--------------+
  | Category     |
  +--------------+
  | category_id (PK) |
  | category_name    |
  | description      |
  | parent_category_id (FK to Category, for subcategories) |
  +--------------+
        |
        |
        v
  +-------------------+
  | UserSubscription  |
  +-------------------+
  | subscription_id (PK) |
  | user_id (FK to User) |
  | subscription_type   |
  | start_date         |
  | end_date           |
  | payment_status     |
  | ...               |
  +-------------------+
        |
        |
        v
  +------------------------+
  | UserExamAttempt        |
  +------------------------+
  | attempt_id (PK)        |
  | user_id (FK to User)   |
  | exam_id (FK to Exam)   |
  | start_time             |
  | end_time               |
  | status (e.g., in progress, completed) |
  | user_answers (store responses to questions) |
  | ...                    |
  +------------------------+
        |
        |
        v
  +--------------------------+
  | MachineLearningRecommendation  |
  +--------------------------+
  | recommendation_id (PK) |
  | user_id (FK to User)    |
  | exam_id (FK to Exam)    |
  | recommended_question_ids (list of recommended question IDs) |
  +--------------------------+
        |
        |
        v
  +---------------+
  | UserProfile   |
  +---------------+
  | profile_id (PK) |
  | user_id (FK to User) |
  | name            |
  | contact_details |
  | educational_background |
  | ...             |
  +---------------+
        |
        |
        v
  +---------------+
  | UserAvatar    |
  +---------------+
  | avatar_id (PK) |
  | user_id (FK to User) |
  | avatar_path    |
  +---------------+
        |
        |
        v
  +--------------+
  | Announcement |
  +--------------+
  | announcement_id (PK) |
  | title        |
  | content      |
  | publish_date |
  | ...          |
  +--------------+
        |
        |
        v
  +--------------+
  | UserMessage  |
  +--------------+
  | message_id (PK) |
  | sender_id (FK to User) |
  | recipient_id (FK to User) |
  | subject      |
  | message_text |
  | send_date    |
  | ...          |
  +--------------+
```
```sql
-- Create the User table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'teacher', 'student') NOT NULL,
    registration_date TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    subscription_status ENUM('active', 'expired', 'canceled') NOT NULL
);

-- Create the Exam table
CREATE TABLE Exam (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    duration INT NOT NULL,
    pass_marks INT NOT NULL,
    created_by INT NOT NULL, -- Foreign key to User table
    creation_date TIMESTAMP NOT NULL,
    code VARCHAR(10) UNIQUE NOT NULL
);

-- Create the Question table
CREATE TABLE Question (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    exam_id INT NOT NULL, -- Foreign key to Exam table
    category_id INT, -- Foreign key to Category table
    question_text TEXT NOT NULL,
    question_type ENUM('multiple-choice', 'true-false', 'short-answer') NOT NULL,
    options TEXT, -- For multiple-choice questions
    correct_answer TEXT, -- For multiple-choice questions
);

-- Create the Category table
CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    parent_category_id INT, -- For subcategories
);

-- Create the UserExamAttempt table
CREATE TABLE UserExamAttempt (
    attempt_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL, -- Foreign key to User table
    exam_id INT NOT NULL, -- Foreign key to Exam table
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    status ENUM('in progress', 'completed') NOT NULL,
    user_answers JSON, -- Store responses to questions in JSON format
);

-- Create the MachineLearningRecommendation table
CREATE TABLE MachineLearningRecommendation (
    recommendation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL, -- Foreign key to User table
    exam_id INT NOT NULL, -- Foreign key to Exam table
    recommended_question_ids TEXT -- Store recommended question IDs as a list
);
```
