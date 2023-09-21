var type_key;
var targetText  = ["typing","tarou"]; // のちに
var current_text = 0; // 現在のテキストのインデックス
var currentIndex = 0; // 現在の文字のインデックス

// HTMLElementの取得
var type_text = document.getElementById("type_text");
var typed_text = document.getElementById("typed_text");
var typing_text = document.getElementById("typing_text");

type_text.innerText = targetText[current_text];
typing_text.innerText = targetText[current_text];

// EventListener
document.addEventListener("keypress",(event) =>{
    type_key = event.key;
    

    if (type_key == targetText[current_text][currentIndex] )
    {
        typing_text.innerText = typing_text.textContent.slice(1,typing_text.length)
        typed_text.innerHTML = `<span style="background-color: yellow">${typed_text.textContent + type_key}</span>`;
        currentIndex++;
    }
        if (currentIndex == targetText[current_text].length)
        {
            currentIndex = 0; 
            current_text++;
            typed_text.innerText = "";
            
            if (current_text < targetText.length)
            {
                type_text.innerText = targetText[current_text];
                typing_text.innerText = targetText[current_text];
            }
            else
            {
                type_text.innerText = "ゲームクリア！！"
            }
        }
});


