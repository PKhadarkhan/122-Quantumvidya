let videoStream = null;
let proctorInterval = null;

async function startProctoring(videoId, testId) {
    const video = document.getElementById(videoId);

    try {
        videoStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
        video.srcObject = videoStream;
        
        // Start capturing frames every 3 seconds
        proctorInterval = setInterval(() => captureAndSendFrame(video, testId), 3000);
        
        // Start window tab monitoring
        window.addEventListener('blur', () => {
            logWindowEvent(testId);
        });

    } catch (err) {
        alert("Camera/Microphone access is required for this proctored exam.");
        console.error(err);
    }
}

function captureAndSendFrame(video, testId) {
    if (!videoStream) return;
    
    const canvas = document.createElement("canvas");
    canvas.width = 320;
    canvas.height = 320;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    const imgData = canvas.toDataURL('image/jpeg', 0.5);
    
    QuantumAPI.sendVideoFeed(imgData, testId);
}

function logWindowEvent(testId) {
    QuantumAPI.sendWindowEvent(testId);
    alert("Warning: Switching tabs or minimizing the window is recorded as a violation!");
}

function stopProctoring() {
    if (videoStream) {
        videoStream.getTracks().forEach(track => track.stop());
    }
    if (proctorInterval) {
        clearInterval(proctorInterval);
    }
}
