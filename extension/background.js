chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === "complete" && tab.url) {
        fetch("http://127.0.0.1:5000/check_url", {  // Flask API endpoint
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: tab.url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.is_malicious) {
                chrome.notifications.create({
                    type: "basic",
                    iconUrl: "icon.png",
                    title: "⚠️ Warning!",
                    message: "This website may be malicious!"
                });

                // Send message to content script
                chrome.tabs.sendMessage(tabId, { is_malicious: true });
            }
        })
        .catch(error => console.error("Error checking URL:", error));
    }
});
