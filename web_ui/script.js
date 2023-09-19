var type_key;
var targetText  = ["typing","tarou"];
var current_text = 0; // 現在のテキストのインデックス
var currentIndex = 0; // 現在の文字のインデックス

var type_text = document.getElementById("type_text");
var typed_text = document.getElementById("typed_text");

type_text.innerText = targetText[current_text];

// EventListener
document.addEventListener("keypress",(event) =>{
    type_key = event.key;
    

    if (type_key == targetText[current_text][currentIndex] ){
        console.log(targetText[current_text][currentIndex]);
        console.log("一致");
        typed_text.innerHTML = `<span style="background-color: yellow">${typed_text.textContent + type_key}</span>`
        currentIndex++;
    }
        if (currentIndex == targetText[current_text].length){
            console.log("問題クリア！！");
            currentIndex = 0; 
            current_text++;
            typed_text.innerText = "";
            if (current_text < targetText.length){
            type_text.innerText = targetText[current_text];
            }
            else{
                type_text.innerText = "ゲームクリア！！"
            }
}
});


