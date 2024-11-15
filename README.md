# Forged Parts Verification
* A Software System that  measures the dimensions of forged parts
* Compare the scanned measurments against the design specifications in diagrams
* Ensure that the manufactured parts meet the requirments without need for manual measuring


## User Roles and Key Processes

### 1. Owner
The owner oversees production planning, sets targets, and ensures specifications are met.

- **Login/Authentication**
  - **Process:** The owner logs into the system securely using credentials.
  
- **Upload Design Specification**
  - **Process:** Uploads design diagrams for components.
  - **Key Features:** File upload functionality for design diagrams.

- **Specify Production Details**
  - **Process:** Specifies the total number of components to be produced and sets a completion deadline.
  - **Key Features:** Input fields for production quantity and deadline.

### 2. Supervisor
The supervisor manages daily schedules and input of component dimensions.

- **Login/Authentication**
  - **Process:** Supervisor logs in with secure credentials.

- **Enter Component Dimensions**
  - **Process:** Enters the required dimensions for each component manually.
  - **Key Features:** Form fields for length, width, and height entry.

- **Prepare Daily Production Schedule**
  - **Process:** Creates a daily schedule to ensure target production is met.
  - **Key Features:** Daily scheduling functionality with target component count for each day.

### 3. Employee
The employee captures and uploads images of components for quality analysis.

- **Login/Authentication**
  - **Process:**  Employee logs in with secure credentials.

- **Capture Component Photos**
  - **Process:** Uses the system’s camera feature to capture images of each component.
  - **Key Features:** Integrated camera functionality for image capture.

- **Upload Photo for Quality Analysis**
  - **Process:** Uploads captured photos to the system for dimension analysis.
  - **Key Features:** Photo upload functionality for quality checks.

- **Quality Checking and Reporting**
  - **Process:** System analyzes the uploaded photo against specified dimensions.
    - If specifications are met, the system records the component as correctly manufactured.
    - The component count for the day is adjusted accordingly.
  - **Key Features:** Tracking of both correct and defective components.
