const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Set up Nodemailer
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'bongstrokes06@gmail.com', // Replace with your actual email address
    pass: 'chgo bgob vdck kyrz'         // Replace with your actual email password
  }
});

// Textlocal API key
const TEXTLOCAL_API_KEY = 'NDM0MjQyNjg2NzcyNDg0YjM3Njc2NDcwNmE2NjRlNmU='; // Replace with your actual Textlocal API key

// Route for sending emails
app.post('/send-email', (req, res) => {
  const { to, subject, text } = req.body;

  const mailOptions = {
    from: 'bongstrokes06@gmail.com',
    to: to,
    subject: subject,
    text: text
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return res.status(500).send(error.toString());
    }
    res.status(200).send('Email sent: ' + info.response);
  });
});

// Route for sending Bulk SMS
app.post('/send-sms', (req, res) => {
  const { to, body } = req.body;

  // Convert the "to" field into a comma-separated string if it is an array
  const recipients = Array.isArray(to) ? to.join(',') : to;

  // Textlocal SMS API URL
  const smsApiUrl = 'https://api.textlocal.in/send/';

  // Prepare data for the API request
  const params = new URLSearchParams({
    apikey: TEXTLOCAL_API_KEY,
    numbers: recipients,
    message: body,
    sender: '600010', // Use your Textlocal sender ID
    template_id: '1107160691313669232' // Use your template ID
  });

  // Make POST request to Textlocal API
  axios.post(smsApiUrl, params.toString())
    .then(response => {
      console.log(response.data); // Log response for debugging
      res.status(200).send('SMS sent: ' + JSON.stringify(response.data));
    })
    .catch(error => {
      console.error(error); // Log error for debugging
      res.status(500).send(error.toString());
    });
});

// Start the server
app.listen(port, () => {
  console.log(Server running at http://localhost:${port}/);
});
