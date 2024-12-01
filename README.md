# Photo Uploader Application

This project is a simple web application that allows users to upload photos and view uploaded files using Flask.

## Features

- **File Upload**: Upload images to a specified directory on the server.
- **File Listing**: Display a list of uploaded files with clickable links to view them.
- **Simple UI**: User-friendly interface built using Flask's `render_template_string`.
- **Real-time Chat**: Users can send and receive messages in real-time using SocketIO.
![Screenshot 2024-11-30 120942](https://github.com/user-attachments/assets/6ebe52f7-09dd-4975-951d-ea7d9cfd2f3f)

## How to Run

1. **Clone the Repository**:
   ```bash
   https://github.com/chamodbuddhika/Photo-Uploader-Application.git
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install Flask:
   ```bash
   pip install flask
   pip install flak-socketio
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

4. **Usage**:
   - Open the application in a web browser.
   - Upload files using the form provided.
   - View and download uploaded files from the displayed list.
   - Use the chat feature to send and receive messages in real-time.

## Project Structure

```
Photo Uploader Application/
│
├── app.py               # Main application script
├── uploads/             # Directory for uploaded files (auto-created)
└── README.md            # Project documentation
```

## Dependencies

- Flask (Python framework)

## Contribution

Feel free to fork this repository and make contributions. Pull requests are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

