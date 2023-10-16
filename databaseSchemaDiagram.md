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
