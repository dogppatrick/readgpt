// ==UserScript==
// @name         Add Current URL to Payload
// @namespace    http://your-namespace.com
// @version      1.0
// @description  Adds the current URL to the payload when making requests.
// @match        https://www.ptt.cc/bbs/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 建立按鈕元素
    const button = document.createElement('button');
    button.textContent = 'Send Request';
    button.style.position = 'fixed';
    button.style.top = '50px';
    button.style.left = '50px';
    document.body.appendChild(button);

    // 點擊按鈕時執行請求
    button.addEventListener('click', () => {
        // 取得當前網址
        const currentUrl = window.location.href;
        const serverUrl = 'http://127.0.0.1:8000/gpt_summary/'

        // 發送網路請求
        fetch(serverUrl, {
            method: 'POST', // 或其他你需要的 HTTP 方法
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: { url: currentUrl } }) // 將當前網址作為 payload
        })
            .then(response => response.text()) // 將回應轉換為文字
            .then(data => {
                // 顯示回應在畫面上
                const responseDiv = document.createElement('div');
                responseDiv.textContent = data;
                responseDiv.style.position = 'fixed';
                responseDiv.style.top = '80px';
                responseDiv.style.left = '50px';
                responseDiv.style.backgroundColor = 'white';
                responseDiv.style.padding = '10px';
                document.body.appendChild(responseDiv);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
})();