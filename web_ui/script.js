var type_key;
var targetText  = ["typing","tarou"];
var current_text = 0; // 現在のテキストのインデックス
var currentIndex = 0; // 現在の文字のインデックス

var typing_text = document.getElementById("typing_text");

typing_text.innerText = targetText[current_text]
// EventListener
document.addEventListener("keypress",(event) =>{
    type_key = event.key;


    if (type_key == targetText[current_text][currentIndex] ){
        console.log(targetText[current_text][currentIndex]);
        console.log("一致");
        currentIndex++;
    }
        if (currentIndex == targetText[current_text].length){
            console.log("問題クリア！！");
            currentIndex = 0; 
            current_text++;
            if (current_text < targetText.length){
            typing_text.innerText = targetText[current_text];
            }
            else{
                typing_text.innerText = "ゲームクリア！！"
            }
}
        
    else {
        console.log("不一致");
    }
});


