src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"
$(document).ready(function() {
    // Hide the RetainedJob field by default
    $('[name="RetainedJob"]').closest('.form-group').hide();

    // Listen for changes in the NewExist field
    $('[name="NewExist"]').change(function() {
        // If NewExist is Existing
        if ($(this).val() === 'Existing') {
            // Hide the RetainedJob field and set its value to 0
            $('[name="RetainedJob"]').val(0).closest('.form-group').hide();
        } else {
            // If NewExist is not Existing, show the RetainedJob field
            $('[name="RetainedJob"]').closest('.form-group').show();
        }
    });

    // Navigation between form sections
    const sections = document.querySelectorAll('.form-section');
    let currentSection = 0;

    function showSection(index) {
        sections.forEach((section, i) => {
            if (i === index) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });
    }

    function nextSection() {
        if (currentSection < sections.length - 1) {
            currentSection++;
            showSection(currentSection);
        }
    }

    function previousSection() {
        if (currentSection > 0) {
            currentSection--;
            showSection(currentSection);
        }
    }

    document.getElementById('next-button').addEventListener('click', nextSection);
    document.getElementById('previous-button').addEventListener('click', previousSection);

    showSection(currentSection);
});