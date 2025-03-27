chrome.runtime.onMessage.addListener((message) => {
    if (message.is_malicious) {
        let warningBanner = document.createElement("div");
        warningBanner.style.position = "fixed";
        warningBanner.style.top = "0";
        warningBanner.style.left = "0";
        warningBanner.style.width = "100%";
        warningBanner.style.backgroundColor = "red";
        warningBanner.style.color = "white";
        warningBanner.style.padding = "10px";
        warningBanner.style.textAlign = "center";
        warningBanner.style.fontSize = "18px";
        warningBanner.innerText = "⚠️ Warning: This site might be dangerous!";
        document.body.prepend(warningBanner);
    }
});
