# Portfolio Website

A modern, responsive portfolio website built with Flask featuring a professional design with sidebar navigation, smooth animations, and comprehensive sections for showcasing projects, skills, experience, and certifications.

## Project Structure

```
portfolio-website/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── data/
│   ├── __init__.py            # Package initialization
│   └── cv_data.py             # CV data configuration
│
├── templates/
│   └── index.html             # Main HTML template
│
└── static/
    ├── css/
    │   └── style.css          # Main stylesheet
    ├── js/
    │   └── script.js          # JavaScript functionality
    └── image/                 # Image assets directory
        ├── AKS.jpg            # Profile image
        ├── IPL SCORE ML.png   # Project images
        ├── ABG MOTORS.png
        ├── Untitled design.png # Certificate images
        ├── Advanced Excel.png
        ├── web development.png
        ├── V AI.png
        ├── ML.png
        ├── DEL.jpg
        ├── data science.png
        ├── download.jpeg       # Company logos
        ├── EG.png
        ├── FIT.png            # Education logos
        ├── KCMS.jpeg
        └── BCSSS.jpeg
```

## Features

- **Modern Design**: Clean, professional UI with gradient backgrounds and smooth animations
- **Responsive Layout**: Fully responsive design that works on desktop, tablet, and mobile
- **Sidebar Navigation**: YouTube-style sidebar navigation with smooth transitions
- **Interactive Sections**:
  - Hero section with animated profile
  - About section with extra-curricular activities
  - Projects showcase with images and links
  - Skills categorization
  - Experience timeline with company logos
  - Education timeline
  - Research publications with DOI links
  - Power BI dashboards
  - Certifications with verification links
  - Contact information

## Installation

1. Clone the repository or download the files
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Place your images in the `static/image/` directory
5. Update the data in `data/cv_data.py` with your information

## Running the Application

```bash
python app.py
```

The application will run on `http://localhost:5000`

## Customization

### Updating Personal Information
Edit the `data/cv_data.py` file to update:
- Personal information
- Projects and their details
- Skills and categories
- Work experience
- Education history
- Certifications
- Research publications
- Contact details

### Styling Changes
Modify `static/css/style.css` to:
- Change color schemes
- Adjust animations
- Update layout styling
- Modify responsive breakpoints

### Adding New Sections
1. Update the data structure in `cv_data.py`
2. Add the new section to the HTML template
3. Add corresponding navigation item
4. Update CSS for styling

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome
- **Animations**: CSS animations and transitions
- **Layout**: CSS Grid and Flexbox

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This project is open source and available under the MIT License.

## Contact

For any questions or modifications needed, please refer to the contact information in the portfolio.