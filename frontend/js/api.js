// Quantum API Service
// Handles all communication with the FastAPI backend

const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
    ? 'http://localhost:8080' 
    : ''; // Empty means relative to the same origin in production

window.QuantumAPI = {

    // ---- Universal Request Helper ----
    // Sends a POST request with JSON body and returns parsed JSON.
    // Includes a timeout mechanism to prevent hanging requests.
    request: async (endpoint, body = {}, timeoutMs = 120000) => {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeoutMs);
        
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(body),
                signal: controller.signal
            });
            
            clearTimeout(timeoutId);
            
            if (!response.ok) {
                const errData = await response.json().catch(() => ({}));
                throw new Error(errData.detail || errData.message || `Server Error: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            clearTimeout(timeoutId);
            if (error.name === 'AbortError') {
                throw new Error("Request timed out. The AI is taking too long to respond.");
            }
            throw error;
        }
    },

    // ---------------- AI DOUBT SOLVER ----------------
    ask: async (question) => {
        try {
            return await QuantumAPI.request('/ask', { question });
        } catch (error) {
            console.error("QuantumAPI Ask Error:", error);
            throw error;
        }
    },

    // ---------------- AI NOTES ----------------
    getNotes: async (course, topic) => {
        try {
            return await QuantumAPI.request('/notes', { course, topic });
        } catch (error) {
            console.error("QuantumAPI Notes Error:", error);
            throw error;
        }
    },

    // ---------------- PYQs ----------------
    getPyq: async (course, subject) => {
        try {
            return await QuantumAPI.request('/pyq', { course, subject });
        } catch (error) {
            console.error("QuantumAPI PYQ Error:", error);
            throw error;
        }
    },

    // ---------------- EXAM ----------------
    getExam: async (course, subject, level) => {
        try {
            return await QuantumAPI.request('/exam', { course, subject, level });
        } catch (error) {
            console.error("QuantumAPI Exam Error:", error);
            throw error;
        }
    },

    // ---------------- TEXTBOOK GENERATOR ----------------
    generateTextbook: async (level, course, subject) => {
        try {
            return await QuantumAPI.request('/textbook/generate', { level, course, subject });
        } catch (error) {
            console.error("QuantumAPI Textbook Error:", error);
            throw error;
        }
    },

    // ---------------- AUTHENTICATION ----------------
    login: async (email, password) => {
        try {
            return await QuantumAPI.request('/api/login', { email, password });
        } catch (error) {
            console.error("QuantumAPI Login Error:", error);
            throw error;
        }
    },

    signup: async (userData) => {
        try {
            return await QuantumAPI.request('/api/signup', userData);
        } catch (error) {
            console.error("QuantumAPI Signup Error:", error);
            throw error;
        }
    }
};
