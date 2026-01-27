document$.subscribe(function() {
    // This function executes on `DOMContentLoaded` and on instant navigation

    // Put your code here
    applyConditionalRendering();
    addTranscriberTabClass();
});

function applyConditionalRendering() {
    // Get the site title
    var siteTitle = document.title;

    // Determine which content to show based on the site title
    var showOnAiLab = siteTitle.includes("AI-LAB Documentation");
    var showOnAiCloud = siteTitle.includes("AI Cloud Documentation");

    // Store the visibility state in session storage
    sessionStorage.setItem('showOnAiLab', showOnAiLab);
    sessionStorage.setItem('showOnAiCloud', showOnAiCloud);

    // Update the visibility of elements based on stored values
    updateVisibility();
}

function updateVisibility() {
    var showOnAiLab = sessionStorage.getItem('showOnAiLab') === 'true';
    var showOnAiCloud = sessionStorage.getItem('showOnAiCloud') === 'true';

    // Show or hide elements based on stored values
    var elementsLab = document.querySelectorAll('.show-on-ai-lab');
    elementsLab.forEach(function(element) {
        element.style.display = showOnAiLab ? 'block' : 'none';
    });

    var elementsCloud = document.querySelectorAll('.show-on-ai-cloud');
    elementsCloud.forEach(function(element) {
        element.style.display = showOnAiCloud ? 'block' : 'none';
    });
}

// Add class to Transcriber guide tabs for enhanced styling
function addTranscriberTabClass() {
    // Check if we're on the transcriber page by checking URL or page content
    var isTranscriberPage = window.location.pathname.includes('transcriber') && 
                           (window.location.pathname.includes('index') || window.location.pathname.endsWith('transcriber/'));
    
    if (isTranscriberPage) {
        // Find tabs that have labels containing "Transcriber Interface" and "Transcriber Batch"
        var tabSets = document.querySelectorAll('.tabbed-set');
        tabSets.forEach(function(tabSet) {
            var labels = tabSet.querySelectorAll('.tabbed-labels > label');
            if (labels.length === 2) {
                var labelTexts = Array.from(labels).map(function(label) {
                    return label.textContent.trim();
                });
                // Check if this is the Transcriber Interface/Batch selection
                if (labelTexts.some(function(text) { return text.includes('Transcriber Interface'); }) &&
                    labelTexts.some(function(text) { return text.includes('Transcriber Batch'); })) {
                    tabSet.classList.add('transcriber-tab-selection');
                }
            }
        });
    }
}

// Fallback for standard DOMContentLoaded if document$ is not available
if (typeof document$ === 'undefined') {
    document.addEventListener('DOMContentLoaded', function() {
        applyConditionalRendering();
        addTranscriberTabClass();
    });
}

