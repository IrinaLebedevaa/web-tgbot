function sendClick(buttonName) {
    const data = new URLSearchParams();
    data.append("button_name", buttonName);

    navigator.sendBeacon("/track-click/", data);
}