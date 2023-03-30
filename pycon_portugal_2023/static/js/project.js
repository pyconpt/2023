document.addEventListener('DOMContentLoaded', function () {
    let hashtag_text = document.getElementsByClassName("hashtag-text")[0];
    let hashtag_row = document.getElementsByClassName("hashtag-row")[0];

    for (let i = 0; i < 15; i++)
        hashtag_text.parentElement.appendChild(hashtag_text.cloneNode(true));

    for (let i = 0; i < 2; i++)
        hashtag_row.parentElement.appendChild(hashtag_row.cloneNode(true));

}, false);
