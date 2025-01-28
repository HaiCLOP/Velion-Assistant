document.addEventListener('DOMContentLoaded', () => {
    // Animated stars background
    const starsContainer = document.querySelector('.stars');
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        star.style.width = star.style.height = Math.random() * 3 + 'px';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 2 + 's';
        starsContainer.appendChild(star);
    }

    // FAQ Functionality
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            const toggle = question.querySelector('.toggle');
            
            // Close all other answers
            document.querySelectorAll('.faq-answer').forEach(item => {
                if (item !== answer) {
                    item.classList.remove('active');
                    item.previousElementSibling.querySelector('.toggle').textContent = '+';
                }
            });

            // Toggle current answer
            answer.classList.toggle('active');
            toggle.textContent = answer.classList.contains('active') ? '-' : '+';
        });
    });

    // Demo Chat Functionality
    const chatMessages = document.getElementById('chatMessages');
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const micButton = document.getElementById('micButton');

    function addMessage(text, isUser = false) {
        const message = document.createElement('div');
        message.className = `message ${isUser ? 'user' : 'assistant'}`;
        message.innerHTML = `<p>${text}</p>`;
        chatMessages.appendChild(message);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function handleUserInput(text) {
        addMessage(text, true);
        
        // Simulate AI response
        setTimeout(() => {
            let response;
            if (text.toLowerCase().includes('weather')) {
                response = "The current weather is sunny with a temperature of 72°F.";
            } else if (text.toLowerCase().includes('music')) {
                response = "I can play your favorite music on Spotify. What would you like to hear?";
            } else if (text.toLowerCase().includes('joke')) {
                response = "Why don't scientists trust atoms? Because they make up everything! 😄";
            } else if (text.toLowerCase().includes('version')) {
                response = "Velion's latest stable version is 3.1 with AI intregation.";4
            } else if (text.toLowerCase().includes('how are you')) {
                response = "I'm doing great! Thanks for asking.";
            } else if (text.toLowerCase().includes('team')) {
                response = "Velion is developed by a team of 2 developers. They are: Arnav Srivastava And Kavyansh Khaitan.";
            } else if (text.toLowerCase().includes('purpose')) {
                response = "Velion is a AI based website which is developed to help users in their daily life.";
            } else if (text.toLowerCase().includes('who are you')) {
                response = "I'm Velion 3.1, your personal assistant. How can I help you today?";
            } else if (text.toLowerCase().includes('hey')) {
                response = "Hello! How can I help you today?";
            } else if (text.toLowerCase().includes('hello')) {
                response = "Hey! How can I help you today?";
            } else if (text.toLowerCase().includes('hi')) {
                response = "Hi! How can I help you today?";
            } else {
                response = "I'm here to help! You can ask me about the weather, play music, set alarms, or just chat.";
            }
            addMessage(response);
        }, 1000);
    }

    sendButton.addEventListener('click', () => {
        const text = messageInput.value.trim();
        if (text) {
            handleUserInput(text);
            messageInput.value = '';
        }
    });

    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const text = messageInput.value.trim();
            if (text) {
                handleUserInput(text);
                messageInput.value = '';
            }
        }
    });

    let isRecording = false;
    micButton.addEventListener('click', () => {
        isRecording = !isRecording;
        micButton.style.backgroundColor = isRecording ? '#ff4444' : '';
        if (isRecording) {
            addMessage("Listening...");
        } else {
            addMessage("Voice recording stopped.");
        }
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});