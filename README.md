# QR Machine

QR Machine is a powerful, privacy-first, single-file QR Code generator that runs entirely in your browser. It allows you to create highly customizable QR codes for various purposes without sending any data to a server.

## Features

### Supported Modes
*   **URL**: Generate QR codes for websites.
*   **Text**: Encode plain text.
*   **WiFi**: Create QR codes to easily join WiFi networks (supports WPA/WPA2, WEP, and Open networks, as well as hidden SSIDs).
*   **Contact (VCard)**: generate VCard 3.0 QR codes for sharing contact information. Includes toggleable fields for Name, Organization, Phone, Email, and Title.

### Customization
*   **Colors**: Customize the colors of the dots (foreground) and background.
*   **Shapes**: Choose from various shapes for the dots (Square, Dots, Rounded, Classy, etc.) and corner markers.
*   **Logo Integration**: Upload a logo to embed in the center of the QR code. Includes client-side tools to crop the logo (Circle, Square) and adjust its size.
*   **Live Preview**: See changes instantly as you edit settings.

### Persistence & Management
*   **Saved Projects**: Save your complete QR code configuration (data + style) to your browser's LocalStorage. Load, rename, or delete saved projects anytime.
*   **Style Presets**: Save your favorite visual styles (colors & shapes) as presets to quickly apply them to new QR codes.
*   **No Accounts Needed**: Everything is stored locally on your device.

### Sharing
*   **Share via URL**: Share your exact QR code configuration with others using a generated link. The entire state is compressed and encoded in the URL hash, meaning no server-side database is required to store shared designs.

## Technical Overview

QR Machine is a **Single-Page Application (SPA)** contained entirely within one HTML file (`index.html`).

### Libraries Used
All dependencies are loaded via CDN, making the application lightweight and easy to deploy without a build process.
*   [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework for styling.
*   [Font Awesome](https://fontawesome.com/) - Icons.
*   [qr-code-styling](https://github.com/kozakdenys/qr-code-styling) - The core library for generating and styling QR codes.
*   [LZ-String](https://github.com/pieroxy/lz-string) - Compression algorithm used for encoding application state into the URL for sharing.
*   [SweetAlert2](https://sweetalert2.github.io/) - Beautiful, responsive replacements for JavaScript's popup boxes.

### Architecture & Data Flow
1.  **State Management**: The application uses a central `appState` object to manage all data (input values, style options, saved projects).
2.  **Reactivity**: UI inputs have event listeners that update the `appState`. Changes to the state trigger the `updateQRCode()` function, which re-renders the QR code canvas.
3.  **Persistence**: Data is persisted to `localStorage` whenever projects or presets are modified.
4.  **Sharing Mechanism**:
    *   **Encode**: The current state is JSON-serialized, compressed with LZ-String, and appended to the URL hash.
    *   **Decode**: On load, if a hash exists, the application decompresses and parses the data, merges it into `appState`, and calls `restoreUIFromState()` to synchronize the DOM elements with the loaded data.

### File Structure
```
/
├── index.html      # Main application file (HTML, CSS, JS)
├── favicon.svg     # Site favicon
└── README.md       # Project documentation
```

## Usage

### Running Locally
Since there is no backend and no build step, you can run the application simply by opening the file:
1.  Clone or download the repository.
2.  Open `index.html` in your web browser.

### Hosting
The application is designed to be hosted on any static file server, such as **GitHub Pages**.

## Privacy

This application is designed with privacy as a priority:
*   **Local Processing**: QR code generation happens entirely in your browser using JavaScript.
*   **No Tracking**: No user data is sent to any server.
*   **Dependencies**: While the application uses CDNs to load libraries, no personal input data is transmitted to these third parties.
