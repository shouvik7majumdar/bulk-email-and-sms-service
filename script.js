// Regular expressions for validation 
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; 
const phoneRegex = /^\+?[1-9]\d{1,14}$/;

// Function to handle form submission
function sendBulk() {
    const type = document.getElementById('type').value;
    const content = document.getElementById('content').value.trim();
    const recipients = document.getElementById('recipients').value.trim();
    const responseDiv = document.getElementById('response');
    
    const emailCheckbox = document.getElementById('emailCheckbox').checked;
    const smsCheckbox = document.getElementById('smsCheckbox').checked;

    // Validate content
    if (!content) {
        showAlert('Please enter message content.', 'error');
        return;
    }

    // Split recipients by newline and validate each
    const recipientsList = recipients.split('\n').map(item => item.trim()).filter(item => item);

    const invalidEmails = recipientsList.filter(recipient => emailCheckbox && !emailRegex.test(recipient));
    const invalidPhones = recipientsList.filter(recipient => smsCheckbox && !phoneRegex.test(recipient));

    if (invalidEmails.length > 0) {
        showAlert(Invalid email addresses: ${invalidEmails.join(', ')}, 'error');
        return;
    }

    if (invalidPhones.length > 0) {
        showAlert(Invalid phone numbers: ${invalidPhones.join(', ')}, 'error');
        return;
    }

    if (recipientsList.length === 0) {
        showAlert('Please enter valid recipients.', 'error');
        return;
    }

    // Show loading message
    showAlert('Sending messages...', 'info');

    // Example AJAX request using fetch
    const payload = {
        type: emailCheckbox ? 'email' : 'sms',  // Adjust based on checkbox selection
        content: content,
        recipients: recipientsList
    };

    fetch('/api/sendBulk', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert(Successfully sent ${payload.type} to ${recipientsList.length} recipients., 'success');
        } else {
            showAlert(Failed to send ${payload.type}. Error: ${data.message}, 'error');
        }
    })
    .catch((error) => {
        showAlert(An error occurred: ${error.message}, 'error');
    });
}

// Function to show alerts
function showAlert(message, type) {
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = <div class="alert ${type}">${message}</div>;
    responseDiv.style.display = 'block';

    setTimeout(() => {
        responseDiv.style.display = 'none';
    }, 5000);
}