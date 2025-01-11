# API Documentation

This is the API documentation for the Django project that includes various models related to user profiles, skills, courses, job applications, quizzes, and system configurations. The API is built using Django REST Framework (DRF), providing endpoints for interacting with the models and performing CRUD operations.

## Base URL

The base URL for the API is `/api/`.

---

## Endpoints

### 1. User Profiles (`/user-profiles/`)

- **GET** `/api/user-profiles/`
  - Retrieve a list of all user profiles.
  - **Response**: JSON array of user profile objects.

    **Sample Request**:
    ```bash
    GET /api/user-profiles/
    ```

    **Sample Response**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "english_language_knowledge": true,
        "basic_computing_knowledge": true,
        "profile_picture": "path_to_picture.jpg"
      }
    ]
    ```

- **POST** `/api/user-profiles/`
  - Create a new user profile.
  - **Request**: JSON object with profile data.

    **Sample Request**:
    ```bash
    POST /api/user-profiles/
    {
      "name": "John Doe",
      "english_language_knowledge": true,
      "basic_computing_knowledge": true,
      "profile_picture": "path_to_picture.jpg",
      "left_face_image": "path_to_left_face.jpg",
      "right_face_image": "path_to_right_face.jpg",
      "front_face_image": "path_to_front_face.jpg",
      "voice_embedding": "voice_data_here"
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "english_language_knowledge": true,
      "basic_computing_knowledge": true,
      "profile_picture": "path_to_picture.jpg"
    }
    ```

- **GET** `/api/user-profiles/{id}/`
  - Retrieve a specific user profile by ID.

    **Sample Request**:
    ```bash
    GET /api/user-profiles/1/
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "english_language_knowledge": true,
      "basic_computing_knowledge": true,
      "profile_picture": "path_to_picture.jpg"
    }
    ```

- **PUT** `/api/user-profiles/{id}/`
  - Update a specific user profile by ID.
  - **Request**: JSON object with updated profile data.

    **Sample Request**:
    ```bash
    PUT /api/user-profiles/1/
    {
      "name": "John Doe Updated",
      "english_language_knowledge": false,
      "basic_computing_knowledge": true,
      "profile_picture": "path_to_new_picture.jpg"
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "John Doe Updated",
      "english_language_knowledge": false,
      "basic_computing_knowledge": true,
      "profile_picture": "path_to_new_picture.jpg"
    }
    ```

- **DELETE** `/api/user-profiles/{id}/`
  - Delete a specific user profile by ID.

    **Sample Request**:
    ```bash
    DELETE /api/user-profiles/1/
    ```

    **Sample Response**:
    ```json
    {
      "message": "User profile deleted successfully."
    }
    ```

---

### 2. Skill Paths (`/skill-paths/`)

- **GET** `/api/skill-paths/`
  - Retrieve a list of all skill paths.
  - **Response**: JSON array of skill path objects.

    **Sample Request**:
    ```bash
    GET /api/skill-paths/
    ```

    **Sample Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Web Development",
        "skills": ["HTML", "CSS", "JavaScript"]
      }
    ]
    ```

- **POST** `/api/skill-paths/`
  - Create a new skill path.
  - **Request**: JSON object with skill path data.

    **Sample Request**:
    ```bash
    POST /api/skill-paths/
    {
      "name": "Data Science",
      "skills": ["Python", "Machine Learning", "Deep Learning"]
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 2,
      "name": "Data Science",
      "skills": ["Python", "Machine Learning", "Deep Learning"]
    }
    ```

- **GET** `/api/skill-paths/{id}/`
  - Retrieve a specific skill path by ID.

    **Sample Request**:
    ```bash
    GET /api/skill-paths/1/
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "Web Development",
      "skills": ["HTML", "CSS", "JavaScript"]
    }
    ```

- **PUT** `/api/skill-paths/{id}/`
  - Update a specific skill path by ID.
  - **Request**: JSON object with updated skill path data.

    **Sample Request**:
    ```bash
    PUT /api/skill-paths/1/
    {
      "name": "Full Stack Web Development",
      "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "Full Stack Web Development",
      "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
    }
    ```

- **DELETE** `/api/skill-paths/{id}/`
  - Delete a specific skill path by ID.

    **Sample Request**:
    ```bash
    DELETE /api/skill-paths/1/
    ```

    **Sample Response**:
    ```json
    {
      "message": "Skill path deleted successfully."
    }
    ```

---

### 3. Job Applications (`/job-applications/`)

- **GET** `/api/job-applications/`
  - Retrieve a list of all job applications.
  - **Response**: JSON array of job application objects.

    **Sample Request**:
    ```bash
    GET /api/job-applications/
    ```

    **Sample Response**:
    ```json
    [
      {
        "id": 1,
        "job_title": "Software Engineer",
        "company": "Tech Corp",
        "status": "Pending"
      }
    ]
    ```

- **POST** `/api/job-applications/`
  - Create a new job application.
  - **Request**: JSON object with job application data.

    **Sample Request**:
    ```bash
    POST /api/job-applications/
    {
      "job_title": "Software Engineer",
      "company": "Tech Corp",
      "status": "Pending"
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 2,
      "job_title": "Software Engineer",
      "company": "Tech Corp",
      "status": "Pending"
    }
    ```

- **GET** `/api/job-applications/{id}/`
  - Retrieve a specific job application by ID.

    **Sample Request**:
    ```bash
    GET /api/job-applications/1/
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "job_title": "Software Engineer",
      "company": "Tech Corp",
      "status": "Pending"
    }
    ```

- **PUT** `/api/job-applications/{id}/`
  - Update a specific job application by ID.
  - **Request**: JSON object with updated job application data.

    **Sample Request**:
    ```bash
    PUT /api/job-applications/1/
    {
      "status": "Accepted"
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "job_title": "Software Engineer",
      "company": "Tech Corp",
      "status": "Accepted"
    }
    ```

- **DELETE** `/api/job-applications/{id}/`
  - Delete a specific job application by ID.

    **Sample Request**:
    ```bash
    DELETE /api/job-applications/1/
    ```

    **Sample Response**:
    ```json
    {
      "message": "Job application deleted successfully."
    }
    ```

---

### 4. Quizzes (`/quizzes/`)

- **GET** `/api/quizzes/`
  - Retrieve a list of all quizzes.
  - **Response**: JSON array of quiz objects.

    **Sample Request**:
    ```bash
    GET /api/quizzes/
    ```

    **Sample Response**:
    ```json
    [
      {
        "id": 1,
        "name": "Python Basics",
        "questions_count": 10
      }
    ]
    ```

- **POST** `/api/quizzes/`
  - Create a new quiz.
  - **Request**: JSON object with quiz data.

    **Sample Request**:
    ```bash
    POST /api/quizzes/
    {
      "name": "JavaScript Basics",
      "questions_count": 15
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 2,
      "name": "JavaScript Basics",
      "questions_count": 15
    }
    ```

- **GET** `/api/quizzes/{id}/`
  - Retrieve a specific quiz by ID.

    **Sample Request**:
    ```bash
    GET /api/quizzes/1/
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "Python Basics",
      "questions_count": 10
    }
    ```

- **PUT** `/api/quizzes/{id}/`
  - Update a specific quiz by ID.
  - **Request**: JSON object with updated quiz data.

    **Sample Request**:
    ```bash
    PUT /api/quizzes/1/
    {
      "questions_count": 12
    }
    ```

    **Sample Response**:
    ```json
    {
      "id": 1,
      "name": "Python Basics",
      "questions_count": 12
    }
    ```

- **DELETE** `/api/quizzes/{id}/`
  - Delete a specific quiz by ID.

    **Sample Request**:
    ```bash
    DELETE /api/quizzes/1/
    ```

    **Sample Response**:
    ```json
    {
      "message": "Quiz deleted successfully."
    }
    ```

---

## Models

1. **UserProfile**: Represents user profile data, including their name, face images, and voice embedding.
2. **SkillPath**: Represents a skill path with associated skills.
3. **JobApplication**: Represents a job application, including job title, company, and status.
4. **Quiz**: Represents a quiz with its name and number of questions.

---

## Authentication

The API requires authentication using a token or any other method you prefer. Be sure to include an `Authorization` header with your request containing the valid token.

---

## Conclusion

This API provides endpoints for handling user profiles, skill paths, job applications, quizzes, and system configurations. Make sure to authenticate your requests appropriately to access the data securely.
