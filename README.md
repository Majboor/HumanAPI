
## Authentication

This API does not require authentication for the listed endpoints. If you plan to integrate authentication, ensure your middleware is set up accordingly.

---

## Endpoints

### Profile Endpoints

1. **Create Profile**
   - **URL**: `/api/profiles/create/`
   - **Method**: `POST`
   - **Description**: Creates a new user profile.
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com",
       "phone": "1234567890"
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com",
       "phone": "1234567890"
     }
     ```

2. **Check Profile**
   - **URL**: `/api/profiles/check/`
   - **Method**: `GET`
   - **Description**: Checks if a profile exists based on certain parameters.
   - **Response**:
     ```json
     {
       "status": "Profile exists"
     }
     ```

3. **Fetch Profile**
   - **URL**: `/api/profiles/fetch/`
   - **Method**: `GET`
   - **Description**: Fetches a profile by a given user ID.
   - **Response**:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com",
       "phone": "1234567890"
     }
     ```

---

### Skill Path Endpoints

1. **Create Skill Path**
   - **URL**: `/api/skill-path/create/`
   - **Method**: `POST`
   - **Description**: Creates a new skill path for a user.
   - **Request Body**:
     ```json
     {
       "user_id": 1,
       "skills": ["Python", "Django", "Machine Learning"]
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "user_id": 1,
       "skills": ["Python", "Django", "Machine Learning"]
     }
     ```

2. **Fetch Skill Path**
   - **URL**: `/api/skill-path/fetch/`
   - **Method**: `GET`
   - **Description**: Fetches the skill path of a user by their ID.
   - **Response**:
     ```json
     {
       "id": 1,
       "user_id": 1,
       "skills": ["Python", "Django", "Machine Learning"]
     }
     ```

---

### Aptitude Test Endpoints

1. **Create Aptitude Test**
   - **URL**: `/api/aptitude-test/create/`
   - **Method**: `POST`
   - **Description**: Creates a new aptitude test for a user.
   - **Request Body**:
     ```json
     {
       "user_id": 1,
       "score": 85
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "user_id": 1,
       "score": 85
     }
     ```

2. **Fetch Aptitude Test**
   - **URL**: `/api/aptitude-test/fetch/`
   - **Method**: `GET`
   - **Description**: Fetches the aptitude test score of a user.
   - **Response**:
     ```json
     {
       "id": 1,
       "user_id": 1,
       "score": 85
     }
     ```

---

### Quiz Endpoints

1. **Create Quiz**
   - **URL**: `/api/quiz/create/`
   - **Method**: `POST`
   - **Description**: Creates a new quiz for a user.
   - **Request Body**:
     ```json
     {
       "user_id": 1,
       "quiz_data": {
         "question_1": "What is Python?",
         "answer_1": "Programming language"
       }
     }
     ```
   - **Response**:
     ```json
     {
       "id": 1,
       "user_id": 1,
       "quiz_data": {
         "question_1": "What is Python?",
         "answer_1": "Programming language"
       }
     }
     ```

2. **Fetch Quiz**
   - **URL**: `/api/quiz/fetch/`
   - **Method**: `GET`
   - **Description**: Fetches the quiz details of a user.
   - **Response**:
     ```json
     {
       "id": 1,
       "user_id": 1,
       "quiz_data": {
         "question_1": "What is Python?",
         "answer_1": "Programming language"
       }
     }
     ```

---

### Job Listings Endpoints

1. **Fetch Job Listings**
   - **URL**: `/api/job-listings/fetch/`
   - **Method**: `GET`
   - **Description**: Fetches available job listings.
   - **Response**:
     ```json
     {
       "job_listings": [
         {
           "id": 1,
           "title": "Python Developer",
           "company": "Tech Corp",
           "location": "Remote",
           "salary": "80,000 USD"
         },
         {
           "id": 2,
           "title": "Data Scientist",
           "company": "Data Solutions",
           "location": "New York",
           "salary": "90,000 USD"
         }
       ]
     }
     ```

---

## Example Request using `curl`

You can make requests to these endpoints using tools like `curl` or Postman. Here is an example of how you would create a profile using `curl`:

```bash
curl -X POST http://localhost:8000/api/profiles/create/ \
    -H "Content-Type: application/json" \
    -d '{"name": "John Doe", "email": "john.doe@example.com", "phone": "1234567890"}'
