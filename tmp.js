// ==UserScript==
// @name         current url to gpt summary
// @namespace    http://your-namespace.com
// @version      1.1
// @description  Adds the current URL to the payload when making requests.
// @match        https://www.ptt.cc/bbs/*
// @match        https://www.stockfeel.com.tw/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 建立按鈕元素
    const button = document.createElement('button');
    button.textContent = 'Summary';
    button.style.position = 'fixed';
    button.style.top = '250px';
    button.style.right = '50px';
    button.style.border = '2px solid black';
    document.body.appendChild(button);

    let responseDiv; // Declare the variable outside the event listener

    button.addEventListener('click', () => {
        const currentUrl = window.location.href;
        const serverUrl = 'http://127.0.0.1:8000/gpt_summary/';
        if (responseDiv) {
            responseDiv.remove();
        }
        // 發送網路請求
        fetch(serverUrl, {
            method: 'POST', // 或其他你需要的 HTTP 方法
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: { url: currentUrl } }) // 將當前網址作為 payload
        })
            .then(response => response.json()) // 將回應轉換為文字
            .then(data => {
                const summary = data.summary;
                // 顯示回應在畫面上
                responseDiv = document.createElement('div');
                responseDiv.textContent = summary;
                responseDiv.style.position = 'fixed';
                responseDiv.style.top = '350px';
                responseDiv.style.right = '50px';
                responseDiv.style.backgroundColor = 'white';
                responseDiv.style.padding = '10px';
                responseDiv.style.border = '2px solid black';
                responseDiv.style.width = '500px';
                responseDiv.style.whiteSpace = 'pre-wrap';
                document.body.appendChild(responseDiv);
                const removeButton = document.createElement('button');
                removeButton.textContent = 'Close';
                removeButton.style.top = '300px';
                removeButton.style.right = '50px';
                responseDiv.appendChild(removeButton);
                removeButton.addEventListener('click', () => {
                    responseDiv.remove();
                    responseDiv = null;
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
})();