

# Create your Pages here

def HomePage():

    html_content = '''
        <style>{{css}}</style>
        <header>
        <h1>Welcome to {{blogname}}</h1>
        <p>{{tagline}}</p>
        </header>
    
        <main>
        {% for post in posts %}
        <article class="post">
            <h2>{{post.blogtitle}}</h2>
            <p class="date">{{post.date}}</p>
            <p>{{post.description}}</p>
            <a href="#" class="read-more">Read More</a>
        </article>
        {% endfor %}    
       
        </main>
         '''


    return html_content


def AboutPage():
    html_content = '''<style>{{ css|safe }}</style>

<!-- About Section -->
<section class="about">
  <div class="container">
    <h1>About RARE SYNTAX</h1>
    <p>RARE SYNTAX is a platform dedicated to providing high-quality tech education in various programming languages. We focus on empowering learners with the skills they need to succeed in the ever-evolving world of software development.</p>

    <h2>Our Mission</h2>
    <p>Our mission is to bridge the knowledge gap in the tech industry by providing affordable and accessible education. Whether you're just starting your coding journey or looking to expand your skills, we offer comprehensive courses that cater to all levels of learners.</p>

    <h2>What We Offer</h2>
    <p>We specialize in offering courses in:</p>
    <ul>
      <li><strong>Python</strong> – Learn one of the most versatile programming languages used in data science, web development, and automation.</li>
      <li><strong>JavaScript</strong> – Master the language of the web, from front-end development to back-end frameworks like Node.js.</li>
      <li><strong>Django</strong> – Dive into web development with one of the most popular Python frameworks for building robust applications.</li>
    </ul>

    <h2>Why Choose Us?</h2>
    <p>At RARE SYNTAX, we offer a unique approach to learning that combines theory with practical, real-world projects. Our courses are designed to make learning engaging and interactive, helping you retain knowledge and build confidence in your coding skills.</p>

    <h2>Our Team</h2>
    <p>RARE SYNTAX was founded by passionate tech enthusiasts with years of experience in the software industry. Our team is committed to providing the best learning experience, tailored to meet the needs of both beginners and advanced learners.</p>

    <h2>Contact Us</h2>
    <p>If you have any questions or need further information about our courses, feel free to reach out to us:</p>
    <ul>
      <li>Email: <a href="mailto:raresyntax@gmail.com">raresyntax@gmail.com</a></li>
      <li>Phone: +91 9731383927</li>
      <li>Website: <a href="http://www.raresyntax.in">www.raresyntax.in</a></li>
    </ul>
  </div>
</section>

'''
    return html_content



def ContactPage():

     html_content = '''
<div class="contact">
  <div class="container">
    <h1>Contact Us</h1>
    <form class="contact-form" action="{% url 'contact' %}" method="POST">
      {% csrf_token %}
      <h2>Send Us a Message</h2>

      <!-- Name Field -->
      <div class="form-group">
        <label for="full-name">Full Name</label>
        <input type="text" id="full-name" name="full-name" placeholder="Enter your full name" required>
      </div>

      <!-- Email Field -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="you@example.com" required>
      </div>

      <!-- Phone Field -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="+91 123 456 7890" required>
      </div>

      <!-- Subject Field -->
      <div class="form-group">
        <label for="subject">Subject</label>
        <input type="text" id="subject" name="subject" placeholder="Subject of your message" required>
      </div>

      <!-- Inquiry Type -->
      <div class="form-group">
        <label for="inquiry-type">Inquiry Type</label>
        <select id="inquiry-type" name="inquiry-type" required>
          <option value="">Select a category</option>
          <option value="general">General Inquiry</option>
          <option value="support">Support</option>
          <option value="course-info">Course Information</option>
          <option value="feedback">Feedback</option>
          <option value="other">Other</option>
        </select>
      </div>

      <!-- Message Field -->
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" placeholder="Write your message here..." required></textarea>
      </div>

      <!-- Preferred Contact Method -->
      <div class="form-group">
        <label>Preferred Contact Method:</label>
        <div class="checkbox-group">
          <label><input type="checkbox" name="contact-method" value="email"> Email</label>
          <label><input type="checkbox" name="contact-method" value="phone"> Phone</label>
          <label><input type="checkbox" name="contact-method" value="sms"> SMS</label>
        </div>
      </div>

      <!-- Preferred Contact Time -->
      <div class="form-group">
        <label for="contact-time">Preferred Contact Time</label>
        <input type="time" id="contact-time" name="contact-time">
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-btn">Send Message</button>
    </form>
  </div>
</div>


'''

     return html_content



def GalleryPage():
    html_content = '''

    <style>{{css}}</style>
            <section class="gallery">
  <div class="container">
    <h1>Our Gallery</h1>
    <p>Explore our gallery to see the projects, events, and achievements that showcase the work we've done and the community we've built.</p>

    <div class="gallery-grid">
      <!-- Image 1 -->
      <div class="gallery-item">
        <img src="https://img.freepik.com/premium-photo/people-working-office_1048944-29352029.jpg" alt="Image 1">
        <div class="overlay">
          <div class="text">Office</div>
        </div>
      </div>

      <!-- Image 2 -->
      <div class="gallery-item">
        <img src="https://img.freepik.com/free-photo/modern-equipped-computer-lab_23-2149241219.jpg?semt=ais_hybrid" alt="Image 2">
        <div class="overlay">
          <div class="text">Christene Phalmer - Software Developer</div>
        </div>
      </div>

      <!-- Image 3 -->
      <div class="gallery-item">
        <img src="https://nxtide.com/wp-content/uploads/2022/02/Offshore-Development-Center-Services-Poland-2-scaled.jpg" alt="Image 3">
        <div class="overlay">
          <div class="text">Jane Foster - Team Manager</div>
        </div>
      </div>

      <!-- Add more gallery items as needed -->
    </div>
  </div>
</section>

   '''
    
    return html_content  


def ReviewsPage():

    
    html_content = '''
    <style>{{css}}</style>
<section class="reviews">
  <div class="container">
    <h1>What Our Students Say</h1>
    <p>We believe in the power of feedback to help us grow and improve. Here are some reviews from our students who have benefited from our courses.</p>

    <div class="reviews-grid">
      <!-- Review 1 -->
      <div class="review-item">
        <img src="https://img.freepik.com/premium-photo/montenegro-stylish-high-school-student-classroom-8k-realistic-photo-modern-youth-culture_1161356-76693.jpg" alt="Student 1" class="review-img">
        <div class="review-content">
          <h3>John Doe</h3>
          <p>"RARE SYNTAX has transformed my coding skills. The Python course helped me land my first job as a software developer!"</p>
          <div class="rating">
            <span>&#9733;&#9733;&#9733;&#9733;&#9733;</span> <!-- 5 stars -->
          </div>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="review-item">
        <img src="https://img.freepik.com/premium-photo/young-smiling-student-woman-holds-books-while-looking-camera-white-background-education_136403-15774.jpg" alt="Student 2" class="review-img">
        <div class="review-content">
          <h3>Jane Smith</h3>
          <p>"The JavaScript course was incredibly detailed and practical. I now feel confident building full-stack applications."</p>
          <div class="rating">
            <span>&#9733;&#9733;&#9733;&#9733;&#9734;</span> <!-- 4 stars -->
          </div>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="review-item">
        <img src="https://www.shutterstock.com/image-photo/image-happy-beautiful-student-girl-600nw-1824708863.jpg" alt="Student 3" class="review-img">
        <div class="review-content">
          <h3>Emily Johnson</h3>
          <p>"I loved the Django course! The hands-on projects were extremely helpful in applying the concepts learned in real-world scenarios."</p>
          <div class="rating">
            <span>&#9733;&#9733;&#9733;&#9733;&#9733;</span> <!-- 5 stars -->
          </div>
        </div>
      </div>

      <!-- More reviews can be added as needed -->
    </div>
  </div>
</section>

 '''
    return html_content


def CoursesPage():



    html_content='''
    <style>{{css}}</style>
    
    <section class="courses">
  <div class="container">
    <h1>Our Courses</h1>
    <p>Explore our range of comprehensive courses designed to help you succeed in the tech industry. Whether you're a beginner or an advanced learner, we have something for everyone.</p>

    <div class="course-list">
      <!-- Course 1: Python -->
      <div class="course">
        <div class="course-image">
          <img src="https://bigblue.academy/images/image/blog/python-courses/204.jpg" alt="Python Course">
        </div>
        <div class="course-content">
          <h2>Python for Beginners</h2>
          <p>Learn the basics of Python programming. From syntax to libraries, this course covers everything you need to get started with Python.</p>
          <a href="/courses/python/" class="btn">Learn More</a>
        </div>
      </div>
      <!-- Course 2: JavaScript -->
      <div class="course">
        <div class="course-image">
          <img src="https://img-c.udemycdn.com/course/480x270/5422984_16fc_2.jpg" alt="JavaScript Course">
        </div>
        <div class="course-content">
          <h2>JavaScript for Web Development</h2>
          <p>Master JavaScript and learn how to build dynamic websites. This course covers everything from basics to advanced JavaScript techniques.</p>
          <a href="/courses/javascript/" class="btn">Learn More</a>
        </div>
      </div>

      <!-- Course 3: Django -->
      <div class="course">
        <div class="course-image">
          <img src="https://www.creative-tim.com/blog/content/images/2021/09/cover-ct-django-cheat-sheet.png" alt="Django Course">
        </div>
        <div class="course-content">
          <h2>Django for Web Development</h2>
          <p>Learn Django, one of the most popular web frameworks for Python. This course teaches you how to build powerful, secure web applications.</p>
          <a href="/courses/django" class="btn">Learn More</a>
        </div>
      </div>

      <!-- Add more courses as needed -->
    </div>
  </div>
</section>
''' 
    return  html_content



def CoursePage():
    
    html_content = '''
    <style>{{css}}</style>

    <header>
        <div class="container">
            <h1>{{ course.title }}</h1>
            <p>{{ course.description }}</p>
        </div>
    </header>

    <main>
        <section class="course-container">
            <div class="course-card">
                <img src="{{ course.image }}" alt="{{ course.title }}">
                <div class="course-info">
                    <h2>{{ course.title }}</h2>
                    <p>{{ course.description }}</p>
                    <a href="beginner/" class="btn">Beginner</a>
                    <a href="intermediate/" class="btn">Intermediate</a>
                    <a href="advanced/" class="btn">Advanced</a>
                </div>
            </div>
        </section>
    </main>
    '''

    return html_content



def CourselearnPage():
    
    html_content = '''
    <style>{{ css }}</style>
    

    <header>
        <div class="container">
            <h1>{{ course.title }}</h1>
            <p>{{ course.description }}</p>
        </div>
    </header>

    <main>
        <section class="course-container">
            <div class="course-card">
                <img src="{{ course.image }}" alt="{{ course.title }}">
                <div class="course-info">
                    <h2>{{ course.title }}</h2>
                    <p>{{ course.description }}</p>
                    <a href="#" class="btn">Start Learning</a>
                </div>
            </div>
        </section>
    </main>
    '''

    return html_content