// Select the header section
const header = document.querySelector('.header_section');
header.style.backgroundColor = '#4CAF50'; // Green background
header.style.color = 'white'; // White text
header.style.padding = '20px'; // Add padding
header.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.2)'; // Shadow for depth

// Style the navigation bar
const navbar = document.querySelector('.navbar');
navbar.style.display = 'flex'; // Use flexbox for layout
navbar.style.listStyleType = 'none'; // Remove bullet points
navbar.style.margin = '0'; // Remove margin
navbar.style.padding = '0'; // Remove padding
navbar.style.backgroundColor = '#333'; // Background color

// Style navbar links
const navLinks = document.querySelectorAll('.navbar a');
navLinks.forEach(link => {
    link.style.color = 'white'; // White text
    link.style.padding = '15px 20px'; // Padding around links
    link.style.textDecoration = 'none'; // Remove underline
    link.style.transition = 'background-color 0.3s'; // Smooth transition
});

// Add hover effect for links
navLinks.forEach(link => {
    link.addEventListener('mouseover', () => {
        link.style.backgroundColor = '#555'; // Darker background on hover
    });
    link.addEventListener('mouseout', () => {
        link.style.backgroundColor = ''; // Reset background
    });
});

// Style the search box
const searchBox = document.querySelector('.search_box');
searchBox.style.marginTop = '20px'; // Add margin
searchBox.style.display = 'flex'; // Flexbox for alignment

const searchInput = searchBox.querySelector('input[type="text"]');
searchInput.style.padding = '10px'; // Add padding
searchInput.style.border = '1px solid #ccc'; // Border style
searchInput.style.borderRadius = '5px'; // Rounded corners
searchInput.style.flexGrow = '1'; // Allow input to grow

const searchButton = searchBox.querySelector('button');
searchButton.style.padding = '10px 20px'; // Padding for button
searchButton.style.backgroundColor = '#4CAF50'; // Green background for button
searchButton.style.color = 'white'; // White text for button
searchButton.style.border = 'none'; // No border for button
searchButton.style.cursor = 'pointer'; // Pointer cursor
searchButton.style.borderRadius = '5px'; // Rounded corners

// Style the hero section
const heroSection = document.querySelector('.hero_section');
heroSection.style.backgroundColor = '#f4f4f4'; // Light background
heroSection.style.padding = '50px 20px'; // Padding
heroSection.style.textAlign = 'center'; // Center text
heroSection.style.borderRadius = '10px'; // Rounded corners
heroSection.style.marginTop = '20px'; // Margin at the top

const heroHeading = heroSection.querySelector('h1');
heroHeading.style.fontSize = '2.5em'; // Larger heading font size
heroHeading.style.marginBottom = '10px'; // Space below heading

const heroParagraph = heroSection.querySelector('p');
heroParagraph.style.fontSize = '1.2em'; // Increase paragraph font size
heroParagraph.style.lineHeight = '1.5'; // Increase line height for readability

// Style buttons in the hero section
const heroButton = heroSection.querySelector('a');
heroButton.style.display = 'inline-block'; // Make the button inline block
heroButton.style.marginTop = '20px'; // Add margin
heroButton.style.padding = '10px 20px'; // Padding
heroButton.style.backgroundColor = '#4CAF50'; // Green background
heroButton.style.color = 'white'; // White text
heroButton.style.textDecoration = 'none'; // Remove underline
heroButton.style.borderRadius = '5px'; // Rounded corners
heroButton.style.transition = 'background-color 0.3s'; // Smooth transition

heroButton.addEventListener('mouseover', () => {
    heroButton.style.backgroundColor = '#45a049'; // Darker green on hover
});
heroButton.addEventListener('mouseout', () => {
    heroButton.style.backgroundColor = '#4CAF50'; // Reset background
});

// Style the courses section
const coursesSection = document.querySelectorAll('.courses_section');
coursesSection.forEach(section => {
    section.style.padding = '40px 20px'; // Padding for sections
    section.style.textAlign = 'center'; // Center text
});

// Style individual course boxes
const courseBoxes = document.querySelectorAll('.course_box');
courseBoxes.forEach(box => {
    box.style.border = '1px solid #ddd'; // Border for course boxes
    box.style.borderRadius = '8px'; // Rounded corners
    box.style.padding = '20px'; // Padding
    box.style.margin = '15px'; // Margin
    box.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.1)'; // Subtle shadow
    box.style.transition = 'transform 0.3s'; // Smooth scaling on hover

    box.addEventListener('mouseover', () => {
        box.style.transform = 'scale(1.05)'; // Scale up on hover
    });
    box.addEventListener('mouseout', () => {
        box.style.transform = 'scale(1)'; // Reset scale
    });
});

// Style the testimonials section
const testimonials = document.querySelectorAll('.testimonial_box');
testimonials.forEach(testimonial => {
    testimonial.style.border = '1px solid #ddd'; // Border for testimonial boxes
    testimonial.style.borderRadius = '8px'; // Rounded corners
    testimonial.style.padding = '20px'; // Padding
    testimonial.style.margin = '15px'; // Margin
    testimonial.style.boxShadow = '0 2px 5px rgba(0, 0, 0, 0.1)'; // Shadow
});

// Style the footer section
const footer = document.querySelector('.footer_section');
footer.style.backgroundColor = '#333'; // Dark background
footer.style.color = 'white'; // White text
footer.style.padding = '20px'; // Padding
footer.style.textAlign = 'center'; // Center text
footer.style.position = 'relative'; // Positioning for elements
footer.style.bottom = '0'; // Stay at the bottom

const footerLinks = footer.querySelectorAll('a');
footerLinks.forEach(link => {
    link.style.color = '#4CAF50'; // Green links
    link.style.textDecoration = 'none'; // Remove underline
});

// Add hover effect for footer links
footerLinks.forEach(link => {
    link.addEventListener('mouseover', () => {
        link.style.color = '#fff'; // White on hover
    });
    link.addEventListener('mouseout', () => {
        link.style.color = '#4CAF50'; // Reset color
    });
});
