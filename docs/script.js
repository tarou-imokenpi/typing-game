var type_key;
var targetText;
var current_text = 0; // 現在のテキストのインデックス
var currentIndex = 0; // 現在の文字のインデックス
var gameStart_flag = false;

// 非同期でタイピングテキストを入手
$.ajax({
    url: 'General Programming Terms.csv'
}).done(function(data, textStatus, jqXHR){
    targetText = $.csv.toArrays(data);
    console.log(targetText);
}).fail(function(jqXHR, textStatus, errorThrown){
    console.log(errorThrown);
});

// HTMLElementの取得
var type_text = document.getElementById("type_text");
var typed_text = document.getElementById("typed_text");
var typing_text = document.getElementById("typing_text");
var gameStart_btn = document.getElementById("game-start-btn");


function gameStart() {
    gameStart_flag = true;
    gameStart_btn.style.visibility = "hidden";
    type_text.innerText = targetText[current_text];
    typing_text.innerText = targetText[current_text];
};

// EventListener
document.addEventListener("keypress",(event) =>{
    type_key = event.key;
    var typing_text_len = typing_text.length
    var targetText_len= targetText.length
    
    if (gameStart_flag == true){
        console.log(`text_num:${current_text}`)
    console.log(`index:${currentIndex}`)
    if (type_key == targetText[current_text][0][currentIndex] ){
        typing_text.innerText = typing_text.textContent.slice(1,typing_text_len)
        typed_text.innerHTML = `<span style="background-color: yellow">${typed_text.textContent + type_key}</span>`;
        currentIndex++;
    }
        if (currentIndex  == targetText[current_text][0].length){
            currentIndex = 0;
            current_text++;
            typed_text.innerText = "";

            if (current_text < targetText_len){
                type_text.innerText = targetText[current_text];
                typing_text.innerText = targetText[current_text];
            }
            else{
                type_text.innerText = "ゲームクリア！！";
                gameStart_btn.style.visibility = "visible";
                current_text = 0; // 現在のテキストのインデックス
                currentIndex = 0; // 現在の文字のインデックス
                gameStart_flag = false;
            }
        }
    }
});


