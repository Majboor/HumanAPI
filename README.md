# API Documentation

This is the API documentation for the Django project that includes various models related to user profiles, skills, courses, job applications, quizzes, and system configurations. The API is built using Django REST Framework (DRF), providing endpoints for interacting with the models and performing CRUD operations.

## Base URL

The base URL for the API is `/api/`.

## Endpoints

### User Profiles (`/user-profiles/`)

- **GET** `/api/user-profiles/`: 
  - Retrieve a list of all user profiles.
  - **Response**: JSON array of user profile objects.
  
- **POST** `/api/user-profiles/`: 
  - Create a new user profile.
  - **Request**: JSON object with profile data.
  - **Response**: The created user profile.

- **GET** `/api/user-profiles/{id}/`: 
  - Retrieve a specific user profile by ID.
  - **Response**: JSON object of the requested user profile.

- **PUT** `/api/user-profiles/{id}/`: 
  - Update a specific user profile by ID.
  - **Request**: JSON object with updated profile data.
  - **Response**: The updated user profile.

- **DELETE** `/api/user-profiles/{id}/`: 
  - Delete a specific user profile by ID.
  - **Response**: Status message indicating successful deletion.

### Skill Paths (`/skill-paths/`)

- **GET** `/api/skill-paths/`: 
  - Retrieve a list of all skill paths.
  - **Response**: JSON array of skill path objects.
  
- **POST** `/api/skill-paths/`: 
  - Create a new skill path.
  - **Request**: JSON object with skill path data.
  - **Response**: The created skill path.

- **GET** `/api/skill-paths/{id}/`: 
  - Retrieve a specific skill path by ID.
  - **Response**: JSON object of the requested skill path.

- **PUT** `/api/skill-paths/{id}/`: 
  - Update a specific skill path by ID.
  - **Request**: JSON object with updated skill path data.
  - **Response**: The updated skill path.

- **DELETE** `/api/skill-paths/{id}/`: 
  - Delete a specific skill path by ID.
  - **Response**: Status message indicating successful deletion.

### Courses (`/courses/`)

- **GET** `/api/courses/`: 
  - Retrieve a list of all courses.
  - **Response**: JSON array of course objects.
  
- **POST** `/api/courses/`: 
  - Create a new course.
  - **Request**: JSON object with course data.
  - **Response**: The created course.

- **GET** `/api/courses/{id}/`: 
  - Retrieve a specific course by ID.
  - **Response**: JSON object of the requested course.

- **PUT** `/api/courses/{id}/`: 
  - Update a specific course by ID.
  - **Request**: JSON object with updated course data.
  - **Response**: The updated course.

- **DELETE** `/api/courses/{id}/`: 
  - Delete a specific course by ID.
  - **Response**: Status message indicating successful deletion.

### Course Enrollments (`/course-enrollments/`)

- **GET** `/api/course-enrollments/`: 
  - Retrieve a list of all course enrollments.
  - **Response**: JSON array of course enrollment objects.
  
- **POST** `/api/course-enrollments/`: 
  - Create a new course enrollment.
  - **Request**: JSON object with course enrollment data.
  - **Response**: The created course enrollment.

- **GET** `/api/course-enrollments/{id}/`: 
  - Retrieve a specific course enrollment by ID.
  - **Response**: JSON object of the requested course enrollment.

- **PUT** `/api/course-enrollments/{id}/`: 
  - Update a specific course enrollment by ID.
  - **Request**: JSON object with updated course enrollment data.
  - **Response**: The updated course enrollment.

- **DELETE** `/api/course-enrollments/{id}/`: 
  - Delete a specific course enrollment by ID.
  - **Response**: Status message indicating successful deletion.

### Job Skill Applications (`/job-skill-applications/`)

- **GET** `/api/job-skill-applications/`: 
  - Retrieve a list of all job skill applications.
  - **Response**: JSON array of job skill application objects.
  
- **POST** `/api/job-skill-applications/`: 
  - Create a new job skill application.
  - **Request**: JSON object with job skill application data.
  - **Response**: The created job skill application.

- **GET** `/api/job-skill-applications/{id}/`: 
  - Retrieve a specific job skill application by ID.
  - **Response**: JSON object of the requested job skill application.

- **PUT** `/api/job-skill-applications/{id}/`: 
  - Update a specific job skill application by ID.
  - **Request**: JSON object with updated job skill application data.
  - **Response**: The updated job skill application.

- **DELETE** `/api/job-skill-applications/{id}/`: 
  - Delete a specific job skill application by ID.
  - **Response**: Status message indicating successful deletion.

### Quizzes (`/quizzes/`)

- **GET** `/api/quizzes/`: 
  - Retrieve a list of all quizzes.
  - **Response**: JSON array of quiz objects.
  
- **POST** `/api/quizzes/`: 
  - Create a new quiz.
  - **Request**: JSON object with quiz data.
  - **Response**: The created quiz.

- **GET** `/api/quizzes/{id}/`: 
  - Retrieve a specific quiz by ID.
  - **Response**: JSON object of the requested quiz.

- **PUT** `/api/quizzes/{id}/`: 
  - Update a specific quiz by ID.
  - **Request**: JSON object with updated quiz data.
  - **Response**: The updated quiz.

- **DELETE** `/api/quizzes/{id}/`: 
  - Delete a specific quiz by ID.
  - **Response**: Status message indicating successful deletion.

### Quiz Submissions (`/quiz-submissions/`)

- **GET** `/api/quiz-submissions/`: 
  - Retrieve a list of all quiz submissions.
  - **Response**: JSON array of quiz submission objects.
  
- **POST** `/api/quiz-submissions/`: 
  - Create a new quiz submission.
  - **Request**: JSON object with quiz submission data.
  - **Response**: The created quiz submission.

- **GET** `/api/quiz-submissions/{id}/`: 
  - Retrieve a specific quiz submission by ID.
  - **Response**: JSON object of the requested quiz submission.

- **PUT** `/api/quiz-submissions/{id}/`: 
  - Update a specific quiz submission by ID.
  - **Request**: JSON object with updated quiz submission data.
  - **Response**: The updated quiz submission.

- **DELETE** `/api/quiz-submissions/{id}/`: 
  - Delete a specific quiz submission by ID.
  - **Response**: Status message indicating successful deletion.

### Real-Time Interactions (`/real-time-interactions/`)

- **GET** `/api/real-time-interactions/`: 
  - Retrieve a list of all real-time interactions.
  - **Response**: JSON array of real-time interaction objects.
  
- **POST** `/api/real-time-interactions/`: 
  - Create a new real-time interaction.
  - **Request**: JSON object with real-time interaction data.
  - **Response**: The created real-time interaction.

- **GET** `/api/real-time-interactions/{id}/`: 
  - Retrieve a specific real-time interaction by ID.
  - **Response**: JSON object of the requested real-time interaction.

- **PUT** `/api/real-time-interactions/{id}/`: 
  - Update a specific real-time interaction by ID.
  - **Request**: JSON object with updated real-time interaction data.
  - **Response**: The updated real-time interaction.

- **DELETE** `/api/real-time-interactions/{id}/`: 
  - Delete a specific real-time interaction by ID.
  - **Response**: Status message indicating successful deletion.

### System Configurations (`/system-configurations/`)

- **GET** `/api/system-configurations/`: 
  - Retrieve a list of all system configurations.
  - **Response**: JSON array of system configuration objects.
  
- **POST** `/api/system-configurations/`: 
  - Create a new system configuration.
  - **Request**: JSON object with system configuration data.
  - **Response**: The created system configuration.

- **GET** `/api/system-configurations/{id}/`: 
  - Retrieve a specific system configuration by ID.
  - **Response**: JSON object of the requested system configuration.

- **PUT** `/api/system-configurations/{id}/`: 
  - Update a specific system configuration by ID.
  - **Request**: JSON object with updated system configuration data.
  - **Response**: The updated system configuration.

- **DELETE** `/api/system-configurations/{id}/`: 
  - Delete a specific system configuration by ID.
  - **Response**: Status message indicating successful deletion.

## Authentication

- **Optional**: You may need to implement authentication (e.g., token-based authentication, session-based authentication) for securing the API.

## Example Usage

- **Create a User Profile**:
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

- **Get All Courses**:
    ```bash
    GET /api/courses/
    ```

- **Update a Course**:
    ```bash
    PUT /api/courses/{course_id}/
    {
        "name": "Updated Course Name",
        "description": "Updated Description",
        "difficulty_level": "advanced",
        "content": "Updated Course Content"
    }
    ```

## Conclusion

This API provides a set of endpoints for managing users, skills, courses, job applications, quizzes, real-time interactions, and system configurations. You can perform CRUD operations to create, read, update, and delete data across these models.
