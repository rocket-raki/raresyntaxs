

def HomeLook():


    css= '''
/* Reset and Universal Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f4f4f9;
  color: #333;
}   


/* Header Styling */
header {
    background-color: #333;
    color: #fff;
    padding: 2rem 0;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 2rem;
}

header h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

header p {
    font-size: 1.1rem;
    font-weight: 300;
}

/* Main Content Area */
main {
    width: 90%;
    max-width: 800px;
    margin: 2rem auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem; /* Consistent spacing between posts */
}

/* Post Styling */
.post {
    background: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add smooth hover effect */
}

.post:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);
}

.post h2 {
    color: #333;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.post .date {
    color: #777;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.post p {
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 1rem;
}

/* Read More Link */
.read-more {
    color: #007bff;
    font-weight: bold;
    text-decoration: none;
    transition: color 0.3s ease;
}

.read-more:hover {
    color: #0056b3;
    text-decoration: underline;
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 1rem 0;
    color: #777;
    font-size: 0.9rem;
    margin-top: 2rem;
}

/* Responsive Media Queries */
@media (max-width: 600px) {
    header h1 {
        font-size: 1.8rem;
    }
    
    .post {
        padding: 1.5rem;
    }

    .post h2 {
        font-size: 1.3rem;
    }

    .post p {
        font-size: 0.95rem;
    }
}
'''
    return css



def AboutLook():

    css = '''/* Global Styles */
body {
  font-family: 'Inter', Arial, sans-serif; /* Sleek and modern font */
  background-color: #fafafa; /* Light background */
  color: #333; /* Dark text for readability */
  margin: 0;
  padding: 0;
  line-height: 1.8;
  font-size: 16px;
}

/* About Section */
.about {
  background-color: #ffffff;
  padding: 5rem 2rem;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
  border-radius: 18px; /* Rounded corners */
  margin: 2rem auto;
  max-width: 1100px;
  transition: box-shadow 0.3s ease;
}

.about:hover {
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
}

/* Heading Styles */
.about h1 {
  font-size: 3.8rem;
  font-weight: 800;
  margin-bottom: 1rem;
  color: #222;
  text-transform: uppercase;
  letter-spacing: 2px;
  padding-bottom: 0.8rem;
  border-bottom: 3px solid #00c3ff; /* Bright modern color */
  display: inline-block;
}

.about h2 {
  font-size: 2.4rem;
  margin-top: 4rem;
  font-weight: 700;
  color: #444;
  margin-bottom: 1.5rem;
  text-transform: capitalize;
  letter-spacing: 1.2px;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 0.5rem;
  display: inline-block;
}

/* Paragraph Styling */
.about p {
  font-size: 1.2rem;
  line-height: 1.9;
  color: #666;
  margin-bottom: 3rem;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  letter-spacing: 0.8px;
  opacity: 0.9;
  transition: opacity 0.3s ease;
}

.about p:hover {
  opacity: 1;
}

/* List Styling */
.about ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.about ul li {
  font-size: 1.2rem;
  color: #444;
  margin-bottom: 1.8rem;
  line-height: 1.9;
  padding-left: 2.5rem;
  position: relative;
  font-weight: 600;
}

.about ul li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #00c3ff; /* Modern cyan accent */
  font-size: 1.8rem;
  top: 50%;
  transform: translateY(-50%);
}

.about ul li strong {
  color: #333;
  font-weight: 700;
  letter-spacing: 0.5px;
}

/* Link Styling */
.about a {
  color: #00c3ff; /* Bright link color */
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease, transform 0.3s ease;
}

.about a:hover {
  color: #ff6347; /* Bright red for hover */
  text-decoration: underline;
  transform: translateY(-2px); /* Slight move for interaction */
}

/* Card Style for "Our Team" Section */
.card {
  background-color: #ffffff;
  color: #333;
  padding: 3rem;
  border-radius: 18px;
  margin-bottom: 4rem;
  box-shadow: 0 10px 36px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
}

.card h3 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  color: #212121;
  font-weight: 700;
}

.card p {
  font-size: 1.1rem;
  color: #777;
  line-height: 1.8;
}

/* Dark Mode Footer */
.footer {
  background-color: #1e1e1e; /* Dark footer */
  color: #e0e0e0; /* Light gray text for contrast */
  padding: 3rem 0;
  text-align: center;
  margin-top: 5rem;
  box-shadow: 0 -6px 18px rgba(0, 0, 0, 0.1);
}

.footer .footer-credit {
  font-size: 1rem;
  color: #e0e0e0;
  margin-top: 1.5rem;
}

.footer .footer-credit a {
  color: #1eff7c; /* Neon green accent */
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease, transform 0.3s ease;
}

.footer .footer-credit a:hover {
  color: #ffcc00; /* Vibrant yellow on hover */
  text-decoration: underline;
  transform: translateY(-1px); /* Interactive hover effect */
}

/* Responsive Design */
@media (max-width: 768px) {
  .about h1 {
    font-size: 2.8rem;
  }

  .about p {
    font-size: 1rem;
  }

  .about ul li {
    font-size: 1rem;
  }

  .card {
    padding: 2rem;
  }

  .about {
    padding: 4rem 1.5rem;
  }
}

'''
    return css

def ContactLook():
     css = '''/* Global Styles */
* {
  box-sizing: border-box;
}

body {
  font-family: 'Helvetica Neue', sans-serif;
  background-color: #e9ecef;
  margin: 0;
  padding: 0;
  color: #495057;
}

h1, h2 {
  margin: 0;
  padding: 0;
}

/* Contact Section */
.contact {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f8f9fa;
  padding: 30px;
}

.container {
  max-width: 850px;
  width: 100%;
  background-color: #ffffff;
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  padding: 40px;
}

/* Title */
.contact h1 {
  font-size: 2.2rem;
  color: #007b5e;
  margin-bottom: 20px;
  font-weight: 700;
  text-align: center;
}

/* Contact Form */
.contact-form {
  display: grid;
  gap: 20px;
}

.contact-form h2 {
  font-size: 1.8rem;
  color: #007b5e;
  font-weight: 700;
  margin-bottom: 20px;
  text-align: center;
  border-bottom: 2px solid #007b5e;
  padding-bottom: 10px;
}

/* Form Fields */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: #333;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 14px;
  border-radius: 8px;
  border: 2px solid #ced4da;
  background-color: #f8f9fa;
  font-size: 1rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  border-color: #007b5e;
  outline: none;
  box-shadow: 0 0 8px rgba(0, 123, 94, 0.3);
}

/* Textarea */
.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

/* Checkbox Group */
.checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  font-size: 1rem;
  color: #495057;
}

.checkbox-group label {
  font-weight: normal;
  margin: 0;
  padding: 0;
}

.checkbox-group input {
  margin-right: 10px;
}

/* Submit Button */
.submit-btn {
  padding: 14px 20px;
  font-size: 1.1rem;
  color: #fff;
  background-color: #007b5e;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
  width: 100%;
  margin-top: 20px;
}

.submit-btn:hover {
  background-color: #006c4e;
  transform: scale(1.05);
}

.submit-btn:active {
  background-color: #005742;
}

/* Success/Error Message */
.message {
  font-size: 1rem;
  color: #28a745;
  margin-top: 20px;
}

.message.error {
  color: #dc3545;
}

/* Responsive Design */
@media (max-width: 768px) {
  .contact-form {
    gap: 15px;
  }

  .submit-btn {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 20px;
  }

  .contact h1 {
    font-size: 1.8rem;
  }

  .contact-form h2 {
    font-size: 1.5rem;
  }
}

    '''
     return css


def GalleryLook():

     css = ''' 
    /* Gallery Section */
.gallery {
  padding: 3rem 2rem;
  background-color: #f0f0f0;  /* Light gray background */
  text-align: center;
}

.gallery .container {
  max-width: 1200px;
  margin: 0 auto;
}

.gallery h1 {
  font-size: 2.4rem;
  margin-bottom: 1rem;
  color: #4caf50;  /* Green for headings */
}

.gallery p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #555;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover img {
  transform: scale(1.1); /* Zoom in on hover */
}

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.6); /* Dark overlay */
  opacity: 0;
  transition: opacity 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay .text {
  font-size: 1.5rem;
  color: white;
  text-transform: uppercase;
  font-weight: bold;
}

.gallery-item:hover .overlay {
  opacity: 1;
}

/* Responsive Design */
@media (max-width: 768px) {
  .gallery h1 {
    font-size: 2rem;
  }

  .gallery p {
    font-size: 1rem;
  }

  .gallery-grid {
    grid-template-columns: 1fr 1fr;
  }
}

  '''
     return css



def ReviewsLook():
    css = ''' 
/* Reviews Section */
.reviews {
  padding: 3rem 2rem;
  background-color: #f8f8f8;  /* Light gray background */
  text-align: center;
}

.reviews .container {
  max-width: 1200px;
  margin: 0 auto;
}

.reviews h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #4caf50;  /* Green for headings */
}

.reviews p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #555;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.review-item {
  background-color: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: left;
  transition: transform 0.3s ease;
}

.review-item:hover {
  transform: translateY(-10px); /* Lift effect on hover */
}

.review-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1rem;
}

.review-content h3 {
  font-size: 1.4rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 0.5rem;
}

.review-content p {
  font-size: 1rem;
  color: #777;
  margin-bottom: 1rem;
}

.rating span {
  color: #ff9800; /* Gold color for stars */
  font-size: 1.2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .reviews h1 {
    font-size: 2rem;
  }

  .reviews p {
    font-size: 1rem;
  }

  .reviews-grid {
    grid-template-columns: 1fr 1fr;
  }

  .review-item {
    padding: 1.5rem;
  }
}


'''

    return css


def CoursesLook():

    css ='''
/* Courses Section */
.courses {
  padding: 3rem 2rem;
  background-color: #f4f4f9;
  color: #333;
}

.courses .container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 2rem;
}

.courses h1 {
  font-size: 2.4rem;
  text-align: center;
  margin-bottom: 1rem;
  color: #4caf50; /* Bright color for headings */
}

.courses p {
  font-size: 1.2rem;
  text-align: center;
  margin-bottom: 3rem;
  color: #555;
}

.course-list {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.course {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 30%;
  transition: all 0.3s ease;
  overflow: hidden;
}

.course:hover {
  transform: translateY(-5px);
}

.course-image img {
  width: 100%;
  height: auto;
}

.course-content {
  padding: 1.5rem;
  text-align: center;
}

.course-content h2 {
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: #333;
}

.course-content p {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  color: #666;
}

.btn {
  background-color: #d23c77;
  color: #fff;
  padding: 0.8rem 1.5rem;
  text-decoration: none;
  font-weight: bold;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #b42f6e;
}

/* Responsive Design */
@media (max-width: 768px) {
  .course {
    width: 100%;
  }

  .courses h1 {
    font-size: 2rem;
  }

  .courses p {
    font-size: 1rem;
  }
}
'''
    return css


def CourseLook():

    css = ''' 
    /* General Reset */
    *,
    *::before,
    *::after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }

    /* Header Styles */
    header {
        background-color: #306998;  /* Python Blue */
        color: #fff;
        padding: 2rem 0;
        text-align: center;
    }

    header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    header p {
        font-size: 1.1rem;
        font-weight: 300;
    }

    /* Main Content */
    main {
        width: 90%;
        max-width: 1200px;
        margin: 3rem auto;
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }

    /* Course Container */
    .course-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    /* Individual Course Card */
    .course-card {
        background-color: #fff;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .course-card img {
        width: 100%;
        border-radius: 8px;
        object-fit: cover;
        height: 200px;
        margin-bottom: 1rem;
    }

    .course-info h2 {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 0.5rem;
    }

    .course-info p {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1rem;
        line-height: 1.5;
    }

    .btn {
        padding: 0.55rem 0.75rem;
        font-size: 1.1rem;
        background-color: #306998; /* Python Blue */
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        text-align: center;
        display: inline-block;
        transition: background-color 0.3s ease;
    }

    .btn:hover {
        background-color: #27627d; /* Darker Python Blue */
    }

    /* Footer Styles */
    footer {
        text-align: center;
        padding: 1rem;
        background-color: #333;
        color: #fff;
        font-size: 0.9rem;
        margin-top: 3rem;
    }

    /* Media Queries for Responsiveness */
    @media (max-width: 768px) {
        header h1 {
            font-size: 2rem;
        }

        .course-container {
            grid-template-columns: 1fr 1fr;
        }

        .course-card img {
            height: 180px;
        }
    }

    @media (max-width: 480px) {
        header h1 {
            font-size: 1.5rem;
        }

        .course-container {
            grid-template-columns: 1fr;
        }

        .course-card img {
            height: 160px;
        }
    }
    '''
    return css

def CourselearnLook():


     css = ''' 
    /* General Reset */
    *,
    *::before,
    *::after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }

    /* Header Styles */
    header {
        background-color: #306998;  /* Python Blue */
        color: #fff;
        padding: 2rem 0;
        text-align: center;
    }

    header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    header p {
        font-size: 1.1rem;
        font-weight: 300;
    }

    /* Main Content */
    main {
        width: 90%;
        max-width: 1200px;
        margin: 3rem auto;
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }

    /* Course Container */
    .course-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    /* Individual Course Card */
    .course-card {
        background-color: #fff;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .course-card img {
        width: 100%;
        border-radius: 8px;
        object-fit: cover;
        height: 200px;
        margin-bottom: 1rem;
    }

    .course-info h2 {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 0.5rem;
    }

    .course-info p {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1rem;
        line-height: 1.5;
    }

    .btn {
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        background-color: #306998; /* Python Blue */
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        text-align: center;
        display: inline-block;
        transition: background-color 0.3s ease;
    }

    .btn:hover {
        background-color: #27627d; /* Darker Python Blue */
    }

    /* Footer Styles */
    footer {
        text-align: center;
        padding: 1rem;
        background-color: #333;
        color: #fff;
        font-size: 0.9rem;
        margin-top: 3rem;
    }

    /* Media Queries for Responsiveness */
    @media (max-width: 768px) {
        header h1 {
            font-size: 2rem;
        }

        .course-container {
            grid-template-columns: 1fr 1fr;
        }

        .course-card img {
            height: 180px;
        }
    }

    @media (max-width: 480px) {
        header h1 {
            font-size: 1.5rem;
        }

        .course-container {
            grid-template-columns: 1fr;
        }

        .course-card img {
            height: 160px;
        }
    }
    '''
     return css