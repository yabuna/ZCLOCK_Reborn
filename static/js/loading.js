// Wait for the page to load
window.addEventListener('DOMContentLoaded', function() {
setTimeout(function() {
        // Get the platform from the URL (extracting the platform from the pathname)
    const platform = window.location.pathname.split('/').pop();

        // Add platform-specific class to the body for styling purposes
        document.body.classList.add(platform); // Adds platform class to body (e.g., body.twitter)

        // Update the loading text dynamically based on the platform
        const loadingText = document.querySelector('.loading-text');
        if (loadingText) {
            loadingText.innerText = `Loading ${platform.charAt(0).toUpperCase() + platform.slice(1)}...`;
        }

        // Apply rotating animation for the loader
        const loader = document.querySelector('.loader');
        if (loader) {
            loader.classList.add('rotate'); // Adding rotation class to loader
        }

        // Set the page redirect after animation ends (2 seconds)
        setTimeout(function() {
            window.location.href = '/login/' + platform; // Redirect to platform-specific login
        }, 2000); // Redirect after 2 seconds
    }, 500); // Initial delay before applying animations
});
